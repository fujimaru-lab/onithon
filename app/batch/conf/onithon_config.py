# encoding utf-8
import configparser
import os


class OnithonConfig:
    '''
    Onithonバッチ用設定ファイル読み込みクラス
    onithon_config.iniより設定値を読み込み返す
    '''
    def __init__(self):
        dir_path = os.path.dirname(__file__)
        self._conf_file = dir_path + '/onithon_config.ini'
        self._config = configparser.ConfigParser()
        self._config.read(self._conf_file)

    def getvalue(self, key1, key2):
        self._config.read(self._conf_file)
        value = self._config[key1][key2]
        return value
