import typing as t
import datetime

from app.models.opportunity import Opportunity
from app.helpers.constants import OPPORTUNITY_TYPES
from app.core.logging import logger


def verify_and_format_opportunity_fields(data: t.Dict) -> Opportunity | None:
    """
    It verifies and formats the opportunity fields to match the required schema.

    Args:
        data (Dict): Raw opportunity dictionary

    Returns:
        Opportunity: Formatted opportunity instance
    """

    # Create the formatted opportunity dictionary directly from input data
    try:
        schema = Opportunity(
            title=data["title"],
            description=data["description"],
            platform_name=data["platform_name"],
            deadline=datetime.datetime.fromisoformat(data["deadline"]),
            key_skills=data["key_skills"],
            opportunity_type=data["opportunity_type"],
            know_more_link=data["know_more_link"],
            location=data["location"],
            compensation=data["compensation"],
            platform_id=data["platform_id"]
        )

        return schema
    except Exception as e:
        logger.error(f"Error creating Opportunity instance: {e}")
        return None
