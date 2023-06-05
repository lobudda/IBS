import requests

import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from src.schema.schema_get_single_user import GET_SINGLE_USER
from src.base_classes.response import Response


def test_getting_single_user():
    r = requests.get(url='https://reqres.in/api/users/2')
    response = Response(r)

    response.assert_status_code(200).validate(GET_SINGLE_USER)


