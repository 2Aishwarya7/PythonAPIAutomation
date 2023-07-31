import pytest
from src.constants.apiconstants import *
from src.helpers.api_wrapper import post_request,put_request, get_request
from src.helpers.common_verifications import *
from src.helpers.payload_manager import *
from src.helpers.utils import common_headers,common_put_patch_headers


class TestIntegration(object):

    @pytest.fixture()
    def test_create_token1(self):
        response=post_request(url_create_token(), auth=None,payload=create_token(),in_json=False, headers=common_headers())
        print(response.json()["token"])
        return response.json()["token"]

    @pytest.fixture()
    def test_create_booking1(self):
        response = post_request(url=url_create_booking(), auth=None, headers=common_headers(),
                                payload=payload_create_booking(), in_json=False)
        return response.json()["bookingid"]

    def test_update(self,test_create_booking1, test_create_token1):
        response=put_request(url=url_update_delete_booking(str(test_create_booking1)), auth=None, headers=common_put_patch_headers(str(test_create_token1)), payload=updated_payload(),in_json=False)
        verify_http_status_code(response,200)


    @pytest.fixture(scope="module")
    def down(self):
        print("end")



