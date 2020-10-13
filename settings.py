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

        #Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
