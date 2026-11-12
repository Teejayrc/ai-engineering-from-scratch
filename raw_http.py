import os, json, urllib.request

url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + os.environ["GROQ_API_KEY"],
    "User-Agent": "course-test/1.0",
}
body = json.dumps({
    "model": os.environ.get("LLM_MODEL", "openai/gpt-oss-20b"),
    "max_tokens": 1024,
    "messages": [{"role": "user", "content": "What is a neural network in one sentence?"}],
}).encode()

req = urllib.request.Request(url, data=body, headers=headers, method="POST")
with urllib.request.urlopen(req) as resp:
    print(json.dumps(json.loads(resp.read()), indent=2))
