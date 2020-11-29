import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #A class to represent an Alien
    def __init__(self, ai_settings, screen):
        #Initialize the alien and set its starting position
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load the alie image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        #Draw the alien
        self.screen.blit(self.image, self.rect)
