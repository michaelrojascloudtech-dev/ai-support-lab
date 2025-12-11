

import os

# Ensure docs folder exists
docs_path = "docs"
os.makedirs(docs_path, exist_ok=True)

articles = {
"KB01_API_Authentication.md": """
# API Authentication Guide

API authentication ensures every request is tied to an authorized user or application. 
Most modern APIs use API keys passed through request headers.

---

## Why Authentication Fails

Common causes:
- Missing API key header
- Misspelled header name (capitalization matters)
- Expired or invalid API key
- Extra spaces or hidden characters
- Sending the key in the query string instead of headers

---

## Correct Header Example

Authorization: Bearer YOUR_API_KEY  
Content-Type: application/json

---

## Incorrect Examples

Auth: KEY  
authorization: apikey  
(no Authorization header at all)

---

## How to Fix

- Verify the header name is exactly: Authorization
- Remove extra spaces around the key
- Ensure the key is active in your dashboard
- Avoid sending API calls directly from the browser (CORS issues)
- Use backend code for secure API requests

---
""",

"KB02_JSON_Formatting.md": """
# Proper JSON Formatting for API Requests

APIs expect valid JSON. If JSON is malformed, the server cannot parse the request.

---

## Common JSON Mistakes

- Missing quotes around keys
- Using single quotes instead of double quotes
- Forgetting commas
- Sending a JavaScript object without converting to JSON

---

## Correct JSON Example

{
  "text": "Hello world"
}

---

## Incorrect JSON Examples

{text: Hello}  
{'text': 'Hello'}

---

## Tips to Avoid JSON Errors

- Always use double quotes
- Set Content-Type: application/json
- Use JSON.stringify() in frontend JavaScript
- Validate JSON in VS Code or online formatters

---
""",

"KB03_Common_HTTP_Errors.md": """
# Common HTTP Errors & How to Troubleshoot Them

HTTP status codes help identify what went wrong with an API request.

---

## 4xx Errors (Client Issues)

400 Bad Request — malformed JSON or missing fields  
401 Unauthorized — missing or invalid API key  
403 Forbidden — correct API key, but lacking permission  
404 Not Found — wrong endpoint or resource  
409 Conflict — resource already exists  
413 Payload Too Large — input exceeds server limits  
422 Unprocessable Entity — valid JSON but invalid data

---

## 5xx Errors (Server Issues)

500 Internal Server Error — unexpected backend failure  
503 Service Unavailable — server temporarily down  
504 Gateway Timeout — server took too long to respond  

---

## Troubleshooting Checklist

1. Verify JSON formatting  
2. Check required fields  
3. Confirm the endpoint path  
4. Inspect headers  
5. Retry with smaller payload  
6. Gather logs, timestamps, screenshots  
7. Escalate if reproducible on valid requests  

---
""",

"KB04_CORS_Explained.md": """
# Understanding CORS and Why It Happens

CORS errors occur when browser-based frontend code attempts to call an API hosted on a different domain.

---

## Why CORS Exists

- Browser security restrictions
- Backend must explicitly allow cross-origin requests
- Prevents malicious websites from calling APIs without permission

---

## Example CORS Error

Access to fetch at 'https://api.example.com' from origin 'http://localhost:3000' 
has been blocked by CORS policy.

---

## How to Fix CORS Issues

- Make API requests from your backend server, not the browser
- Enable CORS only in development (temporary)
- Double-check fetch options such as mode: 'cors'

---

## Important Note

CORS is *not* an API failure.  
It is a browser security mechanism.

---
""",

"KB05_Latency_And_Timeouts.md": """
# Latency and Timeout Troubleshooting

Latency is delay between sending a request and receiving a response.  
Timeouts occur when the delay is too long and the request is aborted.

---

## Why Latency Happens

- High server load or traffic spikes  
- Slow database queries  
- Network congestion  
- Large or complex payloads  
- Inefficient client-side loops or retries  
- Wrong region selected  

---

## Common Symptoms

- Slow UI  
- delayed response from server  
- timeout exceeded  
- Waterfall timing spikes in DevTools  

---

## How to Troubleshoot

1. Test with smaller payloads  
2. Retry after a few seconds (load spike)  
3. Compare regions  
4. Use DevTools timing breakdown  
5. Run repeated requests to detect patterns  

---

## Timeout vs Slow Response

Timeout = no response in max waiting period  
Slow response = response eventually arrives but late

---
""",

"KB06_Escalation_Guidelines.md": """
# Escalation Guidelines for Support Engineers

Not every issue requires engineering involvement.  
Escalations should be meaningful, reproducible, and well-documented.

---

## When You SHOULD Escalate

- Issue is reproducible with valid requests  
- Multiple customers report same backend failure  
- Logs show internal server errors (500/503/504)  
- Latency spikes across regions  
- Rate limits not matching customer plan  
- Security concerns  
- Customer provides clear reproduction steps  

---

## When You SHOULD NOT Escalate

- Customer JSON is invalid  
- Missing or incorrect API key  
- CORS from browser calls  
- Customer exceeding rate limits  
- Payload too large (already documented)  

---

## What to Include in Escalation

- Customer/project ID  
- Exact request + headers  
- Screenshots  
- Logs or timestamps  
- Reproduction steps  
- Expected vs actual result  

---

## Goal of Escalation

Help engineering identify the issue **without repeating support’s investigation**.

---
"""
}

# Write files
for filename, content in articles.items():
    with open(os.path.join(docs_path, filename), "w", encoding="utf-8") as f:
        f.write(content)

print("All KB articles successfully created in /docs/")
