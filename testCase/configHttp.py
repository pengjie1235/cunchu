import requests
import readConfig as readConfig
from common.Log import MyLog as Log
localReadConfig = readConfig.ReadConfig()
class ConfigHttp:
    def __init__(self):
        global host,port,timeout
        host = localReadConfig.get_http("baseurl")
        port = localReadConfig.get_http("port")
        timeout = localReadConfig.get_http("timeout")
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}
    def set_url(self,url):
        self.url = host + url
    def set_headers(self,header):
        self.headers = header
    def set_params(self,param):
        self.param= param
    def set_data(self,data):
        self.data = data
    def set_files(self,file):
        self.files =file

    #defined http get method
    def get(self):
        try:
            response = requests.get(self.url,params=self.params,headers=self.headers,timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.errer("Time out")
    def post(self):
        try:
            response = requests.post(self.url,headers=self.headers,data=self.data,files=self.files,timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.errer("Time out")
            return None
