import pygame

class Games:
    def __init__(self):

        self.width = 800
        self.height = 800
        self.rgb = (245,210,245)

        self.game_window = pygame.display.set_mode((self.width,self.height))

        self.clock = pygame.time.Clock()
        background_image = pygame.image.load('assests/bg.jpg')
        self.background = pygame.transform.scale(background_image,(self.width,self.height))

        treasure_image = pygame.image.load('assests/img3.jpg')
        self.treasure = pygame.transform.scale(treasure_image,(80,80))

    def draw_objects(self):
        self.game_window.fill(self.rgb)
        self.game_window.blit(self.background,(0,0))
        self.game_window.blit(self.treasure,(375,50))
        pygame.display.update()

           





    def run_game_loop(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return


            self.draw_objects()
            self.clock.tick(60)

        

 