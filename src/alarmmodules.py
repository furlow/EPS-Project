#alarmmodules.py

from time import sleep
import pygame
import serial

class alarm():
    def __init__(self, data):
        
		self.data = data
        
		self.attiny = serial.Serial('/dev/ttyAMA0', 4800)

        pygame.mixer.init(44100,-16,1,4096)
        self.sound = pygame.mixer.Sound("Music/Play Hard.wav")
        self.channelA = pygame.mixer.Channel(1)
        self.channelA.set_volume(0)

    def lighton(self):
        self.attiny.write('B')
        self.data.set_light_status(on)
        print "Turned light on"

    def lightoff(self):
        self.attiny.write('A')
        self.set_light_status(off)
        print "Turned light off"

    def alarmoff(self):
        lightoff()
    
        for volume in range(self.channelA.get_volume * 100, 0, -1)
            self.channelA.set_volume(volume * 0.01)
            sleep(0.1)

        self.channelA.stop()
        print "Alarm has been turned off"
    
    def comparetime (self):
        print "In Comparetime "
        self.differenceintime= self.data.alarm_time - self.data.time
        
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
        
        print "Alarm is on"
        
        self.data.print_settings()
        self.channelA.play(self.sound, -1)
        
        try:
            self.attiny.write('C')
            for volume in range(0, 100, 1):
                self.channelA.set_volume(volume * 0.01)
                sleep(1)

        except KeyboardInterrupt:
            self.close()
            raise
    
    def close(self):
        self.channelA.stop()
        pygame.mixer.quit()
        self.attiny.write('A')
        self.attiny.close()
