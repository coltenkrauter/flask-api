#@auth.roles_required([roles.OWNER, roles.ADMIN, roles.DEVELOPER, roles.USER])
def get():
    return {'hello':'world'}, 200
