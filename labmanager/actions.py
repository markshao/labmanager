__author__ = 'root'

from lmwsproxy import LMService
from util import read_dict_fd, write_json_fd


class LabManagerVmProvider(object):
    def __init__(self, provider_info, logger):
        self.provider_info = provider_info
        self.logger = logger

        self.service = LMService(self.provider_info, self.logger)
        self.default_template_name = self.provider_info['default_template_name']
        self.default_network_name = self.provider_info['default_network_name']
        self.machine_map = {}

    def create_machines(self, machine_settings):
        # we currently just support create the machines under an absolutely configuration
        self.configuration_name = self.provider_info['configuration']

        self.configuration_id = self.service.get_configuration_id_by_name(self.configuration_name)

        for machine_name, machine_setting in machine_settings.items():
            template_name = machine_setting.get("template_name", None)
            template_name = template_name if template_name else self.default_template_name

            network_name = machine_setting.get("network_name", None)
            network_name = network_name if network_name else self.default_network_name

            machine_desc = machine_setting.get("description", None)
            machine_desc = machine_desc if machine_desc else machine_name
            machine_id = self.service.machine_create_under_configuration(self.configuration_id, template_name,
                                                                         network_name, machine_name, machine_desc)
            self.logger.info("create the vm <%s> successfully" % machine_name)
            self.machine_map[machine_name] = machine_id

    def start_machines(self, machine_settings):
        self.service.configuration_deploy_by_id(self.configuration_id)
        self.logger.info("deploy the configuration **%s** successfully" % self.configuration_name)

    def stop_machines(self, machine_settings):
        self.service.configuration_undeploy_by_id(self.configuration_id)
        self.logger.info("undeploy the configuration **%s** successfully" % self.configuration_name)

    def destroy_machines(self, machine_settings):
        self.service.configuration_delete_by_id(self.configuration_id)
        self.logger.info("delete the configuration **%s** successfully" % self.configuration_name)

    def get_machine_ip(self, machine_setting):
        machine_id = self.machine_map[machine_setting['name']]
        return self.service.get_machine_ip(machine_id)

    def persistent_to_local(self, machine_settings, path):
        data = {"configuration_id": self.configuration_id}  # just write down the configuration id
        write_json_fd(data, path)


    def clean_from_persistent(self, path):
        res = read_dict_fd(path)
        self.configuration_id = res["configuration_id"]
        self.service.configuration_undeploy_by_id(self.configuration_id)
        self.service.configuration_delete_by_id(self.configuration_id)

        self.logger.info("clean the entire configuration@labmanager successfully")

