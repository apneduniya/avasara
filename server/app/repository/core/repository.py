from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional, Any

from sqlalchemy import select, delete, func
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.exc import NoResultFound

from app.models.core.base import BaseOrm
from app.models.core.pageable import PageRequestSchema
from app.repository.core.session import get_db_session


T = TypeVar('T', bound=BaseOrm)


class BaseRepository(ABC, Generic[T]):
    """Abstract base class defining the contract for all repositories"""
    @abstractmethod
    async def save(self, entity: T) -> T:
        pass

    @abstractmethod
    async def delete(self, entity: T) -> None:
        pass

    @abstractmethod
    async def get_by_id(self, id: int) -> Optional[T]:
        pass

    @abstractmethod
    async def delete_by_id(self, entity_id: int) -> None:
        pass

    @abstractmethod
    async def get_by_ids(self, ids: List[int]) -> List[T]:
        pass

    @abstractmethod
    async def get_paged_items(self, pageable: PageRequestSchema, params: dict) -> tuple[List[T], int]:
        pass


class GenericRepository(BaseRepository[T]):
    """Generic implementation of the repository pattern"""
    
    def __init__(self, model: type[T]):
        """
        Initialize the repository with the given model.

        :param model: The SQLAlchemy model class to be used by the repository.
        """
        self._model = model

    async def save(self, entity: T) -> T:
        """
        Save the given entity to the database.

        :param entity: The entity to be saved.
        :return: The saved entity.
        """
        async with get_db_session() as session:
            session.add(entity)
            # First flush to get the ID
            await session.flush()
            # Then commit to persist the changes
            await session.commit()
            return entity

    async def delete(self, entity: T) -> None:
        """
        Delete the given entity from the database.

        :param entity: The entity to be deleted.
        """
        async with get_db_session() as session:
            await session.delete(entity)
            await session.flush()
            await session.commit()

    async def get_by_id(self, id: int) -> Optional[T]:
        """
        Retrieve an entity by its ID.

        :param id: The ID of the entity to be retrieved.
        :return: The entity with the given ID, or None if not found.
        """
        async with get_db_session() as session:
            # Get all relationships that need to be loaded
            relationships = [rel.key for rel in self._model.__mapper__.relationships]
            
            # Build the query with appropriate loading strategies
            query = select(self._model).filter_by(id=id)
            for rel in relationships:
                # Use joinedload for one-to-one or many-to-one
                # Use selectinload for one-to-many or many-to-many
                if rel in self._model.__mapper__.relationships:
                    rel_obj = self._model.__mapper__.relationships[rel]
                    if rel_obj.direction.name in ['ONETOMANY', 'MANYTOMANY']:
                        query = query.options(selectinload(getattr(self._model, rel)))
                    else:
                        query = query.options(joinedload(getattr(self._model, rel)))
            
            result = await session.execute(query)
            return result.scalar_one_or_none()

    async def delete_by_id(self, entity_id: int) -> None:
        """
        Delete an entity by its ID.

        :param entity_id: The ID of the entity to be deleted.
        """
        async with get_db_session() as session:
            await session.execute(
                delete(self._model).filter_by(id=entity_id)
            )
            await session.flush()
            await session.commit()

    async def get_by_ids(self, ids: List[int]) -> List[T]:
        """
        Retrieve entities by their IDs.

        :param ids: A list of IDs of the entities to be retrieved.
        :return: A list of entities with the given IDs.
        """
        async with get_db_session() as session:
            # Get all relationships that need to be loaded
            relationships = [rel.key for rel in self._model.__mapper__.relationships]
            
            # Build the query with appropriate loading strategies
            query = select(self._model).filter(self._model.id.in_(ids))
            for rel in relationships:
                if rel in self._model.__mapper__.relationships:
                    rel_obj = self._model.__mapper__.relationships[rel]
                    if rel_obj.direction.name in ['ONETOMANY', 'MANYTOMANY']:
                        query = query.options(selectinload(getattr(self._model, rel)))
                    else:
                        query = query.options(joinedload(getattr(self._model, rel)))
            
            result = await session.execute(query)
            return result.scalars().all()

    async def get_paged_items(self, pageable: PageRequestSchema, params: dict) -> tuple[List[T], int]:
        """
        Retrieve a paginated list of entities based on the given parameters.

        :param pageable: The pagination and sorting information.
        :param params: The filter parameters.
        :return: A tuple containing the list of entities and the total count.
        """
        async with get_db_session() as session:
            # Get total count
            count_query = select(func.count()).select_from(self._model).filter_by(**params)
            total_count = (await session.execute(count_query)).scalar()

            # Get paginated results
            if total_count > 0:
                sort_column = getattr(self._model, pageable.sort)
                query = (
                    select(self._model)
                    .filter_by(**params)
                    .order_by(pageable.sql_sort(sort_column))
                    .limit(pageable.size)
                    .offset(pageable.offset)
                )
                
                result = await session.execute(query)
                data = result.scalars().all()
            else:
                data = []

            return data, total_count