def payload_create_booking():
    # In future you can replace this from the excel or JSON
    payload = {
        "firstname": "Pramod88",
        "lastname": "Dutta",
        "totalprice": 432,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2022-01-01",
            "checkout": "2022-01-01"
        },
        "additionalneeds": "Lunch"
    }
    return payload

def create_token():
    payload={
        "username": "admin",
        "password": "password123"
    }
    return payload

def updated_payload():
    payload1 ={
    "firstname" : "yyy",
    "lastname" : "Bryyyn",
    "totalprice" : 6666,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    }
    return payload1