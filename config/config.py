import os
import configparser
from configparser import ConfigParser

configDir = os.path.dirname(__file__) # 获取当前文件所在的目录
print(configDir)
configFile = os.path.join(configDir, 'config.ini')

class MyParser(ConfigParser):
    def __init__(self):
        super().__init__()
    def as_dict(self):
        d = dict(self._sections)
        for k in d:
            d[k] = dict(d[k])
        return d

def get_all_conf(self):
        _config = MyParser()
        result = {}
        if os.path.isfile(configFile):
            try:
                _config.read(configFile, encoding='UTF-8')
                result = _config.as_dict()
            except OSError:
                raise ValueError("Read config file failed: %s" % OSError)
        return result
config = get_all_conf()
sys_config = config['sys']
smtp_config = config['smtp']