# 🚀 Space Bot API Investigation Sheet
**Total Marks: 30**
**Part 1: Collect Required API Documentation**
This investigation sheet helps you gather key technical information from the three
APIs required for the Space Bot project: **Webex Messaging API**, **ISS Current
Location API**, and a **Geocoding API** (LocationIQ or Mapbox or other), plus the
Python time module.
---
## Section 1: Webex Messaging API (7 marks)✅
| Criteria | Details |
|---------|---------|
| API Base URL | `____________[_Webex.com](https://webexapis.com/v1/room/tabs/{id} \)__________________` |
| Authentication Method | `_______________Authorization: Bearer ZTg1MDJiZTgtMjQ1NC00OGQzLWJjOTItOGZhYTdjNzM0OTc0ZWI3MmFhMmUtNGUx_P0A1_636b97a0-b0af-4297-b0e7-480dd517b3f9' \___Bearer_____________` |
| Endpoint to list rooms | `______________v1/room/tabs/{id}_________________` |
| Endpoint to get messages | `_________GET_______/v1/messages/{messageId} \______________` |
| Endpoint to send message | `_________POST_______/v1/messages \_______________` |
| Required headers | `______________--header 'Authorization: Bearer ZTg1MDJiZTgtMjQ1NC00OGQzLWJjOTItOGZhYTdjNzM0OTc0ZWI3MmFhMmUtNGUx_P0A1_636b97a0-b0af-4297-b0e7-480dd517b3f9' \
--header 'Accept: application/json'_________________` |
| Sample full GET or POST request | `___________curl -L --request GET \
--url https://webexapis.com/v1/room/tabs/{id} \
--header 'Authorization: Bearer ZTg1MDJiZTgtMjQ1NC00OGQzLWJjOTItOGZhYTdjNzM0OTc0ZWI3MmFhMmUtNGUx_P0A1_636b97a0-b0af-4297-b0e7-480dd517b3f9' \
--header 'Accept: application/json'____________________` |
---
## Section 2: ISS Current Location API (3 marks)
| Criteria | Details |
|---------|---------|
| API Base URL | `_________________  $.getJSON('http://api.open-notify.org/iss-now.json?callback=?______________` |
| Endpoint for current ISS location | `________________/iss-now.json_______________` |
| Sample response format (example JSON) |
```
```
|
---
## Section 3: Geocoding API (LocationIQ or Mapbox or other) (6 marks)
| Criteria | Details |
|---------|---------|
| Provider used (circle one) | **LocationIQ \
| API Base URL | `_____________https://us1.locationiq.com/v1/reverse__________________` |
| Endpoint for reverse geocoding | `__________v1/reverse \_____________________` |
| Authentication method | `_______________________________` |
| Required query parameters | `_______________________________` |
| Sample request with latitude/longitude | `_______________________________` |
| Sample JSON response (formatted example) |
```
```
|
---
## 🚀 Section 4: Epoch to Human Time Conversion (Python time module) (2 marks)
| Criteria | Details |
|---------|---------|
| Library used | `_______________________________` |
| Function used to convert epoch | `_______________________________` |
| Sample code to convert timestamp |
```
```
|
| Output (human-readable time) | `_______________________________` |
---
## 🚀 Section 5: Web Architecture & MVC Design Pattern (12 marks)
### 🚀 Web Architecture – Client-Server Model
- **Client**:
- **Server**:
- (Explain the communication between them & include a block diagram )
### 🚀 RESTful API Usage
-
-
-
### 🚀 MVC Pattern in Space Bot
| Component | Description |
|------------|-------------|
| **Model** | |
| **View** | |
| **Controller** | |
#### Example:
- Model:
- View:
- Controller:
---
### 🚀 Notes
- Use official documentation for accuracy (e.g. developer.webex.com, locationiq.com
or Mapbox, open-notify.org or other ISS API).
- Be prepared to explain your findings to your instructor or demo how you retrieved
them using tools like Postman, Curl, or Python scripts.
---
### Total: /30
