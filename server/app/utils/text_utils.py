import typing as t
import tiktoken

from app.config.settings import config


def chunk_text(text: str, max_tokens: int) -> t.List[str]:
    """Split text into chunks based on token count.
    
    Args:
        text: The input text to be chunked
        max_tokens: Maximum number of tokens allowed per chunk
        
    Returns:
        List of text chunks, each containing at most max_tokens tokens
        
    Example:
        >>> chunk_text("Hello world", 2)
        ['Hello', 'world']
    """
    enc = tiktoken.encoding_for_model(config.DEFAULT_EMBEDDING_MODEL)
    words = text.split()
    chunks, chunk, total_tokens = [], [], 0

    for word in words:
        tokens = enc.encode(word)
        if total_tokens + len(tokens) > max_tokens:
            chunks.append(" ".join(chunk))
            chunk, total_tokens = [], 0
        chunk.append(word)
        total_tokens += len(tokens)

    if chunk:
        chunks.append(" ".join(chunk))
    return chunks
