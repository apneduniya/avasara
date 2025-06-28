import openai

from app.config.settings import config
from app.service.core.llm import LLM
from app.static.default import DEFAULT_LLM_MODEL
from app.static.prompts.ask_question import SYSTEM_PROMPT, PROMPT


class RAGService:
    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.llm = LLM(model=DEFAULT_LLM_MODEL)

    async def ask(self, query, top_k=5):
        context_chunks = self.vector_store.search(query, top_k)
        context = "\n\n".join(context_chunks)

        response = await self.llm.chat_completion(
            messages=[{"role": "user", "content": PROMPT.format(context=context, query=query)}]
        )
        return response.content
