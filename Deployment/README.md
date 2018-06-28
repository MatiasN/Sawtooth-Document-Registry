# Demo Steps

## Deploy, Provision and Start Nodes

Vagrant up

Vagrant ssh vm1/2/3

vm1 - sudo docker-compose -f Genesis_Node.yml up
vm2 & 3 - sudo docker-compose -f Secondary_Node.yml up

## Test by Submiting Transactions

Vagrant ssh vm2 and vm3

vm2 - intkey set -url http://10.0.1.10:8008 MyKey 999

vm3 - intkey show -url http://10.0.1.11:8008 MyKey 

Verify Outputs and Validator Logs


# Information to Deploy Directly on Ubuntu without Docker
sudo chmod 777 /var/lib/sawtooth
sudo chmod 777 /var/lib/sawtooth/poet*

https://www.howtoforge.com/tutorial/how-to-create-docker-images-with-dockerfile/

https://sawtooth.hyperledger.org/docs/core/nightly/master/app_developers_guide/ubuntu.html

https://sawtooth.hyperledger.org/docs/core/nightly/master/app_developers_guide/creating_sawtooth_network.html#ubuntu-add-a-node-to-the-single-node-environment

https://docs.ansible.com/ansible/2.5/user_guide/playbooks_intro.html