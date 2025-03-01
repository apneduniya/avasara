from sqlalchemy import select, delete, func
from sqlalchemy.exc import NoResultFound

from app.models.base import BaseOrm
from app.models.pageable import PageRequestSchema
from app.utils.db_session import get_db_session


class BaseRepository:
    __abstract__ = True

    def __init__(self, model: BaseOrm):
        """
        Initialize the repository with the given model.

        :param model: The SQLAlchemy model to be used by the repository.
        """
        self.__model__ = model

    async def save(self, data):
        """
        Save the given data to the database.

        :param data: The data to be saved.
        :return: The saved data.
        """
        async with get_db_session() as session:
            session.add(data)
            return data

    async def delete(self, data):
        """
        Delete the given data from the database.

        :param data: The data to be deleted.
        """
        async with get_db_session() as session:
            await session.delete(data)

    async def get_by_id(self, id, *args):
        """
        Retrieve an entity by its ID.

        :param id: The ID of the entity to be retrieved.
        :param args: Optional default value to return if no result is found.
        :return: The entity with the given ID, or the default value if provided.
        :raises NoResultFound: If no entity is found and no default value is provided.
        """
        async with get_db_session() as session:
            try:
                execute = await session.execute(select(self.__model__).filter_by(id=id))
                return execute.one()[0]
            except NoResultFound as e:
                if args:
                    return args[0]
                raise e

    async def delete_by_id(self, entity_id: int):
        """
        Delete an entity by its ID.

        :param entity_id: The ID of the entity to be deleted.
        """
        async with get_db_session() as session:
            await session.execute(delete(self.__model__).filter_by(id=entity_id))

    async def get_by_ids(self, ids, *args):
        """
        Retrieve entities by their IDs.

        :param ids: A list of IDs of the entities to be retrieved.
        :param args: Optional default value to return if no result is found.
        :return: A list of entities with the given IDs, or the default value if provided.
        :raises NoResultFound: If no entities are found and no default value is provided.
        """
        async with get_db_session() as session:
            try:
                return await session.execute(select(self.__model__).filter(self.__model__.id.in_(ids))).fetchall()
            except NoResultFound as e:
                if args:
                    return args[0]
                raise e

    async def get_paged_items(self, pageable: PageRequestSchema, params: dict):
        """
        Retrieve a paginated list of entities based on the given parameters.

        :param pageable: The pagination and sorting information.
        :param params: The filter parameters.
        :return: A tuple containing the list of entities and the total count.
        """
        async with get_db_session() as session:
            data = []
            execute = await session.execute(select(func.count()).select_from(self.__model__).filter_by(**params))
            total_count = execute.scalar()
            if total_count > 0:
                sort = getattr(self.__model__, pageable.sort)
                execute = await session.execute(
                    select(self.__model__).filter_by(**params).order_by(pageable.sql_sort(sort))
                    .limit(pageable.size).offset(pageable.offset)
                )
                data = execute.scalars().all()
            return data, total_count