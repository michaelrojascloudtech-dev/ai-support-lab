 
Ticket: Slow API Response (200 OK with ~5s Delay)

Customer message:

Customer reports that their API requests return 200 OK but take several seconds to complete. They mention the API feels “slow” even though there’s no error message.

Environment checked

- Chrome
- AI Support Lab (local environment)
- Endpoint: POST /api/process
- Debug flag used: slow_200

Steps to Reproduce

- Open the UI at:
http://localhost:3000/
- Enter text: "hello"
- Select debug flag: slow_200
- Open Chrome DevTools → Network tab
- The request remains pending for ~5 seconds, then completes successfully with 200 OK

What I saw in DevTools

Request payload (Payload tab):
{
  "text": "hello",
  "debug": "slow_200"
}

Response (Response tab):
{
  "input": "hello",
  "result": "olleh",
  "info": "Slow API response simulation (5s delay before response)"
}

Status:
200 OK

Timing (Timing tab):

- Waiting (TTFB): ~5000ms ← major delay
- DNS Lookup: ~0ms
- Initial Connection: ~0ms
- Request Sent: <1ms
- Content Download: <1ms

This confirms the backend is intentionally delaying the response for ~5 seconds before sending the first byte.

My analysis

The request succeeds (200 OK), so there is no failure — the issue is backend slowness.

In this lab, the delayed behavior is intentional based on the slow_200 debug flag.

In real systems, a slow 200 OK usually indicates:

- Heavy server processing
- Long-running DB queries
- File processing / encoding
- Cold starts in serverless environments
- Insufficient server resources
- API gateway waiting on an upstream dependency
- N+1 query issues
- Performance regression in a recent deployment

How I verified:

- DevTools confirms correct payload
- The endpoint is correct (/api/process)
- Status is 200 OK
- TTFB (Waiting) ≈ 5000ms — backend delay
- No network overhead (DNS/Connecting minimal)

Everything aligns with server-side latency.

Reply to Customer

Your request is returning successfully (200 OK), but the server is taking longer than normal to generate the response.

Here are the most common causes of slow API responses:

- The backend operation the endpoint depends on is taking longer than expected.
- If your request triggers a heavy process (database query, file generation, ML model, etc.), this can increase response time.
- Cold-start delays can occur if the server has been idle for a while.
- If this endpoint depends on an upstream service, a slow response there will cause overall latency.

If you can provide a sample request (sanitized) and approximate response time, I can help narrow down where the delay is occurring.

—
Michael Rojas
Technical Support Engineer
The SaaS Tech Support
📞 +1 (555) 123-4567
✉️ michael.rojas@thesaassupport.com

Internal notes

Expected behavior with slow_200. Real slow 200s often relate to backend performance, DB queries, or cold starts. Consider creating a KB article explaining how to read TTFB in DevTools for latency investigations.

## Screenshots

- UI: `screenshots/T12-slow-api-response/ui.png`
- Network: `screenshots/T12-slow-api-response/network.png`
- Headers: `screenshots/T12-slow-api-response/headers.png`
- Payload: `screenshots/T12-slow-api-response/payload.png`
- Response: `screenshots/T12-slow-api-response/response.png`
- Timing: `screenshots/T12-slow-api-response/timing.png`
