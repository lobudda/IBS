GET_SINGLE_USER = {
    'type': 'object',
    'properties': {
        "data": {
                "id": {'type': 'number'},
                "email": {'type': "string"},
                "first_name": {'type': "string"},
                "last_name": {'type': "string"},
                "avatar": {'type': "string"}
            },
         "support": {
                "url": {'type': "string"},
                "text": {'type': "string"}
            }

    },
    'required': ['data', 'support']
}
