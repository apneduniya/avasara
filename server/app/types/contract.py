import typing as t
from pydantic import BaseModel, Field

from app.types.base import FrontendAPIResponse


class ContractInfoData(BaseModel):
    owner: str
    registrationFee: str


class UserProfile(BaseModel):
    """Complete user profile data"""
    address: str
    # Contract data
    location: str
    primarySkill: str
    secondarySkill: str
    status: str
    language: str
    yearsOfExperience: int
    exists: bool
    professionalStatus: str
    # IPFS data
    fullName: str
    email: str
    telegramUsername: str
    linkedinUrl: t.Optional[str] = None
    twitterUrl: t.Optional[str] = None
    portfolioLink: t.Optional[str] = None


# Response Types
ContractInfoResponse = FrontendAPIResponse[ContractInfoData]
UsersBySkillResponse = FrontendAPIResponse[t.List[UserProfile]]
UsersByLocationResponse = FrontendAPIResponse[t.List[UserProfile]]
RegisteredUsersResponse = FrontendAPIResponse[t.List[UserProfile]]
UserProfileResponse = FrontendAPIResponse[UserProfile]

