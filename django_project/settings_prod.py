SECRET_KEY = config['SECRET_KEY']

with open('/etc/config.json') as config_file:
    config = json.load(config_file)

EMAIL_HOST_USER = config.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = config.get('EMAIL_PASS')

