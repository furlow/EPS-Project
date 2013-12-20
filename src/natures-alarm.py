#!/usr/bin/python

import RPi.GPIO as GPIO 
from alarmmodules import *
from bluetooth_module import *
from time import sleep
from threading import Timer
from bluetooth_pairing_module import bluetooth_pairing

LED_OUT_PIN = 13
BUTTON_IN_PIN = 22



try:

        list = [0,0,0,0]
	
	#Start the pairing thread
	pairing = bluetooth_pairing()

	#Start the bluetooth communications thread
        blue_comms = bluetooth_comms(list)
        blue_comms.daemon = True
        blue_comms.start()

        print "In Main ", list

        alarm1 = alarm(list, BUTTON_IN_PIN, LED_OUT_PIN)
	totalsecs=0

	print "Current totalsecs is 0"

        while 1:
                sleep(0.1)
                print "In Main ", list

		if(pairing.isAlive()):
			print "Pairing Live"


                if(list[2] == 1):
                        totalsecs = alarm1.comparetime()
                        print "Totalsecs in main is", totalsecs
                        t= Timer ( int(totalsecs), alarm1.alarmon)
                        print "Turning alarm on"
                        t.start()                                                      #function to turn on alarm
			list[2] = 0

                if(list[3] == 1):
                        alarm1.lighton()

                if(list[3] == 0):
                        alarm1.lightoff()
                      
		button_value = GPIO.input(BUTTON_IN_PIN)          #if button is pressed
 		print "Button Value is ", button_value
		if(button_value == 1):
			print "The Button was pressed"
                        if(list[3] == 1):
				print "Turning Light off"         #and light is on
				#pairing.stop()
				#if(not pairing.isAlive()):
				#	print "Pairing stopped"
                                list[3] = 0        #then turn off light
                        else:
				print "Turning Light on"         #but if light is off
				#pairing = bluetooth_pairing()
				#pairing.daemon = True
				#pairing.start()
                                list[3] = 1        #then turn on light
                
except KeyboardInterrupt:
        blue_comms.stop()
        alarm1.close()
        raise
