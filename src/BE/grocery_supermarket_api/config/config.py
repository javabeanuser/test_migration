import configparser
config = configparser.ConfigParser()
conf = config.read('app.properties')
if conf.__len__() == 0:
    config.read('./../app.properties')

class Config:

    @staticmethod
    def get_database_url():
        return config['DATABASE']['url']

    @staticmethod
    def get_log_format():
        return config['LOG']['format']

    @staticmethod
    def get_log_datefmt():
        return config['LOG']['datefmt']

    @staticmethod
    def get_log_level():
        return config['LOG']['level']

    @staticmethod
    def get_log_file():
        return config['LOG']['file']

    @staticmethod
    def get_log_max_bytes():
        return int(config['LOG']['maxBytes'])

    @staticmethod
    def get_log_backup_count():
        return int(config['LOG']['backupCount'])