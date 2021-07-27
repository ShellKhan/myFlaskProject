web: gunicorn wsgi:app
init: flask db init && flask db migrate && flask db upgrade
upgrade: flask db migrate && flask db upgrade