import typing as t

from app.core.logging import logger
from app.service.contract.get_data import SmartContractAPI
from app.static.key_skills import AVAILABLE_KEY_SKILLS
from app.types.contract import UserProfile
from app.models.opportunity import Opportunity


class OpportunityMatcher:
    """
    Service for matching opportunities with capable users based on skills
    """
    
    def __init__(self):
        self.smart_contract_api = SmartContractAPI()
        logger.info("Initialized OpportunityMatcher")

    def match_opportunity_with_users(self, opportunity: Opportunity) -> t.List[UserProfile]:
        """
        Match an opportunity with capable users based on key skills
        
        Args:
            opportunity (Opportunity): The opportunity to match
            
        Returns:
            List[UserProfile]: List of capable users
        """
        logger.info(f"Matching opportunity '{opportunity.title}' with users")
        capable_users = []
        
        # Validate and normalize key skills
        validated_key_skills = []
        for skill in opportunity.key_skills:
            if skill not in AVAILABLE_KEY_SKILLS:
                logger.warning(f"Invalid key skill '{skill}' found, defaulting to 'other'")
                validated_key_skills.append("other")
            else:
                validated_key_skills.append(skill)
        opportunity.key_skills = validated_key_skills

        # Get users for each key skill
        for key_skill in opportunity.key_skills:
            try:
                users = self.smart_contract_api.get_users_by_skill(key_skill)
                capable_users.extend(users)
                logger.debug(f"Found {len(users)} users for key skill '{key_skill}'")
            except Exception as e:
                logger.error(f"Error fetching users for key skill '{key_skill}': {e}")
                continue

        logger.info(f"Found {len(capable_users)} capable users for opportunity '{opportunity.title}'")
        return capable_users 