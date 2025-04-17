
from app.services.core.api import APIService
from app.services.server.routes import AgentAPIRoutes
from app.types.base import BackendAPIResponse
from app.core.logging import logger


class AgentService:
    """
    Service for interacting with the agent API.
    """

    def __init__(self):
        """
        Initialize the agent API client.
        """
        self.api = APIService[AgentAPIRoutes](
            service_name="Agent API",
            base_url=AgentAPIRoutes.BASE
        )
        logger.info("Initialized AgentAPI")

    def ask_question(self, chat_id: int, question: str) -> str:
        """
        Ask a question to the agent.
        """
        response: BackendAPIResponse = self.api.post(AgentAPIRoutes.ASK_QUESTION, params={"chat_id": chat_id, "question": question})
        return response["data"]

