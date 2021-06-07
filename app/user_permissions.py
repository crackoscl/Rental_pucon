def rol_usuario(user):
    if not user.is_superuser:
        return user


def is_trabajador(user):
    return user.is_trabajador
