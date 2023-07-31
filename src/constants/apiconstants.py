#Add your constants

def url_base():
    #In future if we update env this will help
    return "https://restful-booker.herokuapp.com"

def url_create_token():
    return "https://restful-booker.herokuapp.com/auth"

def url_create_booking():
    return "https://restful-booker.herokuapp.com/booking"

def url_update_delete_booking(booking_id):
    return "https://restful-booker.herokuapp.com/booking/" + booking_id