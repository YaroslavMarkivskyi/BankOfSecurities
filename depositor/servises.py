import secrets

from django.contrib.auth.hashers import make_password


def generate_password(length=12):
    password = secrets.token_urlsafe(length)
    print(password)
    hashed_password = make_password(password)
    return hashed_password
