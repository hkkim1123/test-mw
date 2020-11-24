from configparser import ConfigParser

config = ConfigParser()
config.read('/home/rainus/config.ini')

DATABASE_URI = config.get('database', 'uri', fallback='localhost')


NOTIFICATION_SERVICE_PORT = 8080
NOTIFICATION_SERVICE_URL = ""

