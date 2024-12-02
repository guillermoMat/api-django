from jwt import encode, decode


def create_token(data: dict):
    token = encode(payload=data, key="my_key", algorithm="HS256")
    return token


def validate_token(token: str):
    validate = decode(token, key="my_key", algorithms=["HS256"])
    return validate
