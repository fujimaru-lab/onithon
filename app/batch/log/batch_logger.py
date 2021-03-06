import logging
import sys
import string
from conf import onithon_config


class BatchLog:
    '''
    onithonバッチ用ログクラス
    '''
    # 標準出力、ファイル出力のログフォーマット
    batchlog_fmt = '%(asctime)s [%(levelname)s] - %(message)s'
    # '%(asctime)s - %(funcName)s [%(levelname)s]:%(message)s - %(filename)s:(%lineno)d'

    def __init__(self, file_nm):
        config = onithon_config.OnithonConfig()

        # ロガーの取得
        self._logger = logging.getLogger(file_nm)
        # 最低ログレベルの設定
        self._logger.setLevel(config.getvalue("logger config", "LEVEL"))
        
        # コーンソールハンドラーの生成
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(config.getvalue('logger config', 'LEVEL'))
        c_fmt = logging.Formatter(self.batchlog_fmt)
        ch.setFormatter(c_fmt)

        # ファイルハンドラーの生成
        fh = logging.FileHandler(config.getvalue('logger config', 'LOG_FILE'), encoding='utf-8')
        fh.setLevel(config.getvalue('logger config', 'LEVEL'))
        f_fmt = logging.Formatter(self.batchlog_fmt)
        fh.setFormatter((f_fmt))

        # ハンドラーの設定
        self._logger.addHandler(ch)
        self._logger.addHandler(fh)


    def debug(self, msg, *params):
        _msg = self.create_msg(msg, *params)
        self._logger.debug(_msg)

    def info(self, msg, *params):
        _msg = self.create_msg(msg, *params)
        self._logger.info(_msg)

    def warning(self, msg, *params):
        _msg = self.create_msg(msg, *params)
        self._logger.warning(_msg)

    def error(self, msg, *params):
        _msg = self.create_msg(msg, *params)
        self._logger.error(_msg)

    def critical(self, msg, *params):
        _msg = self.create_msg(msg, *params)
        self._logger.critical(_msg)

    def shutdown(self):
        logging.shutdown()

    def create_msg(self, template, *params):
        fmt = string.Formatter()
        return fmt.vformat(template, params, None)
