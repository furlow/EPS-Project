#!/usr/bin/python

import gobject
import sys
import dbus
import dbus.service
import dbus.mainloop.glib
import threading
from time import sleep

gobject.threads_init()
<<<<<<< HEAD

=======
>>>>>>> c03bd31b6bae5aa62bd66006cb7ab5c318d1e899

# The Agent class inherits the dbus.service.Object class, it uses the default
# initialiser of the parent class dbus.service object
class Agent(dbus.service.Object):
    exit_on_release = True
    
    # Initalize the class and base class
    def __init__(self, bus, path):
        dbus.service.Object.__init__(self, bus, path)
    
    # This exports a dbus service method using the @dbus.service.method
    # decorator, which essential lets us define what happens
    # when this signal is called for the RequestPinCode function.
    @dbus.service.method("org.bluez.Agent", in_signature="o", out_signature="s")
    def RequestPinCode(self, device):
        print "RequestPinCode (%s)" % (device)
        return '0000' #Set this to what ever value you want the pincode to be

def create_device_reply(device):
    print "New device (%s)" % (device)
    mainloop.quit()

def create_device_error(error):
    print "Creating device failed: %s" % (error)


#The Bluetooth pairing class inherits the blue threading. Thread class
class bluetooth_pairing(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
<<<<<<< HEAD
=======
	self.mainloop = gobject.MainLoop()

>>>>>>> c03bd31b6bae5aa62bd66006cb7ab5c318d1e899
    
    #This is run by using the start() function for an instance of bluetooth_pairing
    def run(self):

        self.capability = "KeyboardDisplay"
        self.path = "/test/agent"

        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        self.bus = dbus.SystemBus()
        manager = dbus.Interface(self.bus.get_object("org.bluez", "/"), "org.bluez.Manager")

        adapther_path = manager.DefaultAdapter() #gets the path of the default bluetooth device
        self.adapter = dbus.Interface(self.bus.get_object("org.bluez", adapther_path), "org.bluez.Adapter")
<<<<<<< HEAD

        #mainloop = gobject.MainLoop()
        agent = Agent(self.bus, self.path)

        self.adapter.Discoverable = True
        self.adapter.RegisterAgent(self.path,
                           self.capability)
                           
        print "Ready to pair"
            while True:
                sleep(1)
=======

        agent = Agent(self.bus, self.path)

        self.adapter.Discoverable = True
        self.adapter.RegisterAgent(self.path,
                           self.capability)
                           
        print "Ready to pair"
        self.mainloop.run()

    def stop(self):
	self.mainloop.quit()
	print "Exited pairing mode"
>>>>>>> c03bd31b6bae5aa62bd66006cb7ab5c318d1e899

# Need to come up with a way in which the mainloop will quit, using the Thread quit method is okay.
# However We can run the thread when the button is pressed down for 3 seconds. When a succesfull pair
# is made, find out what org.bluez.agent method will be called when a succesfull pair has been created
# we can then call quit() to quit the main loop and thus quit the thread.
<<<<<<< HEAD
pair = bluetooth_pairing()
pair.start()
=======
>>>>>>> c03bd31b6bae5aa62bd66006cb7ab5c318d1e899
