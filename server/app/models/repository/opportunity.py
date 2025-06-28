import typing as t
import datetime

from pydantic import BaseModel
from sqlalchemy import (
    Column,
    String,
    Float,
    BigInteger,
    DateTime,
    Text,
)

from app.models.core.base import BaseOrm


class OpportunityOrm(BaseOrm):
    __tablename__ = "opportunities"

    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    platform_name = Column(String, nullable=False)
    deadline = Column(DateTime, nullable=False)
    key_skills = Column(Text, nullable=True)  # Store as comma-separated string
    opportunity_type = Column(String, nullable=False)
    location = Column(String, nullable=True, default="remote")
    compensation = Column(String, nullable=True, default="variable")
    know_more_link = Column(String, nullable=False)
    platform_id = Column(String, nullable=True)
    

