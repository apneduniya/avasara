import math
import typing as t

from pydantic import BaseModel
from sqlalchemy.orm import InstrumentedAttribute


T = t.TypeVar('T')

class PageRequestSchema(BaseModel):
    page: t.Optional[int] = 1
    size: t.Optional[int] = 25
    sort: t.Optional[str] = 'created_at'
    direction: t.Optional[t.Literal['ASC', 'DESC']] = 'DESC'

    @property
    def offset(self):
        return (self.page - 1) * self.size

    def sql_sort(self, sort: InstrumentedAttribute):
        return sort.asc() if self.direction == "ASC" else sort.desc()


class PageResponseSchema(BaseModel, t.Generic[T]):
    data: t.List[T]
    total_pages: t.Optional[int]
    total_count: int
    page_size: int

    def __init__(self, **data):
        super().__init__(**data)

        self.total_pages = math.ceil(self.total_count / self.page_size)