EPS-Project
===========

EPS Project code for raspberry pi and android app

This project has two code sections. The service which runs on the raspberry pi and a project that runs on an android phone.

Installation of code onto raspberry pi
======================================

To install you will first need to install bluez and python-bluetooth (py-bluez) packages

	sudo apt-get install bluez python-bluetooth python-gobject

To install the natures alarm program;

	sudo python install.py

Checking the service is running
===============================

In terminal type;

	service natures-alarm status

Starting and stopping the service
=================================

To stop use;

	sudo service natures-alarm stop

To start use;

	sudo service natures-alarm start


alex chu
