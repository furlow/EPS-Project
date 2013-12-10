#!/usr/bin/python

import gobject
import sys
import dbus
import dbus.service
import dbus.mainloop.glib
import threading

class Agent(dbus.service.Object):
	exit_on_release = True

	@dbus.service.method("org.bluez.Agent", in_signature="o", out_signature="s")
	def RequestPinCode(self, device):
		print "RequestPinCode (%s)" % (device)
		return '0000'

class bluetooth_pairing(threading.Thread):
	
	def __init__(self):
		
		threading.Thread.__init__(self)
		self.capability = "KeyboardDisplay"
		self.path = "/test/agent"
		dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
		self.bus = dbus.SystemBus()
		manager = dbus.Interface(self.bus.get_object("org.bluez", "/"), "org.bluez.Manager")
		path = manager.DefaultAdapter() #gets the path of the default bluetooth device
		self.adapter = dbus.Interface(self.bus.get_object("org.bluez", path), "org.bluez.Adapter")
		
	def run(self):
		
		agent = Agent(self.bus, self.path)

		mainloop = gobject.MainLoop()

		self.adapter.RegisterAgent(self.path, self.capability)
		print "Agent registered"

		mainloop.run()
