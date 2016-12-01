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
        filename = '/tmp/mongodb-mms_3.4.0.383-1_x86_64.deb'

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


def test_configuration_files(SystemInfo, File):
    """
    Test if configuration settings added
    """

    config_file_path = ''

    if SystemInfo.distribution == 'ubuntu':
        config_file_path = '/opt/mongodb/mms/conf/conf-mms.properties'

    config_file = File(config_file_path)
    assert config_file.contains('mms.centralUrl=http://localhost:8080')
    assert config_file.contains('mms.fromEmailAddr=foo@bar.org')
    assert config_file.contains('mms.replyToEmailAddr=foo@bar.org')
    assert config_file.contains('mms.adminEmailAddr=foo@bar.org')
    assert config_file.contains('mms.emailDaoClass=com.xgen.svc.core.dao.email.JavaEmailDao')
    assert config_file.contains('mms.mail.transport=smtp')
    assert config_file.contains('mms.mail.hostname=localhost')
    assert config_file.contains('mms.mail.port=25')
