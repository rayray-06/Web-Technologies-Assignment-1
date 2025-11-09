###############################################################
#This is just a starter code for the assignment 1,
# you need to follow the assignment brief to complete all the tasks required by the
#assessment brief
#
# This program:
# - Asks the user to enter an access token or use the hard coded access token.
# - Lists the user's Webex rooms.
# - Asks the user which Webex room to monitor for "/seconds" of requests.
# - Monitors the selected Webex Team room every second for "/seconds" messages.
# - Discovers GPS coordinates of the ISS flyover using ISS API.
# - Display the geographical location using geolocation API based on the GPS coordinates.
# - Formats and sends the results back to the Webex Team room.
###############################################################

# 1. Import libraries for API requests, JSON formatting, epoch time conversion, and iso3166.
import requests
import json
import time
from iso3166 import countries

# 2. Complete the if statement to ask the user for the Webex access token.
choice = input("Do you wish to use the hard-coded Webex token? (y/n) ")

if choice == "n":
    InputToken = input("Enter your Webex access token: ")
    accessToken = "Bearer " + InputToken
else:
    accessToken = "Bearer YOUR_WEBEX_TOKEN_HERE"

# 3. Provide the URL to the Webex room API.
r = requests.get("https://webexapis.com/v1/rooms",
                 headers={"Authorization": accessToken})

###################################################################################
# DO NOT EDIT ANY BLOCKS WITH r.status_code
if not r.status_code == 200:
    raise Exception("Incorrect reply from Webex API. Status code: {}. Text: {}".format(r.status_code, r.text))
###################################################################################

# 4. Create a loop to print the type and title of each room.
print("\nList of available rooms:")
rooms = r.json()["items"]
for room in rooms:
    print("Type:", room["type"], "Title:", room["title"])

###################################################################################
# SEARCH FOR WEBEX ROOM TO MONITOR
###################################################################################
while True:
    roomNameToSearch = input("Which room should be monitored for the /seconds messages? ")
    roomIdToGetMessages = None

    for room in rooms:
        if room["title"].find(roomNameToSearch) != -1:
            print("Found rooms with the word " + roomNameToSearch)
            print(room["title"])
            roomIdToGetMessages = room["id"]
            roomTitleToGetMessages = room["title"]
            print("Found room: " + roomTitleToGetMessages)
            break

    if roomIdToGetMessages is None:
        print("Sorry, I didn't find any room with " + roomNameToSearch + " in it.")
        print("Please try again...")
    else:
        break

###################################################################################
# WEBEX BOT CODE
###################################################################################
while True:
    time.sleep(1)
    GetParameters = {
        "roomId": roomIdToGetMessages,
        "max": 1
    }

    # 5. Provide the URL to the Webex messages API.
    r = requests.get("https://webexapis.com/v1/messages",
                     params=GetParameters,
                     headers={"Authorization": accessToken})

    # verify if the returned HTTP status code is 200/OK
    if not r.status_code == 200:
        print("Incorrect reply from Webex API. Status code:", r.status_code)
        print("Text:", r.text)
        continue

    json_data = r.json()
    if len(json_data["items"]) == 0:
        print("No messages in room")
        continue

    messages = json_data["items"]
    message = messages[0]["text"]
    print("Message received:", message)

    if message.find("/") == 0:
        if message[1:].isdigit():
            seconds = int(message[1:])
        else:
            print("Input is invalid, try again")
            continue

        # for the sake of testing, the max number of seconds is set to 5.
        if seconds > 5:
            seconds = 5

        time.sleep(seconds)

        # 6. Provide the URL to the ISS Current Location API.
        r = requests.get("http://api.open-notify.org/iss-now.json")
        json_data = r.json()

        if r.status_code != 200:
            print("ISS data could not be retrieved")
            continue

        # 7. Record the ISS GPS coordinates and timestamp.
        lat = json_data["iss_position"]["latitude"]
        lng = json_data["iss_position"]["longitude"]
        timestamp = json_data["timestamp"]

        # 8. Convert the timestamp epoch value to a human readable date and time.
        timeString = time.ctime(timestamp)

        # 9. Provide your Geolocation API consumer key.
        mapsAPIGetParameters = {
            "key": "YOUR_LOCATIONIQ_API_KEY",
            "lat": lat,
            "lon": lng,
            "format": "json"
        }

        # 10. Provide the URL to the Reverse GeoCode API.
        r = requests.get("https://us1.locationiq.com/v1/reverse",
                         params=mapsAPIGetParameters)

        # Verify if the returned JSON data from the API service are OK
        json_data = r.json()
        if r.status_code != 200:
            print("Location data could not be obtained")
            continue
        else:
            print("Location data obtained")

        # 11. Store the location received from the API in required variables
        CountryResult = json_data["address"].get("country", "Unknown")
        StateResult = json_data["address"].get("state", "Unknown")
        CityResult = json_data["address"].get("city", "Unknown")
        StreetResult = json_data["address"].get("road", "Unknown")

        #Find the country name using ISO3166 country code
        if not CountryResult == "XZ":
            CountryResult = countries.get(CountryResult).name

        # 12. Complete the code to format the response message.
        if CountryResult == "Unknown" and CityResult == "Unknown":
            responseMessage = "On {}, the ISS was flying over a body of water at latitude {}° and longitude {}°.".format(timeString, lat, lng)
        else:
            responseMessage = "On {}, the ISS was flying over {}, {}, {} ({}, {}).".format(timeString, CityResult, StateResult, CountryResult, lat, lng)

        print("Sending to Webex:", responseMessage)

        # 13. Complete the code to post the message to the Webex room.
        HTTPHeaders = {
            "Authorization": accessToken,
            "Content-Type": "application/json"
        }

        PostData = {
            "roomId": roomIdToGetMessages,
            "text": responseMessage
        }

        r = requests.post("https://webexapis.com/v1/messages",
                          data=json.dumps(PostData),
                          headers=HTTPHeaders)

        if r.status_code != 200:
            print("Message could not be sent to Webex. Status code:", r.status_code)
        else:
            print("Message successfully sent to Webex.")
