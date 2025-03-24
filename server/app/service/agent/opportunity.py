import typing as t
import asyncio
from asyncio import Semaphore
import json

from openai import AsyncOpenAI
from app.helpers.prompts.opportunity import SYSTEM_PROMPT, PROMPT


client = AsyncOpenAI()


async def fetch_opportunity(opportunity: t.Dict) -> t.Dict:
    try:
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0.2,
            frequency_penalty=0.1,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": PROMPT.format(opportunities=json.dumps(opportunity, indent=2))
                }
            ],
            response_format={
                "type": "json_object",
            }
        )

        # Parse the JSON response
        try:
            json_response = json.loads(response.choices[0].message.content)
            return json_response
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Error decoding JSON response: {e}")
    except KeyError as e:
        raise KeyError(f"Missing key in opportunity dictionary: {e}")
    except Exception as e:
        # Log or handle other exceptions
        raise e


async def get_opportunity_listings(opportunities: t.List[t.Dict]) -> t.List[t.Dict]:
    # Use asyncio.gather with return_exceptions=True to handle exceptions
    results = await asyncio.gather(*[fetch_opportunity(opportunity) for opportunity in opportunities], return_exceptions=True)
    # Process results to handle exceptions
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            # Handle the exception (e.g., log it, retry, etc.)
            opportunities[i]['response'] = {'error': str(result)}
        else:
            opportunities[i] = result
    return opportunities


if __name__ == "__main__":
    opportunities = [
        {
            "id": "63d3065f-529b-4f23-b50c-afe3ad7a5d82",
            "rewardAmount": None,
            "deadline": "2025-03-31T12:04:40.000Z",
            "type": "project",
            "title": "Senior Protocol Engineer",
            "token": "USDC",
            "winnersAnnouncedAt": None,
            "slug": "senior-protocol-engineer",
            "isWinnersAnnounced": False,
            "isFeatured": False,
            "compensationType": "variable",
            "minRewardAsk": None,
            "maxRewardAsk": None,
            "status": "OPEN",
            "commentsCount": 2,
            "sponsor": {
                "name": "Okto",
                "slug": "okto",
                "logo": "https://res.cloudinary.com/dgvnuwspr/image/upload/v1713532392/earn-sponsor/exlyno6zymckhciqmp1w.png",
                "isVerified": True,
                "st": False
            }
        },
        {
            "id": "a6b95a85-9821-431a-b040-9062f01fe714",
            "rewardAmount": 1500,
            "deadline": "2025-03-21T15:59:58.000Z",
            "type": "bounty",
            "title": "Superteam Malaysia BOUNTYTHON: Developer Track",
            "token": "USDC",
            "winnersAnnouncedAt": None,
            "slug": "superteam-malaysia-bountython-developer-track",
            "isWinnersAnnounced": False,
            "isFeatured": False,
            "compensationType": "fixed",
            "minRewardAsk": None,
            "maxRewardAsk": None,
            "status": "OPEN",
            "commentsCount": 1,
            "sponsor": {
                "name": "Superteam Malaysia",
                "slug": "Superteam Malaysia",
                "logo": "https://res.cloudinary.com/dgvnuwspr/image/upload/earn-sponsors/pww3gee3mlblvxrdbgub.jpg",
                "isVerified": True,
                "st": True
            }
        },
        {
            "id": "39493277-b4b7-443b-b2c3-8e4a6d1a0db0",
            "rewardAmount": 1500,
            "deadline": "2025-03-21T15:59:32.000Z",
            "type": "bounty",
            "title": "Superteam Malaysia BOUNTYTHON: Research Track",
            "token": "USDC",
            "winnersAnnouncedAt": None,
            "slug": "superteam-malaysia-bountython-research-track",
            "isWinnersAnnounced": False,
            "isFeatured": False,
            "compensationType": "fixed",
            "minRewardAsk": None,
            "maxRewardAsk": None,
            "status": "OPEN",
            "commentsCount": 0,
            "sponsor": {
                "name": "Superteam Malaysia",
                "slug": "Superteam Malaysia",
                "logo": "https://res.cloudinary.com/dgvnuwspr/image/upload/earn-sponsors/pww3gee3mlblvxrdbgub.jpg",
                "isVerified": True,
                "st": True
            }
        },
        {
            "id": "2fdf8d2a-f6a7-4823-81f8-70f5c4ef1a79",
            "rewardAmount": 1500,
            "deadline": "2025-03-21T15:59:28.000Z",
            "type": "bounty",
            "title": "Superteam Malaysia BOUNTYTHON: Content Track",
            "token": "USDC",
            "winnersAnnouncedAt": None,
            "slug": "superteam-malaysia-bountython-content-track",
            "isWinnersAnnounced": False,
            "isFeatured": False,
            "compensationType": "fixed",
            "minRewardAsk": None,
            "maxRewardAsk": None,
            "status": "OPEN",
            "commentsCount": 0,
            "sponsor": {
                "name": "Superteam Malaysia",
                "slug": "Superteam Malaysia",
                "logo": "https://res.cloudinary.com/dgvnuwspr/image/upload/earn-sponsors/pww3gee3mlblvxrdbgub.jpg",
                "isVerified": True,
                "st": True
            }
        },
        {
            "id": "af92c15f-272f-474e-910a-1ef16c0da0b4",
            "rewardAmount": 500,
            "deadline": "2025-03-18T10:18:20.000Z",
            "type": "bounty",
            "title": "List Your Product & Join Our Creator Community!",
            "token": "USDC",
            "winnersAnnouncedAt": None,
            "slug": "list-your-product-and-join-our-creator-community",
            "isWinnersAnnounced": False,
            "isFeatured": False,
            "compensationType": "fixed",
            "minRewardAsk": None,
            "maxRewardAsk": None,
            "status": "OPEN",
            "commentsCount": 8,
            "sponsor": {
                "name": "Sendit Markets",
                "slug": "senditmarkets",
                "logo": "https://res.cloudinary.com/dgvnuwspr/image/upload/v1735897197/acnpnvxsjhnckvv59mic.png",
                "isVerified": False,
                "st": False
            }
        }
    ]

    response = asyncio.run(get_opportunity_listings(opportunities))
    print(response)
