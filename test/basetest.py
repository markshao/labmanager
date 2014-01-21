__author__ = 'root'

from suds.client import Client

client = Client("https://chnservices-lm.dctmlabs.com/LabManager/SOAP/LabManagerinternal.asmx?WSDL")

user = client.factory.create("AuthenticationHeader")

user['username'] = 'shaom2'
user['password'] = ')Slamdunk1986'
user['organizationname'] = 'PF-QA-DFS'
user['workspacename'] = 'Main'

client.set_options(soapheaders=user)

configuration_ID = 10221
template_ID = 12643
network_ID = 71

soapIP_mode = client.factory.create("SOAPIPMode")
print soapIP_mode

netinfo = client.factory.create("NetInfo")
netinfo.networkId = network_ID
netinfo.resetMac = True
netinfo.vmxSlot = 0
netinfo.nicId = 0
netinfo.isConnected = True
netinfo.ipAddressingMode = soapIP_mode.STATIC_AUTOMATIC

newArrayofNetInfo = client.factory.create("ArrayOfNetInfo")
newArrayofNetInfo.NetInfo.append(netinfo)

print newArrayofNetInfo

print client.service.ConfigurationAddMachineEx(configuration_ID, template_ID, "test_aaa", "test_aaa", 0, 0,
                                               newArrayofNetInfo)

