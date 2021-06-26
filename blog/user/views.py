from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

user = Blueprint(
    name="user",
    import_name=__name__,
    static_folder="../static",
    url_prefix="/users",
)

USERS = {
    1: "Иван",
    2: "Петр",
    3: "Семен",
    4: "Михаил",
    5: "Андрей",
}


# роуты по урлам "/users/..."
@user.route("/")
def user_list():
    return render_template("users/list.html", users=USERS)


@user.route("/<int:user_id>/")
def user_details(user_id: int):
    try:
        user_name = USERS[user_id]
    except KeyError:
        raise NotFound("Нет такого юзера!")
    return render_template("users/details.html", user_id=user_id, user_name=user_name)
