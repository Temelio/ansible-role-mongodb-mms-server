"""
Role tests
"""
import pytest

# To run all the tests on given docker images:
pytestmark = pytest.mark.docker_images(
    'infopen/ubuntu-trusty-ssh:0.1.0',
    'infopen/ubuntu-xenial-ssh-py27:0.2.0'
)


def test_temporary_package_file(SystemInfo, File):
    """
    Test downloaded package from URL
    """

    if SystemInfo.distribution == 'ubuntu':
        filename = '/tmp/mongodb-mms_2.0.7.372-1_x86_64.deb'

    package = File(filename)
    assert package.exists
    assert package.is_file


def test_package_install(SystemInfo, Package):
    """
    Test if package is installed
    """

    if SystemInfo.distribution == 'ubuntu':
        package_name = 'mongodb-mms'

    package = Package(package_name)
    assert package.is_installed


def test_configuration_files(SystemInfo, File):
    """
    Test if configuration files exists
    """

    config_files = []

    if SystemInfo.distribution == 'ubuntu':
        config_files = [
            '/opt/mongodb/mms/conf/mms.conf',
            '/opt/mongodb/mms/conf/conf-mms.properties',
        ]

    for config_file in config_files:
        assert File(config_file).exists
        assert File(config_file).is_file
        assert File(config_file).user == 'root'
        assert File(config_file).group == 'root'
        assert File(config_file).mode == 0o664
