Ticket: 401 Invalid or Missing API Key

Customer message:
Customer reports they get 401 errors even though they added their API key.

Environment checked:
- Firefox
- AI Support Lab (local)
- POST /api/process
- Debug flag: invalid_api_key

Steps to reproduce:
1. Opened the UI
2. Entered any text
3. Set debug = invalid_api_key
4. Sent the request

DevTools:

Request body:

  "text": "test",
  "debug": "invalid_api_key"


Response:

  "error": "Invalid or missing API key (debug forced error)"


Status:
401 Unauthorized

My analysis:
The backend purposely returns 401 when the debug flag is invalid_api_key. In real cases, 401 usually means the Authorization header was missing or formatted incorrectly (missing "Bearer", expired key, wrong key, frontend stripped headers, etc.).

Possible real causes:
- Missing Authorization header
- Missing "Bearer" prefix
- Expired key
- Wrong environment key

Reply to customer:

401 means the API key wasn't accepted. Make sure you include:
Authorization: Bearer YOUR_API_KEY
If you send me a redacted version of your request headers, I can look.

Best regards,

Michael Rojas
Technical Support Engineer
The Saas Tech Support

📞 +1 (555) 123-4567
✉️ michael.rojas@thesaassupport.com
🌐 www.thesaassupport.com

Internal notes:
We should add a clearer "authentication examples" section.
Check if related article is present in knowledge base.

## Screenshots

- UI: `screenshots/T02-invalid-api-key/ui.png`
- Network: `screenshots/T01-invalid-api-key/network.png`
- Headers: `screenshots/T01-invalid-api-key/header.png`
- Payload: `screenshots/T01-invalid-api-key/payload.png`
- Response: `screenshots/T01-invalid-api-key/response.png`
