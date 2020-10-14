import pygame.font

class Button:
    def __init__(self, ai_game, msg):
        '''Initialize button attributes'''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #Set the deminsions and properties of the button
        self.width, self.height = 200, 50 
        self.button_color = (0, 255, 0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(none, 48)


        #Build the buttons rect object and center it
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center


        #The button messsage needs to be prepped only once
        self._prep_msg(msg)

    def _prep_msg(self):
        # Draw a blank button and then draw the message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)