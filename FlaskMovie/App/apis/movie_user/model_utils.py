from App.models.movie_user import AdminUser


def get_movie_user(user_ident):
    if not user_ident:
        return None
    user = AdminUser.query.get(user_ident)

    if user:
        return user
    user = AdminUser.query.filter(AdminUser.phone == user_ident).first()

    if user:
        return user

    user = AdminUser.query.filter(AdminUser.username == user_ident).first()
    if user:
        return user
    return None