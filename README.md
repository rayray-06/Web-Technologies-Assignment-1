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
| Authentication method | `_____________'accept: application/json'__________________` |
| Required query parameters | `_____________lat: float, lon: float__________________` |
| Sample request with latitude/longitude | `____________`curl --request GET \___________________` |
| Sample JSON response (formatted example) |{
  "place_id": "116136978",
  "licence": "https://locationiq.com/attribution",
  "osm_type": "way",
  "osm_id": "34633854",
  "lat": "40.74844205",
  "lon": "-73.98565890160751",
  "display_name": "Empire State Building, 350, 5th Avenue, Manhattan Community Board 5, Manhattan, New York County, New York, New York, 10001, USA",
  "address": {
    "attraction": "Empire State Building",
    "house_number": "350",
    "road": "5th Avenue",
    "neighbourhood": "Manhattan Community Board 5",
    "suburb": "Manhattan",
    "county": "New York County",
    "city": "New York",
    "state": "New York",
    "postcode": "10001",
    "country": "United States of America",
    "country_code": "us"
  },
  "boundingbox": [
    "40.7479255",
    "40.7489585",
    "-73.9865012",
    "-73.9848166"
  ]
}
```
```
|
---
## 🚀 Section 4: Epoch to Human Time Conversion (Python time module) (2 marks)
| Criteria | Details |
|---------|---------|
| Library used | `_______________time________________` |
| Function used to convert epoch | `_____________time.time()__________________` |
| Sample code to convert timestamp |
import time
start = time.time()
print(f'Start time: {start}')
time.sleep(1)
end = time.time()
print(f'Elapsed: {end - start:.2f} seconds')
```
```
|
| Output (human-readable time) | `_____________| ____Start time: 1711891234.567890 Elapsed: 1.00 seconds_|__________________` |
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
