from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

person = Blueprint(
    name="person",
    import_name=__name__,
    static_folder="../static",
    url_prefix="/persons",
)

PERSONS = {
    1: "Иван",
    2: "Петр",
    3: "Семен",
    4: "Михаил",
    5: "Андрей",
}


@person.route("/")
def person_list():
    return render_template("persons/list.html", persons=PERSONS)


@person.route("/<int:person_id>/")
def person_details(person_id: int):
    try:
        person_name = PERSONS[person_id]
    except KeyError:
        raise NotFound("Нет такого человека!")
    return render_template("persons/details.html", person_id=person_id, person_name=person_name)
