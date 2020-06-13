# encoding utf-8
import  configparser

class OnithonConfig:
    def __init__(self):
        self._config = configparser.ConfigParser()
        self._config.read('onithon_config.ini')

    def getvalue(self, key1, key2):
        value = self._config[key1][key2]
        return value
    