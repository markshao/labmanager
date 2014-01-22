__author__ = 'root'

user = {}

user['wsdl_url'] = 'https://chnservices-lm.dctmlabs.com/LabManager/SOAP/LabManagerinternal.asmx?WSDL'
user['username'] = 'shaom2'
user['password'] = ')Slamdunk1986'
user['organizationname'] = 'PF-QA-DFS'
user['workspacename'] = 'Main'

from labmanager.lmwsproxy import LMService

service = LMService(user)

# print service.get_configuration_id_by_name("pagrant")
# print service.get_network_id_by_name("PF-10.32.122.133-254:network")
print service.get_template_id_by_name("xmnTemplate")