sudo cd /etc/sysconfig/network-scripts
sudo vi ifcfg-ens33

#In Each create above with below configs as per respective VMs

sudo systemctl restart NetworkManager

sudo reboot

##VM1
TYPE=Ethernet
BOOTPROTO=static
NAME=ens33
DEVICE=ens33
ONBOOT=yes
IPADDR=192.168.1.10
NETMASK=255.255.255.0
GATEWAY=192.168.1.1
DNS1=8.8.8.8


##VM2
TYPE=Ethernet
BOOTPROTO=static
NAME=ens33
DEVICE=ens33
ONBOOT=yes
IPADDR=192.168.1.11
NETMASK=255.255.255.0
GATEWAY=192.168.1.1
DNS1=8.8.8.8

##VM3
TYPE=Ethernet
BOOTPROTO=static
NAME=ens33
DEVICE=ens33
ONBOOT=yes
IPADDR=192.168.1.12
NETMASK=255.255.255.0
GATEWAY=192.168.1.1
DNS1=8.8.8.8


##VM_LB
TYPE=Ethernet
BOOTPROTO=static
NAME=ens33
DEVICE=ens33
ONBOOT=yes
IPADDR=192.168.1.13
NETMASK=255.255.255.0
GATEWAY=192.168.1.1
DNS1=8.8.8.8

ping 192.168.1.10-13 #from VM1
ping 192.168.1.11-13 #from VM2
ping 192.168.1.11-13 #from VM3
ping 192.168.1.11-13 #from VM4

##after this run following commands to install GIT and Python
sudo apt update 
sudo yum install git -y
sudo yum install python3 -y

#if yum doesnt work we can dnf also

pip3 install flask request threading time hashlib

cd .. #Go to root
mkdir VC_ASGN1
cd /VC_ASGN1
git clone https://github.com/rahulagarwal25/VC_Assignment_1.git

#Repeat above installation steps on each VM , then run python scripts of respective VM

python3 VM1.py
python3 VM2.py
python3 VM3.py
python3 VM4.py


#Create one test VM with above network config file chaing IP to 192.168.1.14 , run following curl commands

curl http://192.168.1.13:5000/mine_block #TO mine block , LB will direct the traffic to VM1

curl http://192.168.1.13:5000/get_chain #TO Get Chain , LB will direct the traffic to VM2

curl http://192.168.1.13:5000/get_block?index=1 #TO Get block Specify index number to get particular or leave it to get whole block, LB will direct the traffic to VM3
