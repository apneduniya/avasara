import typing as t


from pydantic import BaseModel


T = t.TypeVar('T')


class BackendAPIResponse(BaseModel, t.Generic[T]):
    """
    Generic API response model for backend
    """
    success: bool
    message: t.Optional[str] = None
    data: t.Optional[T] = None
    error: t.Optional[str] = None