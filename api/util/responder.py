# Table lookups for the json error blobs and the HTTP status codes
# fmt: off
error =  {
    0:   {"message": "Success!", "HTTP_code": 200},
    1:   {"message": "Resource successfully created!", "HTTP_code": 201},
    32:  {"message": "Could not authenticate you.", "HTTP_code": 401},
    33:  {"message": "Could not authorize", "HTTP_code": 401},
    34:  {"message": "Sorry, that resource does not exist.", "HTTP_code": 404},
    35:  {"message": "The payload is invalid or not formatted correctly.", "HTTP_code": 400},
    36:  {"message": "Forbidden", "HTTP_code": 403},
    130: {"message": "Internal database error.", "HTTP_code": 500},
    131: {"message": "Internal error.", "HTTP_code": 500},
    132: {"message": "External error.", "HTTP_code": 500},
}
# fmt: on

# Provides a nice single line function call for api response objects
def pack(code, description=None, response=None):
    blob = {"code": code}
    if code in error:
        if response != None:
            blob = response
        else:
            blob["message"] = error[code]["message"]
            if description != None:
                blob["description"] = str(description)
        return blob, error[code]["HTTP_code"]
    else:
        blob["message"] = "Undefined error code!"
    # return 500 (Internal server error) for undefined error codes
    return blob, 500


if __name__ == "__main__":
    # for testing the error code lookups
    for code in error:
        print(code, "-", error[code]["message"], ":", error[code]["HTTP_code"])

    # Testing the single-line implementation
    print()
    print(pack(35, "extra info for code 35, here!"))
    print(pack(321312, description="here!"))
    print(pack(0, response="Custom response!"))
    print(pack(131))
