#!/usr/bin/env python

import RPi.GPIO as GPIO 
from alarmmodules import *
from bluetooth_module import *
from time import sleep
from threading import Timer
from bluetooth_pairing_module import bluetooth_pairing

BUTTON_IN_PIN = 22
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON_IN_PIN, GPIO.IN)

try:

        list = [0,0,0,0]
	#list = [513,513,1,0]
	
	#Start the pairing thread
	#pairing = bluetooth_pairing()

	#Start the bluetooth communications thread
        blue_comms = bluetooth_comms(list)
        blue_comms.daemon = True
        blue_comms.start()

        print "In Main ", list

        alarm1 = alarm(list)
	totalsecs=0

	print "Current totalsecs is 0"

        while 1:
                sleep(0.1)
                print "In Main ", list

		#if(pairing.isAlive()):
		#	print "Pairing Live"


                if(list[2] == 1):
                        totalsecs = alarm1.comparetime()
                        print "Totalsecs in main is", totalsecs
                        t = Timer ( totalsecs, alarm1.alarmon )
			t.daemon = True
                        print "Turning alarm on"
                        t.start()                                                      #function to turn on alarm
			list[2] = 0

                #if(list[3] == 1):
                #        alarm1.lighton()

                #if(list[3] == 0):
                #        alarm1.lightoff()
                
		button_value = GPIO.input(BUTTON_IN_PIN)          #if button is pressed
 		print "Button Value is ", button_value

		if(button_value == 1 and button_value_previous == 0):
			print "The Button was pressed"
                        if(list[3] == 0):
				print "Turning Light on"
				alarm1.lighton()
                                list[3] = 1        #then turn off light
                        else:
				print "Turning Light off"         #but if light is off
				alarm1.lightoff()
                                list[3] = 0     #then turn on light
		button_value_previous = button_value
                
except KeyboardInterrupt:
        blue_comms.stop()
        alarm1.close()
        raise
