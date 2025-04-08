

from app.models.opportunity import Opportunity


def format_opportunity(opportunity: Opportunity):
    """
    Format an opportunity into a Telegram message
    """
    title = opportunity.title
    description = opportunity.description
    opportunity_type = opportunity.opportunity_type.capitalize()
    location = opportunity.location
    compensation = opportunity.compensation
    deadline = opportunity.deadline
    link = opportunity.know_more_link

    return (
        f"*{title}*\n"
        f"{description}\n\n"
        f"💼 Type: {opportunity_type}\n"
        f"🌍 Location: {location}\n"
        f"💰 Compensation: {compensation}\n"
        f"⏳ Deadline: {deadline}\n"
        f"🔗 [Know More]({link})"
    )
