import sys

import pygame

from settings import Settings

from ship import Ship

from bullet import Bullet

from alien import Alien

class AlienInvasion:
    '''Overall class to manage game assets and behavior'''
    def _init_(self):
        '''Initialize the game, creat game reasources'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.Screen_height = self.screen.get_rect().height

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption('Alien Invasion')

        self.Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #Set BackGround Color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        '''Start the main loop for game.'''
        while True:

            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
    def _update_bullet(self):
        '''Update position of bullets and get rid of old bullets'''
        #Update bullet position
            #Get rid of bullets that have disappered
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))


        self._update_screen()

            #Watch keyboard and mouse events
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)


            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                   

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _fire_bullet(self):
        '''Create a new bullet and add it to the bullets group'''
        if len(self.bullet) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)



    
        self.bullets.add(new_bullet)







            #Redraw the screen with each pass through the loop 
    def _update_screen(self):
        '''Update images on the screen, and flip to the new screen'''
        self.screen.fill(self.bg_color)
        self.Ship.bitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()


    def _create_fleet(self):
        '''Create the fleet of aliens'''
        #make the alien
        alien = Alien(self)
        alien_width = alien.rect.width
        availble_space_x = self.setting.screen_width - (2* alien_width)
        number_aliens_x = availble_space_x // (2 * alien_width)

        #Creat a first row of aliens
        for alien_number in range(number_aliens_x):
            self._create_alien(alien_number)
    def _create_alien(self, alien_number):
        #creat an alien and place it in the row
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2* alien_width * alien_number
        alien.rect.x = alien.x
        self.aliens.add(alien)

if _name_ == '_main_':

#Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()


