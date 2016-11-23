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
