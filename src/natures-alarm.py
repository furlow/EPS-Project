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
    data = app_data()
	
	#Start the pairing thread
	#pairing = bluetooth_pairing()

	#Start the bluetooth communications thread
    blue_comms = bluetooth_comms(data)
    blue_comms.daemon = True
    blue_comms.start()
    
    main_alarm = alarm(data)

	print "Current totalsecs is 0"

    while 1:
        sleep(0.1)
        
        data.print_settings()

		#if(pairing.isAlive()):
		#	print "Pairing Live"


        if(data.alarm_status() == True):
            totalsecs = main_alarm.comparetime()
            print "Totalsecs in main is", totalsecs
            alarm_timer = Timer ( totalsecs, main_alarm.alarmon )
			alarm_timer.daemon = True
            print "Turning alarm on"
            alarm_timer.start()
			data.set_alarm_status(False)

            #if(list[3] == 1):
            #   alarm1.lighton()

            #if(list[3] == 0):
            #   alarm1.lightoff()
        
        #Move this into and class
		button_value = GPIO.input(BUTTON_IN_PIN)
 		print "Button Value is ", button_value

		if(button_value == 1 and button_value_previous == 0):
            print "The Button was pressed"
            
            if(data.light_status == False):
                alarm1.lighton()
                data.set_light_status(True)
            else:
				alarm1.lightoff()
                data.set_light_status(False)
		button_value_previous = button_value
                
except KeyboardInterrupt:
    blue_comms.stop()
    alarm1.close()
    raise
