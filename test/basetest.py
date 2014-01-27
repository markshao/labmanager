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
# print soapIP_mode

netinfo = client.factory.create("NetInfo")
# netinfo.networkId = network_ID
# netinfo.resetMac = True
# netinfo.vmxSlot = 1
# netinfo.nicId = 1
# netinfo.isConnected = True
# netinfo.ipAddressingMode = soapIP_mode.STATIC_AUTOMATIC

newArrayofNetInfo = client.factory.create("ArrayOfNetInfo")
newArrayofNetInfo.NetInfo.append(netinfo)

tangram_id = 8441
lxc_id = 22395
git_lab_ci_ruunner = 22005
#
import suds
#
try:
    print client.service.GetConfigurationByName("pagrant1")
    # result = client.service.GetNetworkInfo(22395)
    # print (result.NetInfo)[0].ipAddress
except suds.WebFault,e:
    print e
# print client.service.GetNetworkInfo(23275)
# print client.service.GetMachine(23275)
# #
# machine_id = client.service.ConfigurationAddMachineEx(configuration_ID, template_ID, "testaaa", "testaaa", 0, 0,
#                                                       newArrayofNetInfo)
#
# print machine_id
#
# print client.service.NetworkInterfaceCreate(machine_id, network_ID, soapIP_mode.STATIC_AUTOMATIC)