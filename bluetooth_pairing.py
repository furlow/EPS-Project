#!/usr/bin/python

import gobject
import sys
import dbus
import dbus.service
import dbus.mainloop.glib
import threading

#The Agent class inherits the dbus.service.Object class
class Agent(dbus.service.Object):
	exit_on_release = True

	#Not sure how this works
	@dbus.service.method("org.bluez.Agent", in_signature="o", out_signature="s")
	#Overides the RequestPinCode function for the dbus.service.method, org.bluez.Agent
	def RequestPinCode(self, device):
		print "RequestPinCode (%s)" % (device)
		mainloop.quit()
		return '0000'

#The Bluetooth pairing class inherits the blue threading.Thread class
class bluetooth_pairing(threading.Thread):
	
	def __init__(self):
		
		threading.Thread.__init__(self)
		
		self.capability = "KeyboardDisplay"
		self.path = "/test/agent"
		dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
		self.bus = dbus.SystemBus()
		manager = dbus.Interface(self.bus.get_object("org.bluez", "/"), "org.bluez.Manager")
		adapther_path = manager.DefaultAdapter() #gets the path of the default bluetooth device
		self.adapter = dbus.Interface(self.bus.get_object("org.bluez", adapther_path), "org.bluez.Adapter")
		
	#This is run by using the start() function for an instance of bluetooth_pairing
	def run(self):
		
		agent = Agent(self.bus, self.path)

		self.mainloop = gobject.MainLoop()

		self.adapter.RegisterAgent(self.path, self.capability)
		print "Agent registered"

		self.mainloop.run()
		
	def quit(self):
		self.mainloop.quit()

