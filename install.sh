!#/bin/sh

#This needs to be run as root

#copy the files to installation directories
echo "Creating Directories\n"
mkdir /opt/EPS-Project/
echo "Copying files\n"
cp src/* /opt/EPS-project/
cp init.d/ /etc/init.d/

update-d.rc natures-alarm.sh defaults

echo "Installation Complete"

echo "Natures-alarm will auto start on reboot"
echo "To Start now type "sudo service natures-alarm start" in terminal"
