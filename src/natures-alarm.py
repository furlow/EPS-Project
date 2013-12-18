#!/usr/bin/python

import RPi.GPIO as GPIO 
from alarmmodules import *
from bluetooth_module import *
from time import sleep
from threading import Timer
from bluetooth_pairing_module import bluetooth_pairing


try:

        list = [0,0,0,0]
	
	#Start the pairing thread
	pairing = bluetooth_pairing()
	pairing.daemon = True
	pairing.start()
	
	#Start the bluetooth communications thread
        blue_comms = bluetooth_comms(list)
        blue_comms.daemon = True

        print "In Main ", list      

        blue_comms.start()

        print "In Main ", list

        alarm1 = alarm()
	totalsecs=0
	print "Current totalsecs is 0"
        while 1:
                
                sleep(3)
                print "In Main ", list

                if(list[2]== 1):
                        totalsecs = alarm1.comparetime(list)
                        print "Totalsecs in main is", totalsecs
                        t= Timer (int(totalsecs),alarm1.alarmon(list))
                        print "Turning alarm on"
                        t.start()                                                      #function to turn on alarm

                if(list[3]== 1):
                        alarm1.lighton()

                if(list[3]== 0):
                        alarm1.lightoff()
                        
                if (GPIO.input(22)== 1):          #if button is pressed
                        if (list[3]== 1):         #and light is on
                                list[3]= 0        #then turn off light
                        if (list[3]== 0):         #but if light is off
                                list[3]= 1        #then turn on light
                
except KeyboardInterrupt:
        blue_comms.stop()
        alarm1.close()
        raise
