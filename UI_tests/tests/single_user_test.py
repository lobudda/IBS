import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from UI_tests.pages.single_user_page import GetSingleUser

class TestSingleUser:

        def test_user(self, driver):
            single_user_page = GetSingleUser(driver, 'https://reqres.in/')
            single_user_page.open_url()
            single_user_page.check_fields()
            output_data = single_user_page.check_fields()
            output_data_api = single_user_page.api_response()
            assert output_data == output_data_api





