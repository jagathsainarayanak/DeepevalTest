import configparser

class Config_read():
    def read_conf():
        config = configparser.ConfigParser()
        config.read('/Users/jagathsa.kakaraparty/Documents/DeepEvalTest/utilities/endpoints.properties')
        return config
    
