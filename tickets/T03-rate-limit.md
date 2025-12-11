Ticket: 429 Too Many Requests (Rate Limit)

Customer message:
Customer says they're receiving 429 errors even though they aren't calling the API very often.

Environment checked:
- Firefox
- AI Support Lab (local)
- POST /api/process
- Debug flag: rate_limit

Steps to reproduce:
1. Opened UI
2. Entered "hello"
3. Set debug = rate_limit
4. Sent request

DevTools:

Request:

  "text": "hello",
  "debug": "rate_limit"


Response:


  "error": "Too many requests - rate limit exceeded (debug forced error)"


Status:
429 Too Many Requests

My analysis:
This error is intentionally triggered by the debug mode. In real systems, 429 usually means the user is hitting the API too fast or a retry loop or UI double-calls are happening.

Possible real causes:
- Customer script retrying too fast
- UI sending duplicate requests
- Missing delay/backoff
- Exceeded plan limit

Reply to customer:

429 means requests are arriving faster than allowed. Adding a delay (like 1 second) or exponential backoff usually fixes it. If you share the code that triggers the request, I can check for duplicates or loops.

Best regards,

Michael Rojas
Technical Support Engineer
The Saas Tech Support

📞 +1 (555) 123-4567
✉️ michael.rojas@thesaassupport.com
🌐 www.thesaassupport.com

Internal notes:
Helpful to include rate-limit response headers.
Check if related article is present in knowledge base. 

## Screenshots

- UI: `screenshots/T03-rate-limit/ui.png`
- Network: `screenshots/T01-invalid-api-key/network.png`
- Headers: `screenshots/T01-invalid-api-key/header.png`
- Payload: `screenshots/T01-invalid-api-key/payload.png`
- Response: `screenshots/T01-invalid-api-key/response.png`