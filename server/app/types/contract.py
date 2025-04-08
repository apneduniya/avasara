import typing as t
from pydantic import BaseModel, Field

from app.types.base import FrontendAPIResponse


class ContractInfoData(BaseModel):
    owner: str
    registrationFee: str


class UserProfile(BaseModel):
    address: str
    name: t.Optional[str] = None
    skills: t.List[str] = Field(default_factory=list)
    location: t.Optional[str] = None
    registration_date: t.Optional[str] = None


# Response Types
ContractInfoResponse = FrontendAPIResponse[ContractInfoData]
UsersBySkillResponse = FrontendAPIResponse[t.List[UserProfile]]
UsersByLocationResponse = FrontendAPIResponse[t.List[UserProfile]]
RegisteredUsersResponse = FrontendAPIResponse[t.List[UserProfile]]
UserProfileResponse = FrontendAPIResponse[UserProfile]

