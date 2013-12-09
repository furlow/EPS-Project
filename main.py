#main.py

import RPi.GPIO as GPIO	
import alarmmodules    #is it as simple as this?
from bluetooth_comms import thread_bluetooth_comms
#where bluetooth_comms.py is the file in the same directory and
#thread_bluetooth_comms is the class name??

try:

        list= [0,0,0,0]
        thread_bluetooth_comms(list).start()

        push_init()                 #initiates the push button
        
        # need to create function to set the time
    
	while 1:
		
		if(list[2]== '1'):
                        #there needs to be a function to compare time before alarm is turned on
			alarmon()							#function to turn on alarm

                if(list[3]== '1'):
			lighton()
		
		if(list[3]== '0'):
			lightoff()
			
                if (GPIO.input(22)== '1'):          #if button is pressed
                        if (list[3]== '1'):         #and light is on
                                list[3]= '0'        #then turn off light
                        if (list[3]== '0'):         #but if light is off
                                list[3]= '1'        #then turn on light
		
except KeyboardInterrupt:
	pass
