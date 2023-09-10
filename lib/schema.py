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

