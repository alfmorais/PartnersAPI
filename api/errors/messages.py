JWT_REVOKED_TOKEN_CALLBACK = {
    "description": "The token has been revoked.",
    "error": "token_revoked",
}

JWT_TOKEN_NOT_FRESH_CALLBACK = {
    "message": "The token is not fresh.",
    "error": "fresh_token_required.",
}

JWT_EXPIRED_TOKEN_CALLBACK = {
    "message": "The token has expired.",
    "error": "token_expired",
}

JWT_INVALID_TOKEN_CALLBACK = {
    "message": "Signature verification failed.",
    "error": "invalid_token",
}

JWT_MISSING_TOKEN_CALLBACK = {
    "description": "Request does not contain an access token.",
    "error": "authorization_required",
}