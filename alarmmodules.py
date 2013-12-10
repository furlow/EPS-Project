#alarmmodules.py

from time import sleep
import pygame
import RPi.GPIO as GPIO 

def lighton():
        
        GPIO.setmode(GPIO.BOARD)                                                                        # Set pin convention.
        GPIO.setwarnings(False)
        GPIO.setup(13, GPIO.OUT, initial= GPIO.LOW)                                     # Set up channel 13 to be output and set the output to low.
        p = GPIO.PWM(13, 100)                                                                           # Channel=13, Frequency=100Hz.
        p.start(100)                                                                                            # Set duty cycle to 100.
        
        print "Dutycycle set to 100"
        
        return

def lightoff():
        
        GPIO.setmode(GPIO.BOARD)                                                                        # Set pin convention.
        GPIO.setwarnings(False)
        p = GPIO.PWM(13, 100)
        p.stop()                                                                                                        # Stop PWM
        #GPIO.cleanup()                                                                                         # Changes all channels used by script back to inputs.
        
        print "Dutycycle set to 0"
        
        return

def alarmoff():

        GPIO.setmode(GPIO.BOARD)                                                                        # Set pin convention.
        GPIO.setwarnings(False)
        p = GPIO.PWM(13, 100)
        p.stop()                                                                                                        # Stop PWM
        #GPIO.cleanup()                                                                                         # Changes all channels used by script back to inputs.
        channelA.stop()
        a=0

        print "Alarm has been turned off"
        
        return


def alarmon(list):
        

	print list

        pygame.mixer.init(22050,-16,1,4096)                                                                                             # Initiate pygame module.
        sound = pygame.mixer.Sound("Play Hard.wav")     #need to make track as long as gradual wake up?
        channelA = pygame.mixer.Channel(1)
        channelA.set_volume(0.0)                                                                                                        #test
        channelA.play(sound, -1)
        j=0.01
        #turn on leds

        GPIO.setmode(GPIO.BOARD)                                                                        # Set pin convention.
        GPIO.setwarnings(False)
        GPIO.setup(13, GPIO.OUT, initial= GPIO.LOW)                                     # Set up channel 13 to be output and set the output to low.
        p = GPIO.PWM(13, 100)                                                                           # Channel=13, Frequency=100Hz.
        p.start(0)                                                                                                      # Start PWM with duty cycle of 0.

        print "Turning on the LEDs and Audio"

        try:
                for dutycycle in range(0, 101, 1):                                      # Use dutycycle of 0,5,10,15,20....100.         IS THIS ':' NEEDED?
                        
                        channelA.set_volume(j)
                        p.ChangeDutyCycle(dutycycle)                                    # Change dutycycle.
                        j=j+0.01
                        time.sleep(50)                                                                          # Delays the code for 60secs.
                        a=1
                        
                        if dutycycle == '100':                                                          # If dutycycle reaches maximium
                        
                                while a:                                                        #track plays on replay
                                        
                                        if list[2] == '0':
                                                alarmoff()
                                                                                                # time.sleep(1800)                                                                      # Then delay by 30mins/ stay on until turned off 
                                                
        except KeyboardInterrupt:
                pass
                
        return


def push_init():

        GPIO.setmode(GPIO.BOARD)                                                                        # Set pin convention.
        GPIO.setwarnings(False)
        GPIO.setup(22, GPIO.IN, initial= GPIO.LOW)

        return
