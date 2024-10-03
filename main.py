#imports
import pygame
import sys

class main:
    def __init__(self):

        pygame.init()
        pygame.display.set_caption('Our Game Name')

        self.screen = pygame.display.set_mode((640,480))
        self.clock = pygame.time.Clock()

        # sounds
        self.sfx = {
            'ambience' : pygame.mixer.Sound('data/sfx/ambience.wav')
        }
        self.sfx['ambience'].set_volume(0.2)

    

    def run(self):
        #load the song into pygame
        pygame.mixer.music.load('data/music.wav')
        pygame.mixer.music.set_volume(0.5)
        #loop the song and ambience infinitely
        pygame.mixer.music.play(-1)
        self.sfx['ambience'].play(-1)

        #this is where our game runs
        while True:
            self.screen.fill((14,219,248))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            

            pygame.display.update()
            #framerate of 60 
            self.clock.tick(60)

main().run()