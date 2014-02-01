#!/usr/bin/python

import gobject
import sys
import dbus
import dbus.service
import dbus.mainloop.glib

class Agent(dbus.service.Object):
	exit_on_release = True

	@dbus.service.method("org.bluez.Agent", in_signature="o", out_signature="s")
	def RequestPinCode(self, device):
		print "RequestPinCode (%s)" % (device)
		return '0000'

if __name__ == '__main__':
	dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
	
	bus = dbus.SystemBus()
	
	manager = dbus.Interface(bus.get_object("org.bluez", "/"), "org.bluez.Manager")
	
	capability = "KeyboardDisplay"

	path = manager.DefaultAdapter() #gets the path of the default bluetooth device

	adapter = dbus.Interface(bus.get_object("org.bluez", path), "org.bluez.Adapter")
	
	print adapter

	path = "/test/agent"
	
	agent = Agent(bus, path)

	print agent

	mainloop = gobject.MainLoop()

	adapter.RegisterAgent(path, capability)
	print "Agent registered"

	mainloop.run()
