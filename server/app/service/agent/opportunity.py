import typing as t
import asyncio
import json

from openai import AsyncOpenAI

from app.helpers.prompts.opportunity import SYSTEM_PROMPT, PROMPT
from app.models.opportunity import Opportunity
from app.helpers.verify.verify_opportunity_data import verify_and_format_opportunity_fields


client = AsyncOpenAI()


async def process_opportunity(opportunities: t.List[t.Dict]) -> t.List[Opportunity]:
    """
    Process opportunities asynchronously and processes them through the OpenAI API.

    Args:
        opportunities (List[Dict]): List of opportunity dictionaries containing details like title,
            reward amount, deadline etc.

    Returns:
        List[Opportunity]: Processed opportunities as Opportunity model instances
    """
    try:
        response = await client.chat.completions.create(
            model="gpt-4o",
            temperature=0.2,
            frequency_penalty=0.1,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": PROMPT.format(opportunities=json.dumps(opportunities, indent=2))
                }
            ],
            response_format={
                "type": "json_object",
            }
        )

        # Parse the JSON response
        try:
            json_response = json.loads(response.choices[0].message.content)

            # Ensure we have a list of opportunities
            # if the response is a dictionary, we need to convert it to a list
            if isinstance(json_response, dict):
                opportunities_list = [json_response]
            elif isinstance(json_response, list):
                opportunities_list = json_response
            else:
                raise ValueError("Response must be a list or dictionary")

            # Verify fields and format each opportunity
            processed_opportunities = []
            for opp in opportunities_list:
                try:
                    opportunity = verify_and_format_opportunity_fields(opp)
                    if opportunity:
                        processed_opportunities.append(opportunity)
                except Exception as e:
                    print(f"Error processing opportunity: {e}")
                    continue

            return processed_opportunities

        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Error decoding JSON response: {e}")
    except KeyError as e:
        raise KeyError(f"Missing key in opportunities: {e}")
    except Exception as e:
        # Log or handle other exceptions
        raise e


async def process_opportunity_by_chunk(opportunities: t.List[t.Dict], chunk_size: int = 5) -> t.List[Opportunity]:
    """
    Process opportunities in chunks

    Args:
        opportunities (List[Dict]): List of opportunity dictionaries containing details like title,
            reward amount, deadline etc.

    Returns:
        List[Opportunity]: Processed opportunities as Opportunity model instances
    """
    results = []

    for i in range(0, len(opportunities), chunk_size):
        chunk = opportunities[i:i + chunk_size]
        try:
            chunk_result = await process_opportunity(chunk)
            results.extend(chunk_result if isinstance(
                chunk_result, list) else [chunk_result])
        except Exception as e:
            # Handle the exception by adding error responses for the whole chunk
            error_responses = [{'response': {'error': str(e)}} for _ in chunk]
            results.extend(error_responses)
            # pass

    return results
