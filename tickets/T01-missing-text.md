Ticket: 400 Missing Text Field

Customer message:
The customer says they keep getting:
 "error": "Missing 'text' field in body" 

Environment checked:
- Firefox
- AI Support Lab (local)
- POST /api/process
- Debug flag used: missing_text

Steps to reproduce:
1. Opened the UI
2. Left the text field empty
3. Entered debug = missing_text
4. Sent the request

What I saw in DevTools:
Request body:

  "debug": "missing_text"


Response:

  "error": "Missing 'text' field in body (debug forced error)"


Status:
400 Bad Request

My analysis:

The backend intentionally returns this 400 error when the "missing_text" debug flag is used. In real situations, this error normally happens when the customer forgets to include the required "text" field or uses the wrong key name.

Possible real causes:
- Missing "text" in payload
- Wrong key (ex: "message")
- Missing application/json header

Reply to customer:

Hi Dear Customer, 

The 400 error usually means the "text" field wasn't included in the request. Make sure the body includes:
{ "text": "hello" }
If you send me your request (remove sensitive info), I can confirm.

Best regards,

Michael Rojas
Technical Support Engineer
The Saas Tech Support

📞 +1 (555) 123-4567
✉️ michael.rojas@thesaassupport.com
🌐 www.thesaassupport.com

Internal notes:
Docs should show a required fields list.
Check if related article is present in knowledge base

## Screenshots

- UI: `screenshots/T01-missing-text/ui.png`
- Network: `screenshots/TT01-missing-text/network.png`
- Headers: `screenshots/T01-missing-text/header.png`
- Payload: `screenshots/T01-missing-text/payload.png`
- Response: `screenshots/T01-missing-text/response.png`

