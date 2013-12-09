import operator
from time import sleep
import os
import pygame
from bluetooth import *
import RPi.GPIO as GPIO	

def bluetooth_comms():
	
	port = 5
	backlog = 1
	
	server_sock=BluetoothSocket( RFCOMM )
	server_sock.bind(("",port))
	server_sock.listen(backlog)

	uuid = "df0677bc-5f0b-45e4-8207-122adee18805"

	try:
		
		advertise_service( server_sock, "alarm",
							service_id = uuid,
							service_classes = [ uuid, SERIAL_PORT_CLASS],
							profiles = [SERIAL_PORT_PROFILE])
							
		print "waiting for connection..."
		
#		client_sock, client_info = server_sock.accept()
#		print "Accepted connection from ", client_info

		print "waiting for data..."
		
#		data = client_sock.recv(1024)

		data = "1910;1912;1;0";
		current_time = data[0:4];
		alarm_time = data[5:9];
		alarm = data[10];
		light = data[12];
#		client_sock.send ("data sent")
		List = [int(current_time),int(alarm_time),int(alarm),int(light)]
		
		print List
		
	except keyboardInterrupt:
		
		stop_advertising (server_sock)        
		client_sock.close()
		server_sock.close()
		
	return List

def lighton():
	
	GPIO.setmode(GPIO.BOARD)									# Set pin convention.
	GPIO.setwarnings(False)
	GPIO.setup(13, GPIO.OUT, initial= GPIO.LOW)					# Set up channel 13 to be output and set the output to low.
	p = GPIO.PWM(13, 100)  										# Channel=13, Frequency=100Hz.
	p.start(100)												# Set duty cycle to 100.
	
	print "Dutycycle set to 100"
	
	return

def lightoff():
	
	GPIO.setmode(GPIO.BOARD)									# Set pin convention.
	GPIO.setwarnings(False)
	p.stop()													# Stop PWM
	GPIO.cleanup()												# Changes all channels used by script back to inputs.
	
	print "Dutycycle set to 0"
	
	return

def alarmoff():
	
	p.stop()													# Stop PWM
	GPIO.cleanup()												# Changes all channels used by script back to inputs.
	channelA.stop()
	a=0
	
	return


def alarmon():
	
	pygame.mixer.init(22050,-16,1,4096)												# Initiate pygame module.
	sound = pygame.mixer.Sound("Play Hard.wav")	#need to make track as long as gradual wake up
	channelA = pygame.mixer.Channel(1)
	channelA.set_volume(0.0)													#test
	channelA.play(sound, -1)
	j=0.01
	#turn on leds

	GPIO.setmode(GPIO.BOARD)									# Set pin convention.
	GPIO.setwarnings(False)
	GPIO.setup(13, GPIO.OUT, initial= GPIO.LOW)					# Set up channel 13 to be output and set the output to low.
	p = GPIO.PWM(13, 100)		  								# Channel=13, Frequency=100Hz.
	p.start(0)													# Start PWM with duty cycle of 0.


	try:
		for dutycycle in range(0, 101, 1):					# Use dutycycle of 0,5,10,15,20....100.         IS THIS ':' NEEDED?
			
			channelA.set_volume(j)
			p.ChangeDutyCycle(dutycycle)					# Change dutycycle.
			j=j+0.01
			time.sleep(50)										# Delays the code for 60secs.
			a=1
			
			if dutycycle == '100':								# If dutycycle reaches maximium
			
				while a:							#track plays on replay
					
					bluetooth_comms()
					if list[2] == '0':
						alarmoff
												# time.sleep(1800)									# Then delay by 30mins/ stay on until turned off 
						
	except KeyboardInterrupt:
		pass
		
	return


# A check to see if push button is pressed, before it goes into bluetooth mode?

try:
	while 1:
		list = bluetooth_comms()
		
		if(list[2]== '1'):
			alarmon()							#function to turn on alarm
		
		if(list[3]== '1'):
			lighton()
		
		if(list[3]== '0'):
			lightoff()
		
		# set time and compare time
		# when alarmtime== current time-30??
		# call function alarm on
					
except KeyboardInterrupt:
	pass

