import pygame
from time import sleep

pygame.mixer.init(22050,-16,1,4096)                                                                                      
sound = pygame.mixer.Sound("Music/Play Hard.wav") 
channelA = pygame.mixer.Channel(1) 
channelA.set_volume(1)                                                                                                 
channelA.play(sound)
sleep(200)

# self.channelA.stop()
