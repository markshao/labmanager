__author__ = 'root'

WSDL = 'wsdl_url'
USERNAME = 'username'
PASSWORD = 'password'
ORGANIZATION = 'organizationname'
WORKSPACE = 'workspacename'

AUTHENTICATION_HEADER = 'AuthenticationHeader'

from suds.client import Client
from suds import WebFault


class LMService(object):
    network_cache = {}

    def __init__(self, provider_info):
        self.provider_info = provider_info

        self.proxy = Client(provider_info[WSDL])

        authenticationHeader = self.proxy.factory.create(AUTHENTICATION_HEADER)
        authenticationHeader[USERNAME] = self.provider_info[USERNAME]
        authenticationHeader[PASSWORD] = self.provider_info[PASSWORD]
        authenticationHeader[ORGANIZATION] = self.provider_info[ORGANIZATION]
        authenticationHeader[WORKSPACE] = self.provider_info[WORKSPACE]

        self.proxy.set_options(soapheaders=authenticationHeader)

        self.soapIP_mode = self.proxy.factory.create("SOAPIPMode")

    def get_configuration_id_by_name(self, configuration_name):
        try:
            configuration = self.proxy.service.GetSingleConfigurationByName(configuration_name)
            return configuration.id
        except WebFault:
            # if the configuratoin not found , create the new one
            configuration_id = self.proxy.service.ConfigurationCreateEx(configuration_name, configuration_name)
            return configuration_id

    def get_network_id_by_name(self, network_name):

        # PF-10.37.10.5-254:network
        if network_name in self.__class__.network_cache:
            return self.__class__.network_cache[network_name]
        else:
            network_list = self.proxy.service.ListNetworks().Network
            for network in network_list:
                if network_name == network.Name:
                    self.__class__.network_cache[network_name] = network.NetID
                    return network.NetID
