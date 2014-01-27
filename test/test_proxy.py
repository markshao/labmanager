__author__ = 'root'

user = {}

user['wsdl_url'] = 'https://chnservices-lm.dctmlabs.com/LabManager/SOAP/LabManagerinternal.asmx?WSDL'
user['username'] = 'shaom2'
user['password'] = ')Slamdunk1986'
user['organizationname'] = 'PF-QA-DFS'
user['workspacename'] = 'Main'

import logging

from labmanager.lmwsproxy import LMService

logger = logging.getLogger()
service = LMService(user, logger)

# print service.get_configuration_id_by_name("pagrant")
# print service.get_network_id_by_name("PF-10.32.122.133-254:network")
service.configuration_undeploy_by_id(int(10313))