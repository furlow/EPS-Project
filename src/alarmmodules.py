#alarmmodules.py

from time import sleep
import pygame
import RPi.GPIO as GPIO 

class alarm():
        def __init__(self):
                GPIO.setmode(GPIO.BOARD)                                                                        # Set pin convention.
                GPIO.setwarnings(False)
                GPIO.setup(13, GPIO.OUT, initial= GPIO.LOW)                                     # Set up channel 13 to be output and set the output to low.
                self.light = GPIO.PWM(13, 100)

                GPIO.setup(22, GPIO.IN, initial= GPIO.LOW)
                
                pygame.mixer.init(22050,-16,1,4096)                                                                                       # Initiate pygame module.
                self.sound = pygame.mixer.Sound("Music/Play Hard.wav")     #need to make track as long as gradual wake up?
                self.channelA = pygame.mixer.Channel(1)
        
        def lighton(self):                                                   # Channel=13, Frequency=100Hz.
                self.light.start(100)                                                                                            # Set duty cycle to 100.
                print "Dutycycle set to 100"
                return

        def lightoff(self):
                self.light.stop()                                                                                                        # Stop PWM                                                                                         # Changes all channels used by script back to inputs.
                print "Dutycycle set to 0"
                return

        def alarmoff(self):
                volume=1
                
                for dutycycle in range(101,0,1):                                      # Use dutycycle of 0,5,10,15,20....100.         IS THIS ':' NEEDED?
                                
                                self.channelA.set_volume(volume)
                                self.light.ChangeDutyCycle(dutycycle)                                    # Change dutycycle.
                                volume=volume-0.01
                                sleep(0.1)                                                                          # Delays the code for 60secs.

                self.light.stop()
                self.channelA.stop()
                self.a=0 #what does this line do?    - its to escape the loop when this function returns to alarmon
                print "Alarm has been turned off"
                return

        def comparetime (self, list):
                print "In Comparetime "
                self.differenceintime= list[1]-list[0]

                print 'Alarm will go off in' 
                print self.differenceintime
                print 
                self.dmins =self.differenceintime%100
                self.dhour = (self.differenceintime-self.dmins)/ 100

                print 'Alarm will go off in'
                print self.dhour
                print 'hours and' 
                print self.dmins 
                print 'minutes!'
                print
                self.totalmins= self.dmins+ (self.dhour*60)

                print 'Alarm will go off in' 
                print self.totalmins 
                print 'minutes.'
                print 
                self.totalsecs= self.totalmins *60

                print 'Alarm will go off in' 
                print self.totalsecs
                print 'seconds.'
                print 
                return self.totalsecs


        def alarmon(self, list):

                print "In Alarm ", list
                
                self.channelA.set_volume(0.0)                                                                                                        #test
                self.channelA.play(self.sound, -1)
                volume=1

                self.light.start(0)                                                                                                      # Start PWM with duty cycle of 0.

                print "Turning on the LEDs and Audio"

                try:
                        for dutycycle in range(0, 101, 1):                                      # Use dutycycle of 0,5,10,15,20....100.         IS THIS ':' NEEDED?
                                
                                self.channelA.set_volume(volume)
                                self.light.ChangeDutyCycle(dutycycle)                                    # Change dutycycle.
                                # volume=volume+0.01
                                sleep(1)                                                                          # Delays the code for 60secs.
                                self.a=1
                                
                                if dutycycle == '100':                                                          # If dutycycle reaches maximium
                                
                                        while self.a:                                                        #track plays on replay
                                                
                                                if list[2] == '0':
                                                        alarmoff()
                                                                                                        # time.sleep(1800)                                                                      # Then delay by 30mins/ stay on until turned off 
                                                        
                except KeyboardInterrupt:
                    self.close()
                    raise
                        
                return

        def close(self):
                self.channelA.stop()
                pygame.mixer.quit()
                return
