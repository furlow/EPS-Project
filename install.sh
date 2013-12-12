#!/bin/sh

#File names and directories
install_dir='/opt/EPS-Project/'
LSB_Script='natures-alarm'
main_prog='natures-alarm.py'
init_dir='/etc/init.d/'

#This needs to be run as root

#Attempt to install dependencies for natures-alarm

apt-get install bluez python-bluetooth gobject

#copy the files to installation directories
echo "Creating installation directories"
mkdir $install_dir

echo "Copying files"
cp src/* $install_dir
cp init/* $init_dir

echo "Setting file permissions"
chmod +x $init_dir/$LSB_Script
chmod +x $install_dir/$main_prog

update-rc.d $LSB_Script defaults

echo "Installation Complete"

echo "Natures-alarm will auto start on reboot"
echo "To Start now type 'sudo service natures-alarm start' in terminal"
