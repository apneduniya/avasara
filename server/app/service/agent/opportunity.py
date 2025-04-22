import typing as t
import asyncio
import json

from app.static.prompts.opportunity import SYSTEM_PROMPT, PROMPT
from app.models.opportunity import Opportunity
from app.helpers.verify.verify_opportunity_data import verify_and_format_opportunity_fields
from app.static.key_skills import AVAILABLE_KEY_SKILLS
from app.core.logging import logger
from app.service.core.llm import LLM
from app.static.llm import OpenAIModel, GeminiModel


async def process_opportunity(opportunities: t.List[t.Dict]) -> t.List[Opportunity]:
    """
    Process opportunities asynchronously and processes them through the LLM.

    Args:
        opportunities (List[Dict]): List of opportunity dictionaries containing details like title,
            reward amount, deadline etc.

    Returns:
        List[Opportunity]: Processed opportunities as Opportunity model instances
    """
    try:
        logger.info(f"Processing {len(opportunities)} opportunities through LLM")
        
        # Initialize LLM client
        llm = LLM(OpenAIModel.GPT_4O)
        
        # Make the API call
        response = await llm.chat_completion(
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT.format(available_key_skills=AVAILABLE_KEY_SKILLS)
                },
                {
                    "role": "user",
                    "content": PROMPT.format(opportunities=json.dumps(opportunities, indent=2))
                }
            ],
            temperature=0.2,
            frequency_penalty=0.1,
            response_format={
                "type": "json_object",
            }
        )

        # Parse the JSON response
        try:
            json_response = json.loads(response.content)
            logger.debug(f"Received response from LLM: {json_response}")

            # Ensure we have a list of opportunities
            # if the response is a dictionary, we need to convert it to a list
            if isinstance(json_response, dict):
                opportunities_list = [json_response]
            elif isinstance(json_response, list):
                opportunities_list = json_response
            else:
                logger.error(f"Invalid response format from LLM: {type(json_response)}")
                raise ValueError("Response must be a list or dictionary")

            # Verify fields and format each opportunity
            processed_opportunities = []
            for opp in opportunities_list:
                try:
                    opportunity = verify_and_format_opportunity_fields(opp)
                    if opportunity:
                        processed_opportunities.append(opportunity)
                except Exception as e:
                    logger.error(f"Error processing opportunity: {e}")
                    continue

            logger.info(f"Successfully processed {len(processed_opportunities)} opportunities")
            return processed_opportunities

        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON response from LLM: {e}")
            raise json.JSONDecodeError(f"Error decoding JSON response: {e}")
    except KeyError as e:
        logger.error(f"Missing key in opportunities: {e}")
        raise KeyError(f"Missing key in opportunities: {e}")
    except Exception as e:
        logger.error(f"Unexpected error processing opportunities: {e}")
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
    total_chunks = (len(opportunities) + chunk_size - 1) // chunk_size
    logger.info(f"Processing {len(opportunities)} opportunities in {total_chunks} chunks of size {chunk_size}")

    for i in range(0, len(opportunities), chunk_size):
        chunk = opportunities[i:i + chunk_size]
        try:
            logger.debug(f"Processing chunk {i//chunk_size + 1}/{total_chunks}")
            chunk_result = await process_opportunity(chunk)
            results.extend(chunk_result if isinstance(
                chunk_result, list) else [chunk_result])
        except Exception as e:
            logger.error(f"Error processing chunk {i//chunk_size + 1}: {e}")
            # Handle the exception by adding error responses for the whole chunk
            error_responses = [{'response': {'error': str(e)}} for _ in chunk]
            results.extend(error_responses)

    logger.info(f"Completed processing all chunks. Total processed opportunities: {len(results)}")
    return results
