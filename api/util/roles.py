from rest_api import config, app, logger

# Make the roles accessible as attributes
roles = []
fgids = []
try:
    globals()["DEFINITIONS"] = config.get("ROLES")
    for definition in globals()["DEFINITIONS"]:
        roles.append(definition["name"])
        globals()[definition["name"].upper()] = definition["name"]

        if "requirements" in definition:
            for requirement in definition["requirements"]:
                if "fgid" in requirement:
                    # Ensure fgid is a string padded by zeroes
                    requirement["fgid"] = f"{int(requirement['fgid']):05}"
                    fgids.append(requirement["fgid"])

except:
    logger.error()

globals()["ALL"] = roles
globals()["FGIDS"] = list(set(fgids))

expected_roles = ["Owner", "Developer", "Admin", "User", "Viewer"]

# Ensure that the expected roles (the core roles) are defined in the config file
for role in expected_roles:
    if role not in roles:
        raise Exception(
            'Invalid ROLES definition in API config file. Unable to find "'
            + role
            + '" which is a required role.'
        )

# If there is ever a drastic role change, we can override the role mapping in here
# EX: if we rename the Owner role to Epic_People, we could override with the following,
#
#     globals()["OWNER"] = "Epic_People"
#
