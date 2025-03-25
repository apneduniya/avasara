import typing as t

from app.models.opportunity import Opportunity
from app.helpers.constants import OPPORTUNITY_TYPES


def verify_and_format_opportunity_fields(data: t.Dict) -> Opportunity | None:
    """
    It verifies and formats the opportunity fields to match the required schema.

    Args:
        data (Dict): Raw opportunity dictionary

    Returns:
        Opportunity: Formatted opportunity instance
    """

    # Create the formatted opportunity dictionary directly from input data
    formatted_opp = {
        "title": data.get("title", ""),
        "description": data.get("description", ""),
        "platform_name": data.get("platform_name", ""),
        "deadline": data.get("deadline", ""),
        "key_skills": data.get("key_skills", []),
        "opportunity_type": data.get("opportunity_type", "other"),
        "know_more_link": data.get("know_more_link", ""),
        "location": data.get("location", ""),
        "compensation": data.get("compensation", "")
    }

    # Use the Opportunity model to ensure the formatted data matches the schema
    try:
        return Opportunity(**formatted_opp)
    except Exception as e:
        print(f"Error creating Opportunity instance: {e}")
        return None
