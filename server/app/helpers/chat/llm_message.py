import typing as t

from app.models.repository.chat import ChatSchema


def generate_llm_message(chat_history: t.List[ChatSchema]) -> t.List[t.Dict[str, t.Any]]:
    """
    Convert chat history into a format suitable for LLM processing.
    
    This function transforms a list of ChatSchema objects into a list of message dictionaries
    that follow the standard LLM message format with 'role' and 'content' fields.
    
    Args:
        chat_history (List[ChatSchema]): List of chat messages to be converted
        
    Returns:
        List[Dict[str, Any]]: List of messages in LLM format where:
            - role: Either "assistant" (for avasara_bot) or "user" (for other users)
            - content: The actual message content
            
    Example:
        >>> chat_history = [
        ...     ChatSchema(username="user1", message_content="Hello"),
        ...     ChatSchema(username="avasara_bot", message_content="Hi there!")
        ... ]
        >>> messages = generate_llm_message(chat_history)
        >>> print(messages)
        [
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "Hi there!"}
        ]
    """
    messages = []
    for chat in chat_history:
        if chat.username == "avasara_bot":
            messages.append({"role": "assistant", "content": chat.message_content})
        else:
            messages.append({"role": "user", "content": chat.message_content})

    messages.reverse()
    return messages

