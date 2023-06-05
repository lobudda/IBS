from jsonschema import validate

import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from src.enums.global_enums import GlobalErrorMessages


class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code
    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                validate(item, schema)
        else:
            validate(self.response_json, schema)

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessages.ERROR_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorMessages.ERROR_STATUS_CODE.value
        return self



