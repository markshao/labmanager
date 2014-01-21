__author__ = 'root'


class LabManagerVmProvider(object):
    def __init__(self, provider_info, logger):
        self.provider_info = provider_info
        self.logger = logger

    def create_machine(self, machine_setting):
        NotImplemented

    def start_machine(self, machine_setting):
        NotImplemented

    def stop_machine(self, machine_setting):
        NotImplemented

    def destroy_machine(self, machine_setting):
        NotImplemented

    def get_machine_ip(self, machine_setting):
        NotImplemented