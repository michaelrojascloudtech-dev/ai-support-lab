 
Ticket: 422 Unprocessable Entity (Invalid or Unprocessable Input)

Customer message:

Customer reports they are receiving a 422 Unprocessable Entity error when calling the API. They mention the server “understands the request but can’t process it.”

Environment checked:

- Chrome
- AI Support Lab (local)
- Endpoint: POST /api/process
- Debug flag used: unprocessable_entity

Steps to Reproduce

- Open the UI at http://localhost:3000/
- Enter any text (e.g., "hello")
- Set Debug Flag = unprocessable_entity
- Click Send

The UI returns a 422 Unprocessable Entity response immediately

What I saw in DevTools

Request payload:
{
  "text": "hello",
  "debug": "unprocessable_entity"
}

Response:
{
  "error": "Unprocessable Entity: The server understands the content type but was unable to process the contained instructions (debug forced error)"
}

Status:
422 Unprocessable Entity

The Network tab shows correct request body and endpoint, and the debug flag properly triggers the 422 response.

My analysis

A 422 Unprocessable Entity error means:

- The server received the request
- The server understood the structure
- But the content itself is invalid or cannot be processed

It is different from:

- 400 Bad Request → malformed JSON, missing fields
- 500 Internal Error → backend failure
- 409 Conflict → version/state conflict

422 specifically means:

“Your input is well-formed, but logically invalid.”

Common real-world examples:

- Invalid values (e.g., date in the past when only future dates allowed)
- Wrong data types (string where number expected)
- Violating validation rules
- Unsupported operations
- Required nested fields missing
- Incorrect format (e.g., invalid email pattern)

In this lab, the behavior is expected because the debug flag triggers the validation failure.

Reply to customer

The 422 Unprocessable Entity error means the server received your request and understood its format, but the content didn’t meet the required validation rules. This typically happens when a field has the wrong type or contains data that the endpoint cannot process.

Please review the data you’re sending and confirm:

- All fields meet the required validation rules
- Any dates, IDs, or formats follow the correct structure
- No invalid or unsupported values are included

If you can share a sanitized example of the payload (removing sensitive data), I can check it and confirm which field is causing the validation issue.

—
Michael Rojas
Technical Support Engineer
The SaaS Tech Support
📞 +1 (555) 123-4567
✉️ michael.rojas@thesaassupport.com

Internal notes 

Expected debug behavior. In real cases, 422 happens when input passes JSON parsing but fails deeper validation rules. Useful to suggest updating validation guidelines in KB for common fields customers struggle with.

## Screenshots

- UI: `screenshots/T10-unprocessable-entity/ui.png`
- Network: `screenshots/T10-unprocessable-entity/network.png`
- Headers: `screenshots/T10-unprocessable-entity/headers.png`
- Payload: `screenshots/T10-unprocessable-entity/payload.png`
- Response: `screenshots/T10-unprocessable-entity/response.png`
