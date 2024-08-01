import os
import json
from typing import Dict, List
from groq import Groq

os.environ["GROQ_API_KEY"] = "need_to_add"

LLAMA3_70B_INSTRUCT = "llama3-70b-8192"

DEFAULT_MODEL = LLAMA3_70B_INSTRUCT

client = Groq()


def chat_completion(
        messages: List[Dict],  # A list of messages in the conversation
        model: str = DEFAULT_MODEL,  # The language model to use
        temperature: float = 0.2,  # Controls randomness of responses
        max_tokens: int = 2048,  # Max number of tokens in the response
        top_p: float = 0.9,  # Nucleus sampling for token selection
        stream: bool = False,  # Stream responses in real-time
        stop: List[str] = None,  # Stop sequences to end the response
        seed: int = None,  # Seed for reproducibility
        response_format: Dict[str, str] = None  # Format of the response, for example: {"type": "json_object"}
) -> str:
    response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        stream=stream,
        stop=stop,
        seed=seed,
        response_format=response_format
    )
    return response.choices[0].message.content
