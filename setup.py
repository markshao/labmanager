__author__ = 'root'

from setuptools import setup, find_packages

__version__ = "1.0.1"

setup(
    name="labmanager",
    version=__version__,
    packages=find_packages(),
    description='the labmanager cloud plugin for pagrant',
    classifiers=[
        "Programming Language :: Python",
    ],
    platforms='any',
    keywords='framework testing',
    entry_points={
        'PAGRANT': [
            "VMPROVIDER=labmanager.actions:LabManagerVmProvider",
            "VMPROVIDER_INFO=labmanager:get_provider_info"
        ]
    }
)