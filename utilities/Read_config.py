import configparser

class Config_read():
    def read_conf():
        config = configparser.ConfigParser()
        config.read('utilities/endpoints.properties')
        return config
    
