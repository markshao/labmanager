__author__ = 'root'

WSDL = 'wsdl_url'
USERNAME = 'username'
PASSWORD = 'password'
ORGNIZATIOn = 'orgnization'
WORKSPACE = 'workspace'



class LMService(object):
    def __init__(self, provider_info):
        self.provider_info = provider_info