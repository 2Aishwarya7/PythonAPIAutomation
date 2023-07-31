#Write all common verificationmethods like HTTP status code, validate json etc


#To verify the http code with any expected http code
def verify_http_status_code(response_data,expected_code):
    assert response_data.status_code == expected_code, "Expected HTTP Status : " + expected_code

#Verify any key shouldnot benull or zero
def verify_key_notnull_and_notequal_zero(key):
    assert key != 0, "Key is notempty: "+key
    assert key > 0, "Key should be greater than zero : " + key

