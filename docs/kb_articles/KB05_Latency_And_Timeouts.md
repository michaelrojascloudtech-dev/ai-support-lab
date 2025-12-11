
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
