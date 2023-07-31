# Help you to read the json files and provide you the JSON data
import json
from src.helpers.api_wrapper import post_request

def get_payload_auth():
    # Read from the auth.json and return json
    file_data = open("src/resources/outh.json")
    data = json.loads(file_data)
    file_data.close()
    return str(data)


def common_headers():
    headers = {
        "Content-Type": "application/json",
    }
    return headers

def common_put_patch_headers(bookingId):
    headers= {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie":"token="+bookingId
    }
    return headers

# Read from the Excel and Run a Test case Multiple Times
# Data driven -

# Read data from Excel and Run the API - 100 Times