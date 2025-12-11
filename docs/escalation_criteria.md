
# Escalation Criteria

Support Engineers must know when an issue can be solved independently and when it must be escalated to engineering or SRE. This guide provides clear criteria, structure, and examples for proper escalations.

---

## 1. When to escalate an issue

You should escalate when **any** of the following apply:

### **1. Widespread impact**
- Multiple users reporting the same issue  
- High volume of failures in logs  
- Outage patterns or sudden spikes

### **2. High business impact**
- Critical workflows failing (payments, login, core API endpoints)  
- Production systems degraded  
- Urgent customer deadlines blocked

### **3. Data integrity concerns**
- Inconsistent data returned  
- Missing or corrupted fields  
- Duplicate or unexpected records

### **4. Security-related symptoms**
- Access level issues  
- Permission leaks  
- Unexpected access to private data

### **5. Reproducible server-side errors**
- You tested the request in Postman  
- Payload is correct  
- Headers are correct  
- You still receive persistent 5xx errors

### **6. Customer tier**
- Strategic or high-value customers are affected in any way

---

## 2. What to include in an escalation

Engineering needs **short, clear, complete** information.

Provide:

### **A. Summary (2–3 sentences)**
Describe what is happening and who is affected.

### **B. Reproduction steps**
- Endpoint  
- Method  
- Payload  
- Headers  
- Whether the issue reproduces in Postman

### **C. Scope**
Include:
- Affected customers  
- Regions  
- Frequency  
- Time range  

### **D. Evidence**
Useful evidence includes:
- Logs  
- Request IDs (if available)  
- Screenshots from DevTools or Postman  
- Error examples  
- Timestamps  

### **E. Impact**
Explain what breaks for the customer.

---

## 3. Example escalation (lab context)

**Subject:** Persistent 500 Internal Server Error on `/api/process`  
**Summary:** API responses intermittently return 500 errors even with valid payloads. The issue is reproducible in Postman and Python scripts, so it is not client-side.  
**Scope:** Occurs on every request using the payload `{ "text": "test", "debug": "server_error" }`.  
**Steps to Reproduce:**
1. POST `http://localhost:3000/api/process`  
2. Body: `{ "text": "test", "debug": "server_error" }`  
3. Response: `500 Internal Server Error`

**Evidence:**  
- DevTools screenshots included  
- Logs show repeated 500s between 14:05–14:20 UTC  
- Affects test user accounts across local environment

**Expected:**  
- Should return `200 OK` or a documented `4xx` error

**Impact:**  
- Cannot complete basic API testing flows  

### Result:  
Issue escalated to engineering with complete context.

---

## 4. How to explain escalation to a customer

A simple Support Engineer explanation:

> “I’ve reproduced the issue, collected the details, and escalated it to our engineering team. They’ll be able to investigate the server-side behavior further. I will update you as soon as I hear back.”

Clear, calm, and professional.
```
