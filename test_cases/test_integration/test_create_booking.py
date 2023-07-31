'''
Author-Aishwarya
Objective-Tets the create boockingAPI
TC1-Verify the status code,header
TC2-Verify the booking ID
TC3-Verify JSON schema
'''
import pytest

from src.constants.apiconstants import url_create_booking
from src.helpers.api_wrapper import post_request
from src.helpers.common_verifications import *
from src.helpers.payload_manager import payload_create_booking
from src.helpers.utils import common_headers

class TestIntegration(object):

    @pytest.fixture(scope="module")
    def setup(self):
        print("Before")

    def test_create_booking_tc1(self):
        response = post_request(url_create_booking(), headers=common_headers(), auth=None,
                                payload=payload_create_booking(), in_json=False)
        verify_http_status_code(response, 200)
        verify_key_notnull_and_notequal_zero(response.json()["bookingid"])

    # URL -> Separate URLpytest
    # Payload - Separate Payload manager
    # Headers -> Headers Utils
    # Verify - Seperate Verify

    @pytest.fixture(scope="module")
    def tear_down(self):
        print("End")