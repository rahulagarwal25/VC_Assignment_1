sudo /etc/sysconfig/network-scripts
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
IPADDR=192.168.1.14
NETMASK=255.255.255.0
GATEWAY=192.168.1.1
DNS1=8.8.8.8


##after this run following commands to install GIT and Python
sudo apt update 
sudo yum install git -y
sudo yum install python3 -y

#if yum doesnt work we can dnf also

pip3 install flask request threading time hashlib