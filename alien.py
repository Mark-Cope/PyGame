import pygame

from pygame import Sprite

class Alien (Sprite):
    '''A class to represent a single alien fleet'''
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Load the alien image and set its starting point
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the aliens exact horizontal position
        self.x = float(self.rect.x)
    def update(self): 
        ''' Move the alien left or right'''
        self.x += (self.setting.alien_speed * self.settings.fleet_direction)
        
        self.rect.x = self.x

    def check_edges(self):
        '''return True if alien is on the edge of the screen'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
            

#We keep the alien features in this folder so that we keep the code clean, in here we can edit the alien its self without messing up the game files