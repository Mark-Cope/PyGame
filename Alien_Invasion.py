import sys

import pygame

from settings import Settings

from ship import Ship

class AlienInvasion:
    '''Overall class to manage game assets and behavior'''
    def _init_(self):
        '''Initialize the game, creat game reasources'''
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption('Alien Invasion')

        self.Ship(self)

        #Set BackGround Color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        '''Start the main loop for game.'''
        while true:

            self._check_events()
            self._update_screen()

            #Watch keyboard and mouse events
        def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #Redraw the screen with each pass through the loop 
        def _update_screen(self):
            '''Update images on the screen, and flip to the new screen'''
            self.screen.fill(self.bg_color)
            self.Ship.bitme()
            pygame.display.flip()


if _name_ == '_main_':

#Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()


