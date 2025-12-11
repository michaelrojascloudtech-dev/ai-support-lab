
# Escalation Guidelines for Support Engineers

Not every issue requires engineering involvement.  
Escalations should be meaningful, reproducible, and well-documented.

---

## When You SHOULD Escalate

- Issue is reproducible with valid requests  
- Multiple customers report same backend failure  
- Logs show internal server errors (500/503/504)  
- Latency spikes across regions  
- Rate limits not matching customer plan  
- Security concerns  
- Customer provides clear reproduction steps  

---

## When You SHOULD NOT Escalate

- Customer JSON is invalid  
- Missing or incorrect API key  
- CORS from browser calls  
- Customer exceeding rate limits  
- Payload too large (already documented)  

---

## What to Include in Escalation

- Customer/project ID  
- Exact request + headers  
- Screenshots  
- Logs or timestamps  
- Reproduction steps  
- Expected vs actual result  

---

## Goal of Escalation

Help engineering identify the issue **without repeating support’s investigation**.

---
