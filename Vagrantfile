# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = '2'

VMS = {
  :mongodb_mms_server_trusty => {
    :box => 'ubuntu/trusty64',
    :ext_port => 8080
  },
  :mongodb_mms_server_xenial => {
    :box => 'ubuntu/xenial64',
    :ext_port => 8081
  }
}

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  VMS.each_pair do |name, options|

    config.vm.define name do |vm_config|

      # Set proper box
      vm_config.vm.box = options[:box]
      vm_config.vm.network "forwarded_port", guest: 8080, host: options[:ext_port]


      # Virtualbox vm name management
      vm_config.vm.provider "virtualbox" do |vm|
          vm.name = name.to_s
          vm.memory = 15360
      end


      # Use trigger plugin to set environment variable used by Ansible
      # Needed with 2.0 home path change
      vm_config.vm.provision 'trigger' do |trigger|
        trigger.fire do
          ENV['ANSIBLE_ROLES_PATH'] = '../'
          ENV['ANSIBLE_ROLE_NAME'] = File.basename(Dir.getwd)
          ENV['VAGRANT'] = 'true'
        end
      end


      # Install python 2.7 if not present (On Xenial)
      vm_config.vm.provision 'shell' do |sh|
        sh.inline = '! type -P python2.7 \
                     && (sudo apt-get update \
                     && sudo apt-get install python2.7 -y) || true'
      end


      # Run Ansible provisioning
      vm_config.vm.provision 'ansible' do |ansible|
        ansible.playbook = 'testing_deployment.yml'
        # Enable requirement if role has dependencies
        ansible.galaxy_role_file = './requirements.yml'
        ansible.extra_vars = {
          ansible_python_interpreter: '/usr/bin/env python2.7'
        }
      end

    end
  end
end
