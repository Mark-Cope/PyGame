import pygame

from pygame import Sprite

class Alien(Sprite):
    '''A class to represent a single alien fleet'''
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        #Load the alien image and set its starting point
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the aliens exact horizontal position
        self.x = float(self.rect.x)