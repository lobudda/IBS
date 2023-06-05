import requests
from UI_tests.locators.element_page_locators import PageLocators
from UI_tests.pages.base_page import BasePage


class GetSingleUser(BasePage):
    locators = PageLocators()

    def check_fields(self):
        self.element_is_present(self.locators.GET_SINGLE_USER).click()

        response_status = self.element_is_present((self.locators.GET_SINGLE_USER_STATUS)).text
        response_body = self.element_is_present((self.locators.GET_SINGLE_USER_RESPONSE_BODY)).text
        response_body = response_body.replace("\n", "")
        response_body = response_body.replace(' ', '')
        return response_status, response_body

    def api_response(self):
        response_api = requests.get("https://reqres.in/api/users/2")
        response_status_api = str(response_api.status_code)
        response_body_api = response_api.text
        response_body_api = response_body_api.replace(' ', '')
        return response_status_api, response_body_api

