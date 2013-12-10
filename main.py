#main.py

import RPi.GPIO as GPIO 
from alarmmodules import *
from bluetooth_module import *

try:

        list= [0,0,0,0]

        blue_comms = bluetooth_comms(list)

        print list      

        blue_comms.start()

        print list

        alarm1 = alarm()
        
        # need to create function to set the time
    
        print "position 1"

        while 1:

                print "position 2"
                
                if(list[2]== 1):
                        #there needs to be a function to compare time before alarm is turned on
                        print "Turning alarm on"
                        alarm1.alarmon(list)                                                       #function to turn on alarm

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
