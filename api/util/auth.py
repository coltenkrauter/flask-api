from flask import request, jsonify
import jwt

def token_info(apikey, required_scopes=None):
    """
    This function is needed for the python connexion 
    lib and is referenced from the swagger spec.
    """

    return {
      "username": "jdoe",
      "fullname": "John Doe",
      "email": "email@example.com",
      "iat": 1579635983,
      "exp": 1580865513,
      "iss": "CK-Apps"
    }


#def validate_token():
#    if request.method == "OPTIONS":
#        return "OPTIONS"
#
#    if "Authorization" not in request.headers:
#        return "No Authorization header."
#
#    bearer_token = request.headers["Authorization"]
#    if bearer_token[:7] != "Bearer ":
#        return "Not a bearer token."
#
#    error, token = decode_and_verify(bearer_token[7:])
#    if error is not None:
#        return error
#
#    # Think of this as returning no errors
#    return None
#
#
## Verify the authenticity of the token with the public key
#def decode_and_verify(bearer_token):
#    error = None
#    decoded_jwt = None
#
#    try:
#        # Attempt to verify and decode the token
#        decoded_jwt = jwt.decode(
#            bearer_token,
#            config.get("AUTH_VERIFY_KEY"),
#            issuer=config.get("AUTH_ISSUER"),
#            algorithms=[config.get("AUTH_ALGORITHM")],
#        )
#
#    except jwt.ExpiredSignatureError:
#        # Token exp timestamp is in the past
#        error = "Token is expired."
#    except jwt.InvalidIssuerError:
#        # Issuer does not match
#        error = "Invalid token issuer."
#    except jwt.InvalidIssuedAtError:
#        # When the iat claim is in the future
#        error = "Invalid token issue time."
#    except jwt.MissingRequiredClaimError:
#        # ISS, IAT, EXP, all required
#        error = "Token missing required claims."
#    except jwt.InvalidTokenError:
#        # Base exception when decode() fails on a token
#        error = "Invalid token."
#
#    # If error is None, the decoded_jwt is valid
#    return error, decoded_jwt
