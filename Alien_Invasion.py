import sys

from time import sleep

import pygame

from settings import Settings 

from game_stats import GameStats                  #Import the other files onto the main one, This keeps our code clean and we dont have to go digging

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
        self.settings.screen_width = self.screen.get_rect().width                       #Location of the Screen settings 
        self.settings.Screen_height = self.screen.get_rect().height

        self.screen = ((self.settings.screen_width, self.settings.Screen_height))
        pygame.display.set_caption('Alien Invasion')

        #Create an instance tp store game statistics 
        self.stats = GameStats(self)

        self.ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #Set BackGround Color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        '''Start the main loop for game.'''
        while True:

            self._check_events()
            self.ship.update()                                                          #Updating the running parts of the game
            self.bullets.update()
            self._update_aliens()
            self._update_screen()


    def _update_bullet(self):
        '''Update position of bullets and get rid of old bullets'''
        #Update bullet position
        #Get rid of bullets that have disappered
        for bullet in self.bullets.copy():                                              #Here is where the bullet is managed and changed during the game
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collision()
        print(len(self.bullets))

    def _check_bullet_alien_collision(self):
        #Check to see if any bullets have hit any aliens
        #If so get rid of that bullet and the alien
        collision = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            #Destroy existing bullets and creat a new fleet
            self.bullets.empty()
            self._create_fleet()
    
    def _update_aliens(self):
        '''Update the position of all aliens in the fleet'''
        self.aliens.update()

        #Look for collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print('Ship Hit!!!')

        '''Check if fleet is at an edge, then update the positions of all aliens in the fleet'''        #checks to make sure the aliens stay in the screen and react the way they are suppose to when they reach the edge
        self._check_fleet_edges()
        self._update_screen()

            #Watch keyboard and mouse events
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


            elif event.type == pygame.KEYDOWN:                                        #This is the starting and stopping functions of the game
                self._check_keydown_events(event)


            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                   

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:                                            #The keyboard controls of the game
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
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)

                                                                            #This is where the bullet mechanicls come from
        self.bullets.add(new_bullet)




            #Redraw the screen with each pass through the loop 
    def _update_screen(self):
        '''Update images on the screen, and flip to the new screen'''
        self.screen.fill(self.bg_color)
        self.ship.bitme()
        for bullet in self.bullets.sprites():                                #This is where we update the screen while the game is running so the user can see it
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()


    def _create_fleet(self):
        '''Create the fleet of aliens'''
        #make the alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size                                     #This is what creates the rows of aliens in the game and manages them
        availble_space_x = self.settings.screen_width - (2* alien_width)
        number_aliens_x = availble_space_x // (2 * alien_width)
        
        #Determain the number of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height
        availble_space_y = (self.settings.Screen_height (3 * alien_height)- ship_height)
        number_rows = availble_space_y // ( 2 * alien_height)

        for row_number in range (number_rows):
        #Creat a first row of aliens
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
    
    
    
    def _create_alien(self, alien_number, row_number):
        #creat an alien and place it in the row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien_width = alien.rect.width
        alien.x = alien_width + 2* alien_width * alien_number               #This creates a single alien and is used in the function above to create the rows of aliens
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        '''Responds appropriatly if any aliens have reached the edge'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        '''Drop the entire fleet and change fleets direction'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


if _name_ == '_main_':

#Make a game instance, and run the game                                   #Where the game is actually called which makes it run
    ai = AlienInvasion()
    ai.run_game()