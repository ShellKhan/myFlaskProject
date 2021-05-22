from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

report = Blueprint(
    name="report",
    import_name=__name__,
    static_folder="../static",
    url_prefix="/reports",
)
REPORTS = [
    {
        "id": 1,
        "title": "Доктор Ноу (1962)",
        "text": "some text",
        "author": {
            "name": "Иван",
            "id": 1,
        },
    },
    {
        "id": 2,
        "title": "Из России с любовью (1963)",
        "text": "some text",
        "author": {
            "name": "Михаил",
            "id": 4,
        },
    },
    {
        "id": 3,
        "title": "Голдфингер (1964)",
        "text": "some text",
        "author": {
            "name": "Петр",
            "id": 2,
        },
    },
    {
        "id": 4,
        "title": "Шаровая молния (1965)",
        "text": "some text",
        "author": {
            "name": "Семен",
            "id": 3,
        },
    },
    {
        "id": 5,
        "title": "Живёшь только дважды (1967)",
        "text": "some text",
        "author": {
            "name": "Андрей",
            "id": 5,
        },
    },
]


# роут по урлу "/reports/..."
@report.route("/")
def report_list():
    return render_template("reports/list.html", reports=REPORTS)


@report.route("/<int:report_id>/")
def report_details(report_id: int):
    for report in REPORTS:
        if report_id == report["id"]:
            this_report = report
            return render_template("reports/details.html", report=this_report)
    else:
        raise NotFound("Нет такого отчета!")
