
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
