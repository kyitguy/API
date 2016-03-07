# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/trusty64"

  # Expose on the network
  config.vm.hostname = "drchrono.local"
  config.vm.network "forwarded_port", guest: 5000, host: 5000
  #config.vm.network "public_network", ip: "192.168.1.17"
  
  # Mount the current folder in the home directory
  #config.vm.synced_folder ".", "/home/vagrant/drchrono"

  # Stolen from:
  # https://github.com/DSpace/vagrant-dspace/blob/master/Vagrantfile#L146 Turn
  # on SSH forwarding (so that 'vagrant ssh' has access to your local SSH keys,
  # and you can use your local SSH keys to access GitHub, etc.)
  config.ssh.forward_agent = true
  
  # provision the rest with ansible
  config.vm.provision "ansible" do |ansible|
    ansible.verbose = "v"
    ansible.playbook = "playbook.yml"
  end

  config.vm.provider "virtualbox" do |v|
    v.name = "drchronodev"
    v.memory = 1024
    v.cpus = 2
  end

end
