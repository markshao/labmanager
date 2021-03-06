LabManager
==========

This is the labmanger vmprovider plugin for the `Pagrant <https://github.com/markshao/pagrant>`_, it can
help you distribute your test cases to the labmanager support cloud platform. You just need to config the
Pagrantfile to use it

Install
-------------------------

.. code-block:: python

    pagrant vmprovider install labmanager [--index-url http://pypi.douban.com/simple]


Pagrantfile configuration
-------------------------


vmprovider
`````````````````````
.. code-block:: python

    def vmprovider():
        return {
            "type": "labmanager"
            # this is required to make pagrant detect that
            # you are using the labmanger plguin
        }



vmprovider config
````````````````````````````
.. code-block:: python

    def vmprovider_config():
        return {
            'wsdl_url': 'https://chnservices-lm.dctmlabs.com/LabManager/SOAP/LabManagerinternal.asmx?WSDL',
            'username': 'shaom2',
            'password': '**********',
            'organizationname': '************', # The organization name
            'workspacename': 'Main', # workspace name
            'default_template_name': 'xmnTemplate', # the template name displayed on the web portal
            'default_network_name': 'PF-10.32.122.133-254:network', # the network name displayed on the web portal
            'configuration': 'pagrant1', # all the machines will been created under it ,
                                         #  please create the new configuraion for the test

            'ssh_username': 'root', # default user for ssh
            'ssh_password': 'password', # default password for ssh
        }