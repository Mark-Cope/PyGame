class Settings:
    '''A classs to stroe all the settings for Alien Invasion'''
    def _init_(self):
        '''Initialize the gammes static settings'''
        #Screen Settings
        self.screen_width = 1200
        self.Screen_height = 800
        self.bg_color = (230, 230, 230)

        #Ship Settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        #Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        #Alien Settings
        self.alien_speed = 1.0 
        self.fleet_drop_speed = 10
        #Fleet_direction of 1 represnts right, -1 represents left
        self.fleet_direction = 1

        #How Quickly the game speeds up
        self.speedup_scale = 1.1

        #How quickly alien points increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''Initialize settings that change throughout the game'''
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        #Scoring
        self.alien_points = 50
        
        #Fleet_direction of 1 represnts right, -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        '''Increase the speed and alien points'''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)


#We want to keep all the settings in one place because we dont want the code to get messy plus if we need to change anyhting it is much easier to find in this folder instead of the bigger one