
# Practice Scenarios

These scenarios simulate real API Support Engineer situations. Use them to practice reproducing issues, debugging, reading logs, and creating clear explanations or escalations. Each scenario is designed to strengthen your investigation workflow and confidence.

---

## Scenario 1 — CORS vs Backend Issue

### Goal:
Identify when a failure is caused by **CORS** instead of a real API error.

### Steps:
1. Open your frontend HTML file using `file://`  
2. Make an API call → observe a **CORS error**  
3. Now send the same request in Postman

### Expected:
- Browser fails (CORS)
- Postman succeeds

### Key Learning:
If Postman works → the backend is fine, the browser is blocking the request.

---

## Scenario 2 — Broken JSON Body

### Goal:
Identify JSON formatting issues quickly.

### Steps:
1. In Postman, send invalid JSON, for example:

```json
{
  "text": "Hello world",
}
```

2. Observe the `400 missing_text` error  
3. Fix the JSON  
4. Send again

### Key Learning:
Bad JSON often causes missing fields and 400 errors.

---

## Scenario 3 — Latency Spike Investigation

### Goal:
Understand slow 200s and latency patterns.

### Steps:
1. Send:
```json
{ "debug": "high_latency" }
```
2. Measure time in:
   - Postman  
   - Browser  
   - Python latency script  
3. Compare average, min, and max latency

### Key Learning:
Consistent slowness across tools = backend latency.

---

## Scenario 4 — Rate Limit Triggering

### Goal:
Recognize 429 patterns and retry logic.

### Steps:
1. Send multiple requests quickly  
2. Trigger:
```json
{ "debug": "rate_limit" }
```
3. Observe 429 responses  
4. Look for “Retry-After” headers (if implemented)

### Key Learning:
429 errors require backoff, retries, or reduced concurrency.

---

## Scenario 5 — Payload Too Large

### Goal:
Understand when large payloads break requests.

### Steps:
1. Send a huge `"text"` value  
2. Trigger:
```json
{ "debug": "payload_too_large" }
```
—or send a real oversized body  
3. Fix by reducing payload

### Key Learning:
Large bodies cause 413 errors and must be split or optimized.

---

## Scenario 6 — Invalid API Key Troubleshooting

### Goal:
Debug authentication problems.

### Steps:
1. Remove or change the `x-api-key` header  
2. Observe the `401 invalid_api_key` error  
3. Fix the header and retry

### Key Learning:
Most auth issues come from wrong header names or malformed keys.

---

## Scenario 7 — 500 Error + Escalation Practice

### Goal:
Practice writing a clean escalation note.

### Steps:
1. Send:
```json
{ "text": "test", "debug": "server_error" }
```
2. Observe `500 Internal Server Error`  
3. Write a short escalation using:
   - Summary  
   - Reproduction steps  
   - Example payload  
   - Scope  
   - Impact  
   - Evidence  

### Key Learning:
Good escalations are short, complete, and contain all the facts.

---

## Scenario 8 — Frontend vs Backend Comparison

### Goal:
Determine whether an issue is frontend-only.

### Steps:
1. Trigger an error from your HTML test page  
2. Reproduce in:
   - Postman  
   - Python  
3. Compare results

### Expected:
- If only the browser fails → CORS or frontend formatting issue  
- If all tools fail → real backend or request issue  

### Key Learning:
Comparing tools is essential for isolating the cause.

---

## Scenario 9 — JSON vs Form-Encoded Misuse

### Goal:
Spot wrong request data formats.

### Steps:
1. Send valid JSON with the header missing:

```
Content-Type: application/json
```

2. Then send an incorrect form-encoded body:
```
text=Hello
```

3. Compare results

### Key Learning:
Wrong content types lead to parsing failures and missing fields.

---

These scenarios build practical investigation skills and prepare you for real API Support Engineering tasks.
```
