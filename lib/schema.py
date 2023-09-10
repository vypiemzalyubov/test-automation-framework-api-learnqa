schema_register_user = {
    "type": "object",
    "properties": {
        "id": {"type": "string"}
    },
    "required": ["id"]
}

schema_auth_user = {
    "type": "object",
    "properties": {
        "user_id": {"type": "integer"}
    },
    "required": ["user_id"]
}

schema_user_info = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "firstName": {"type": "string"},
        "lastName": {"type": "string"}
    },
    "required": ["id", "username", "email", "firstName", "lastName"]
}