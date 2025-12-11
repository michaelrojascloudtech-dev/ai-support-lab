 
 Ticket: 403 Forbidden (Unauthorized Action)

Customer message:
Customer says they are getting a 403 forbidden error when calling the endpoint.

Environment checked:
- Firefox
- AI Support Lab (local)
- POST /api/process
- Debug flag used: forbidden

Steps to reproduce:
1. Opened the UI
2. Entered basic text (ex: "hello")
3. Set debug = forbidden
4. Sent request
5. The UI returned a 403 error immediately

What I saw in DevTools:

Request body:

  "text": "hello",
  "debug": "forbidden"


Response:

  "error": "Forbidden: you do not have permission to perform this action (debug forced error)"


Status:
403 Forbidden

My analysis:

The backend intentionally returns a 403 when the debug flag "forbidden" is used. In real API systems, 403 usually means authentication succeeded (the key is valid), but the user is not allowed to perform the requested action. This can happen due to missing permissions, wrong API plan, blocked feature, or a role that doesn’t have access.

Possible real causes:
- API key is valid but doesn’t have permission for this specific operation
- Customer is using a free tier key to call a premium endpoint
- Workspace/organization settings blocking access
- User role (ex: viewer instead of editor)
- Regional restrictions

Reply to customer:

A 403 error usually means the API key is valid but does not have permission for the requested operation. Check if the key has the right role or access level for this endpoint. If you share which key or project you’re using (remove sensitive data), I can verify permissions.

Michael Rojas
Technical Support Engineer
The Saas Tech Support

📞 +1 (555) 123-4567
✉️ michael.rojas@thesaassupport.com
🌐 www.thesaassupport.com

Internal notes:
We should document which endpoints require elevated permissions or plan upgrades.
Check if related article is present in knowledge base. 


## Screenshots

- UI: `screenshots/T05-forbidden/ui.png`
- Network: `screenshots/T05-forbidden/network.png`
- Headers: `screenshots/T05-forbidden/headers.png`
- Payload: `screenshots/T05-forbidden/payload.png`
- Response: `screenshots/T05-forbidden/response.png`
