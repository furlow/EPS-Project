#alarmmodules.py

from time import sleep
import pygame
import serial
#import RPi.GPIO as GPIO 

class alarm():
        def __init__(self, list):

		self.list = list

		self.attiny = serial.Serial('/dev/ttyAMA0', 4800)

                #GPIO.setmode(GPIO.BOARD)                                                                        # Set pin convention.
                #GPIO.setwarnings(False)

                #GPIO.setup(self.BUTTON_IN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
                
                pygame.mixer.init(44100,-16,1,4096)                                                                                       # Initiate pygame module.
                self.sound = pygame.mixer.Sound("Music/Play Hard.wav")     #need to make track as long as gradual wake up?
		self.channelA = pygame.mixer.Channel(1)
		self.channelA.set_volume(0)
        
        def lighton(self):                                                   # Channel=13, Frequency=100Hz.
                self.attiny.write('B')                                                                                                        # Stop PWM                                                                                         # Changes all channels used by script back to inputs.
                print "Turned light on"
                return

        def lightoff(self):
                self.attiny.write('A')                                                                                                        # Stop PWM                                                                                         # Changes all channels used by script back to inputs.
                print "Turned light off"
                return

        def alarmoff(self):
                volume=1

		self.attiny.write('A')                

                for dutycycle in range(101,0,1):                                      # Use dutycycle of 0,5,10,15,20....100.         IS THIS ':' NEEDED?                                
                                self.channelA.set_volume(volume)
                                # self.light.ChangeDutyCycle(dutycycle)                                    # Change dutycycle.
                                volume=volume-0.01
                                sleep(0.1)                                                                          # Delays the code for 60secs.

                #self.light.stop()
                self.channelA.stop()
                self.a=0 #what does this line do?    - its to escape the loop when this function returns to alarmon
                print "Alarm has been turned off"
                return

        def comparetime (self):
                print "In Comparetime "
                self.differenceintime= self.list[1] - self.list[0]

                print 'Alarm will go off in' 
                print self.differenceintime
                print 
                self.dmins = self.differenceintime % 100
                self.dhour = ( self.differenceintime - self.dmins ) / 100

                print 'Alarm will go off in'
                print self.dhour
                print 'hours and' 
                print self.dmins 
                print 'minutes!'
                print
                self.totalmins = self.dmins + ( self.dhour * 60 )

                print 'Alarm will go off in' 
                print self.totalmins 
                print 'minutes.'
                print 
                self.totalsecs = self.totalmins * 60

                print 'Alarm will go off in' 
                print self.totalsecs
                print 'seconds.'
                print 
                return self.totalsecs


        def alarmon(self):

                print "In Alarm ", self.list
                
                self.channelA.play(self.sound, -1)

		volume_float = 0.0

                print "Turning on the LEDs and Audio"

                try:
			print "writin to the attiny"
        		self.attiny.write('C')
                     	for volume in range(0, 100, 1):
				volume_float = volume * 0.01
				print "volume", volume_float
                        	self.channelA.set_volume(volume_float)
                                sleep(1)
                        
                except KeyboardInterrupt:
                	self.close()
		  	raise
                        
                return

        def close(self):
                self.channelA.stop()
                pygame.mixer.quit()
        	self.attiny.write('A')
        	self.attiny.close()
                return
