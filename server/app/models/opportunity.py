import typing as t
from uuid import uuid4

from app.models.base.base import BaseSchema



class Opportunity(BaseSchema):
    title: str
    description: str # short description
    platform_name: str
    deadline: str
    key_skills: t.List[str]
    opportunity_type: t.Literal["job", "internship", "freelance", "hackathon", "scholarship", "fellowship", "grant", "internship", "other"]
    location: t.Optional[str] = "remote"
    compensation: t.Optional[str] = "variable"
    know_more_link: str

