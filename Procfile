release: python manage.py migrate
web: NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program gunicorn democloud.wsgi --log-file -