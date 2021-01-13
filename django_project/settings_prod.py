import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://266e48c56b1a408f8e2da432b3e56262@o504307.ingest.sentry.io/5590940",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True
)

SECRET_KEY = config['SECRET_KEY']

with open('/etc/config.json') as config_file:
    config = json.load(config_file)

EMAIL_HOST_USER = config.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = config.get('EMAIL_PASS')

