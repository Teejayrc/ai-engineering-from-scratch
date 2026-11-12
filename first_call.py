import os
from groq import Groq

client = Groq()
MODEL = os.environ.get("LLM_MODEL", "llama-3.1-8b-instant")

response = client.chat.completions.create(
    model=MODEL,
    max_tokens=1024,
    messages=[{"role": "user", "content": "What is a neural network in one sentence?"}],
)
print(response.choices[0].message.content)
