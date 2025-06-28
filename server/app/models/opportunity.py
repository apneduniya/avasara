import datetime
import typing as t
from uuid import uuid4

from app.models.core.base import BaseSchema
from app.models.repository.opportunity import OpportunityOrm


class Opportunity(BaseSchema):
    __orm__ = OpportunityOrm
    
    title: str
    description: str # short description
    platform_name: str
    deadline: datetime.datetime
    key_skills: t.List[str]
    opportunity_type: t.Literal["job", "internship", "freelance", "hackathon", "scholarship", "fellowship", "grant", "internship", "other"]
    location: t.Optional[str] = "remote"
    compensation: t.Optional[str] = "variable"
    know_more_link: str
    platform_id: t.Optional[str] = None

    def to_orm(self) -> OpportunityOrm:
        orm = super().to_orm()

        # Convert list to comma-separated string
        orm.key_skills = ", ".join(self.key_skills)
        
        return orm

