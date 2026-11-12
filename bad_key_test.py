import json, urllib.request, urllib.error

url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer wrong-key",
    "User-Agent": "course-test/1.0",
}
body = json.dumps({
    "model": "openai/gpt-oss-20b",
    "max_tokens": 50,
    "messages": [{"role": "user", "content": "Hi"}],
}).encode()

req = urllib.request.Request(url, data=body, headers=headers, method="POST")
try:
    urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print("Status:", e.code)
    print("Body:", e.read().decode())
