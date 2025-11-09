###############################################################
# Space Bot Assignment 1
# This program connects to Webex, listens for "/seconds" messages,
# gets ISS location info and converts it to a readable address.
###############################################################

import requests
import json
import time
from iso3166 import countries  # added so I can use country names from country codes

# ask the user if they want to use their own token or the hard-coded one
choice = input("Do you wish to use the hard-coded Webex token? (y/n) ")

if choice == "n":
    # added this part to allow manual token input when testing
    InputToken = input("Enter your Webex access token: ")
    accessToken = "Bearer " + InputToken
else:
    # added my bot token here for quick testing (hard-coded)
    accessToken = "Bearer NzUyZDJlY2UtZTE2Ny00MDQ0LTliNDYtOTc2MWJkZTM1YjA2NDMzZmVmODMtNjQw_P0A1_636b97a0-b0af-4297-b0e7-480dd517b3f9"

# this connects to Webex and lists all my rooms
r = requests.get("https://webexapis.com/v1/rooms",
                 headers={"Authorization": accessToken})

if not r.status_code == 200:
    raise Exception("Incorrect reply from Webex API. Status code: {}. Text: {}".format(r.status_code, r.text))

# shows all available rooms in my account
print("\nList of available rooms:")
rooms = r.json()["items"]
for room in rooms:
    print("Type:", room["type"], "Title:", room["title"])

# loop to find the room name the user typed in
while True:
    roomNameToSearch = input("Which room should be monitored for the /seconds messages? ")
    roomIdToGetMessages = None

    for room in rooms:
        # added this part to match user input with the actual room name
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

# this keeps the bot running and checking for messages every second
while True:
    time.sleep(1)
    GetParameters = {
        "roomId": roomIdToGetMessages,
        "max": 1
    }

    # added this part to get the latest message from the chosen Webex room
    r = requests.get("https://webexapis.com/v1/messages",
                     params=GetParameters,
                     headers={"Authorization": accessToken})

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

    # added this part so the bot only reacts to messages that start with "/"
    if message.find("/") == 0:
        if message[1:].isdigit():
            seconds = int(message[1:])
        else:
            print("Input is invalid, try again")
            continue

        # I added this limit so the delay doesn't go over 5 seconds during testing
        if seconds > 5:
            seconds = 5

        time.sleep(seconds)

        # this gets the current ISS location from the ISS API
        r = requests.get("http://api.open-notify.org/iss-now.json")
        json_data = r.json()

        if r.status_code != 200:
            print("ISS data could not be retrieved")
            continue

        # added these lines to store latitude, longitude, and timestamp from the ISS data
        lat = json_data["iss_position"]["latitude"]
        lng = json_data["iss_position"]["longitude"]
        timestamp = json_data["timestamp"]

        # converts the time from numbers to readable date and time
        timeString = time.ctime(timestamp)

        # added my own LocationIQ API key here for the reverse geocode lookup
        mapsAPIGetParameters = {
            "key": "pk.cb8dfc0f12f34b86334407ab1c5306f9",
            "lat": lat,
            "lon": lng,
            "format": "json"
        }

        # this sends the ISS coordinates to the LocationIQ API
        r = requests.get("https://us1.locationiq.com/v1/reverse",
                         params=mapsAPIGetParameters)

        json_data = r.json()
        if r.status_code != 200:
            print("Location data could not be obtained")
            continue
        else:
            print("Location data obtained")

        # added this part to extract readable location info from the API response
        CountryResult = json_data["address"].get("country", "Unknown")
        StateResult = json_data["address"].get("state", "Unknown")
        CityResult = json_data["address"].get("city", "Unknown")
        StreetResult = json_data["address"].get("road", "Unknown")

        # converts the country code to full name using the iso3166 library
        if not CountryResult == "XZ":
            CountryResult = countries.get(CountryResult).name

        # added this message format so it looks nice when sent to Webex
        if CountryResult == "Unknown" and CityResult == "Unknown":
            responseMessage = "On {}, the ISS was flying over a body of water at latitude {}° and longitude {}°.".format(timeString, lat, lng)
        else:
            responseMessage = "On {}, the ISS was flying over {}, {}, {} ({}, {}).".format(timeString, CityResult, StateResult, CountryResult, lat, lng)

        print("Sending to Webex:", responseMessage)

        # added this part to send the final message back to the Webex room
        HTTPHeaders = {
            "Authorization": accessToken,
            "Content-Type": "application/json"
        }

        PostData = {
            "roomId": roomIdToGetMessages,
            "text": responseMessage
        }

        # this sends the formatted ISS location message to Webex
        r = requests.post("https://webexapis.com/v1/messages",
                          data=json.dumps(PostData),
                          headers=HTTPHeaders)

        if r.status_code != 200:
            print("Message could not be sent to Webex. Status code:", r.status_code)
        else:
            print("Message successfully sent to Webex.")
