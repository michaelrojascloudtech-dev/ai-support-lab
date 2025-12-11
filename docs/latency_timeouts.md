
# Latency & Timeouts

Latency and timeout issues are extremely common in API systems. This guide explains how to identify slow responses, differentiate between slow 200s and timeouts, and analyze these cases like a Support Engineer.

---

## 1. Key concepts

### **Latency**
The total time it takes for a request to complete.

### **Slow 200**
The request succeeds with a `200 OK` but takes too long.

### **Timeout**
The client or server stops waiting and aborts the request.

### **High latency**
Long delays caused by heavy processing, poor network conditions, or infrastructure load.

This lab includes three latency modes:
- `slow_api_response`
- `high_latency`
- `timeout`

---

## 2. How the lab simulates latency

### `slow_api_response`
The server intentionally delays before returning 200.

### `high_latency`
A heavier delay simulating infrastructure issues.

### `timeout`
Simulates a request that takes too long and triggers a timeout scenario.

---

## 3. Measuring latency with Python

Example pattern used in latency tests:

```python
import time
import requests

url = "http://localhost:3000/api/process"
latencies = []

for i in range(10):
    start = time.time()
    resp = requests.post(url, json={"debug": "slow_api_response"})
    elapsed_ms = (time.time() - start) * 1000
    latencies.append(elapsed_ms)
    print(f"{i}: {resp.status_code} in {elapsed_ms:.1f} ms")

print("Avg:", sum(latencies) / len(latencies), "ms")
print("Min:", min(latencies), "ms")
print("Max:", max(latencies), "ms")
```

This helps identify:
- average latency  
- consistency  
- spikes  
- worst-case delays  

---

## 4. When latency becomes a problem

Latency is concerning when:
- Requests consistently exceed 1–2 seconds  
- Latency spikes occur frequently  
- Slow requests cause UI delays  
- Only some regions/users see slowness  
- The slow endpoint affects critical workflows  

---

## 5. Debugging latency vs timeout

### Step 1 — Compare tools  
- Browser  
- Postman  
- Python script  

If all tools show slowness → backend issue.  
If only browser is slow → network or frontend problem.  
If only Python/Postman is slow → network path issues.

---

### Step 2 — Verify request size  
Large payloads can significantly increase latency.

---

### Step 3 — Check server logs  
Look for slow operations repeating at the same time.

---

### Step 4 — Identify pattern  
- Only certain endpoints slow?  
- Only at peak times?  
- Only when using debug flags?  

---

## 6. Explaining latency to a customer

A clear, professional way to explain latency:

> “Your requests are completing successfully but taking longer than expected. I’ve reproduced the behavior here and confirmed elevated latency on this endpoint. I am collecting logs and details for our engineering team to investigate further.”

And for timeouts:

> “Your request is being terminated after waiting too long for a response. This may be caused by heavy processing, network delays, or a server-side performance issue. I’m escalating with timestamps and request examples.”

---

## 7. When to escalate latency issues

Escalate when:
- Latency consistently exceeds normal baseline  
- Multiple customers report slowness  
- Requests time out repeatedly  
- Region-specific performance issues appear  
- You confirm slow 200s internally  

Latency issues are often early signs of infrastructure problems, so escalating early is good practice.
```
