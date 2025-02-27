import jwt


key = "secret"

print(
    jwt.encode(
        payload={
            "name": "nikita"
        },
        key=key,
        algorithm="HS256"
    )
)