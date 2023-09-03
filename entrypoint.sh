python manage.py migrate
python manage.py collectstatic --no-input
python manage.py compress
gunicorn heidegger_landing.wsgi:application --bind 0.0.0.0:$1
