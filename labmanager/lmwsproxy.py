__author__ = 'root'

WSDL = 'wsdl_url'
USERNAME = 'username'
PASSWORD = 'password'
ORGANIZATION = 'organizationname'
WORKSPACE = 'workspacename'

AUTHENTICATION_HEADER = 'AuthenticationHeader'

from suds.client import Client
from suds import WebFault


TIMEOUT = 60 * 60 * 5


class LMService(object):
    network_cache = {}
    template_cache = {}

    def __init__(self, provider_info, logger):

        self.provider_info = provider_info

        self.proxy = Client(provider_info[WSDL])
        self.proxy.set_options(timeout=TIMEOUT)

        authenticationHeader = self.proxy.factory.create(AUTHENTICATION_HEADER)
        authenticationHeader[USERNAME] = self.provider_info[USERNAME]
        authenticationHeader[PASSWORD] = self.provider_info[PASSWORD]
        authenticationHeader[ORGANIZATION] = self.provider_info[ORGANIZATION]
        authenticationHeader[WORKSPACE] = self.provider_info[WORKSPACE]

        self.proxy.set_options(soapheaders=authenticationHeader)

        self.soapIP_mode = self.proxy.factory.create("SOAPIPMode")

        self.logger = logger

    def get_configuration_id_by_name(self, configuration_name):
        try:
            configuration = self.proxy.service.GetSingleConfigurationByName(configuration_name)
            raise Exception("The configuration %s existed,please create a new one\n" % configuration_name)
        except WebFault:
            # if the configuratoin not found , create the new one
            configuration_id = self.proxy.service.ConfigurationCreateEx(configuration_name, configuration_name)
            self.logger.info("create the configuration **%s**" % configuration_name)
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

    def get_template_id_by_name(self, template_name):

        # xmnTemplate
        if template_name in self.__class__.template_cache:
            return self.__class__.template_cache[template_name]
        else:
            template_list = self.proxy.service.ListTemplates().Template
            for template in template_list:
                if template_name == template.name:
                    self.__class__.template_cache[template_name] = template.id
                    return template.id

    def get_machine_info_by_id(self, machine_id):
        try:
            return self.proxy.service.GetMachine(machine_id)
        except WebFault:
            return None

    def get_machine_network_info_by_id(self, machine_id):
        try:
            return self.proxy.GetNetworkInfo(machine_id)
        except WebFault:
            return None

    def configuration_deploy_by_id(self, configuration_id):
        # fenceMode = 1 Not fenced
        # fenceMode = 2 Fenced Block In And Out
        # fenceMode = 3 Fenced Allow Out Only
        # fenceMode = 4 Fenced Allow In Only
        self.proxy.service.ConfigurationDeploy(configuration_id, False, 1)


    def configuration_undeploy_by_id(self, configuration_id):
        self.proxy.service.ConfigurationUndeploy(configuration_id)

    def configuration_delete_by_id(self, configuration_id):
        self.proxy.service.ConfigurationDelete(configuration_id)

    def machine_create_under_configuration(self, configuration_id, template_name, network_name, machine_name,
                                           machine_description):

        netinfo = self.proxy.factory.create("NetInfo")
        newArrayofNetInfo = self.proxy.factory.create("ArrayOfNetInfo")
        newArrayofNetInfo.NetInfo.append(netinfo)

        template_id = self.get_template_id_by_name(template_name) # get the template id

        new_machine_id = self.proxy.service.ConfigurationAddMachineEx(configuration_id, template_id, machine_name,
                                                                      machine_description,
                                                                      0, 0,
                                                                      newArrayofNetInfo)
        network_id = self.get_network_id_by_name(network_name) # get the network id

        self.proxy.service.NetworkInterfaceCreate(new_machine_id, network_id, self.soapIP_mode.STATIC_AUTOMATIC)

        return new_machine_id

    def machine_delete(self, machine_id):
        self.proxy.service.MachineDelete(machine_id)

    def get_machine_ip(self, machine_id):
        result = self.proxy.service.GetNetworkInfo(machine_id)
        network_infos = result.NetInfo
        return network_infos[0].ipAddress

