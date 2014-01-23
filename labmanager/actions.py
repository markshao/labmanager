__author__ = 'root'

from lmwsproxy import LMService


class LabManagerVmProvider(object):
    def __init__(self, provider_info, logger):
        self.provider_info = provider_info
        self.logger = logger

        self.service = LMService(self.provider_info)
        self.default_template_name = self.provider_info['default_template_name']
        self.default_network_name = self.provider_info['default_network_name']
        self.machine_map = {}

    def create_machines(self, machine_settings):
        # we currently just support create the machines under an absolutely configuration
        configuration_name = self.provider_info['configuration']

        self.configuration_id = self.service.get_configuration_id_by_name(configuration_name)

        for machine_name, machine_setting in machine_settings.items():
            template_name = machine_setting.get("template_name", None)
            template_name = template_name if template_name else self.default_template_name

            network_name = machine_setting.get("network_name", None)
            network_name = network_name if network_name else self.default_network_name

            machine_desc = machine_setting.get("description", None)
            machine_desc = machine_desc if machine_desc else machine_name
            machine_id = self.service.machine_create_under_configuration(self.configuration_id, template_name,
                                                                         network_name, machine_name, machine_desc)

            self.machine_map[machine_name] = machine_id

    def start_machines(self, machine_settings):
        self.service.configuration_deploy_by_id(self.configuration_id)

    def stop_machines(self, machine_settings):
        self.service.configuration_undeploy_by_id(self.configuration_id)

    def destroy_machines(self, machine_settings):
        self.service.configuration_delete_by_id(self.configuration_id)

    def get_machine_ip(self, machine_setting):
        machine_id = self.machine_map[machine_setting['name']]
        return self.service.get_machine_ip(machine_id)
