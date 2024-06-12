import os
from typing import Dict, List
from groq import Groq

os.environ["GROQ_API_KEY"] = "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"

LLAMA3_70B_INSTRUCT = "llama3-70b-8192"
LLAMA3_8B_INSTRUCT = "llama3-8b-8192"

DEFAULT_MODEL = LLAMA3_70B_INSTRUCT

client = Groq()


def chat_completion(
        messages: List[Dict],
        model=DEFAULT_MODEL,
        temperature: float = 0.6,
        top_p: float = 0.9,
        max_tokens=2048,
) -> str:
    response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        top_p=top_p,
    )
    return response.choices[0].message.content


