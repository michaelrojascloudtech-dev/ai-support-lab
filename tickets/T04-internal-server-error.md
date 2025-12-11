Ticket: 500 Internal Server Error

Customer message:
Customer says they get a 500 error even with simple input.

Environment checked:
- Firefox
- AI Support Lab (local)
- POST /api/process
- Debug flag: server_error

Steps to reproduce:
1. Opened UI
2. Entered "hello"
3. Set debug = server_error
4. Sent request

DevTools:

Request:

  "text": "hello",
  "debug": "server_error"


Response:

  "error": "Internal server error (debug forced error)"


Status:
500 Internal Server Error

My analysis:
The backend forces a 500 error for simulation. In real-world APIs, a 500 usually means an unhandled exception, missing variable, dependency failure, database timeout, or a bad deployment.

Possible real causes:
- Backend crash
- Unhandled exception
- Downstream service failure
- Missing environment variable
- Server overload

Reply to customer:

A 500 error means the server had an unexpected issue. This usually resolves quickly. If it continues, share the timestamp and request body (remove sensitive data) and we can check logs.

Best regards,

Michael Rojas
Technical Support Engineer
The Saas Tech Support

📞 +1 (555) 123-4567
✉️ michael.rojas@thesaassupport.com
🌐 www.thesaassupport.com

Internal notes:
Would be good to add correlation IDs so errors can be traced.
Check if related article is present in knowledge base. 

## Screenshots

- UI: `screenshots/T03-rate-limit/ui.png`
- Network: `screenshots/T01-invalid-api-key/network.png`
- Headers: `screenshots/T01-invalid-api-key/header.png`
- Payload: `screenshots/T01-invalid-api-key/payload.png`
- Response: `screenshots/T01-invalid-api-key/response.png`