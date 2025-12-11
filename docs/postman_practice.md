
# Postman Practice

Postman is one of the core tools used by API Support Engineers to reproduce issues, analyze requests, and isolate whether problems come from the front end or the backend. This guide covers how to use Postman with this lab’s API and how to trigger every error.

---

## 1. Setup

### Install Postman (Desktop App)
Download from:
https://www.postman.com/downloads/

Use the desktop version so you can call:
`http://localhost:3000`  
without needing a browser agent.

---

## 2. Making your first request

Create a new **POST** request.

### URL:
```
http://localhost:3000/api/process
```

### Headers:
- `Content-Type: application/json`
- `x-api-key: test_api_key`

### Body → raw → JSON:
```json
{
  "text": "Hello world"
}
```

Click **Send** → expect:

- Status: `200 OK`
- Time: small (fast)
- JSON response body

---

## 3. Triggering each error in Postman

You can simulate every error in this lab using the `debug` field or malformed requests.

### 400 – missing_text
```json
{}
```

### 401 – invalid_api_key  
Use wrong header:
```
x-api-key: wrongkey
```

### 403 – forbidden
```json
{ "debug": "forbidden" }
```

### 404 – not_found  
Wrong URL:
```
http://localhost:3000/wrong
```

### 408 – timeout
```json
{ "debug": "timeout" }
```

### 409 – conflict
```json
{ "debug": "conflict" }
```

### 413 – payload_too_large  
Send a huge `"text"` value.

### 422 – unprocessable_entity
```json
{ "debug": "unprocessable_entity" }
```

### 429 – rate_limit
```json
{ "debug": "rate_limit" }
```

### 500 – server_error
```json
{ "debug": "server_error" }
```

### Slow 200 – slow_api_response
```json
{ "debug": "slow_api_response" }
```

### High latency – high_latency
```json
{ "debug": "high_latency" }
```

---

## 4. How to analyze requests in Postman

### Status line
Shows:
- Status code  
- Response time  
- Response size  

### Body view
- **Pretty**: formatted JSON  
- **Raw**: exact server output  
- **Preview**: web preview  

### Headers
Check:
- CORS (backend response headers)
- Rate limit headers
- Content-Type
- Server details

### Cookies (if any)
Rare in API testing but can appear.

---

## 5. Postman Console (VERY important)

Open:
**View → Show Postman Console**

The console shows:
- Full request timeline  
- Network errors  
- Redirects  
- DNS resolution  
- Socket hangups  
- Exact payload sent  

This is the Postman equivalent of the browser’s Network tab.

---

## 6. Why Support Engineers use Postman

Postman helps determine:
- If the frontend is adding wrong headers  
- If JSON is malformed  
- If CORS is blocking the browser  
- Whether the backend is actually down  
- Whether latency is real or UI-based  
- If rate limits are triggered  

If Postman works but browser doesn’t → **frontend/CORS issue**  
If both fail → **backend or payload issue**  
If only Python fails → **environment issue**  
If only Postman fails → **rare header or auth mismatch**

---

## 7. Explaining Postman results to a customer

Professional explanation:

> “I tested your request in Postman using the same payload and headers. The API returned a 200 OK response, which confirms the backend is working correctly. The issue appears to be in the frontend request formatting. Here’s how you can fix it…”  

Or:

> “I reproduced the same 500 error using Postman, which confirms this is a server-side issue. I’m escalating this with full request details.”

Postman is your single source of truth.
```
