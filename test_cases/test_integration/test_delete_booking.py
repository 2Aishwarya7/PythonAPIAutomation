import pytest
from src.constants.apiconstants import *
from src.helpers.api_wrapper import *
from src.helpers.common_verifications import *
from src.helpers.payload_manager import *
from src.helpers.utils import common_headers,common_put_patch_headers

class TestIntegration(object):

    @pytest.fixture()
    def test_create_token2(self):
        response=post_request(url_create_token(), headers=common_headers(), payload=create_token(),in_json=False,auth=None)
        return response.json()["token"]

    @pytest.fixture()
    def test_booking(self):
        response=post_request(url=url_create_booking(), auth=None, payload=payload_create_booking(), headers=common_headers(),in_json=False)
        return response.json()["bookingid"]

    def test_update_booking2(self,test_booking,test_create_token2):
        response=put_request(url=url_update_delete_booking(str(test_booking)), auth=None,payload=updated_payload(), headers=common_put_patch_headers(str(test_create_token2)),in_json=False)
        verify_http_status_code(response,200)

    def test_delete_booking(self, test_booking,test_create_token2):
        token= "token="+test_create_token2
        headers={"Content-Type": "application/json",
               "Cookie":token}
        response=delete_data(url_update_delete_booking(str(test_booking)),auth=None,headers=headers, in_json=False)
        verify_http_status_code(response, 201)

