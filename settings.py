class Settings:
    '''A classs to stroe all the settings for Alien Invasion'''
    def _init_(self):
        '''Initialize the games settings'''
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



#We want to keep all the settings in one place because we dont want the code to get messy plus if we need to change anyhting it is much easier to find in this folder instead of the bigger one