import pygame
from data.Map.Platform import Platform


class Map():

    def __init__(self):
        super().__init__()

        # Load background
        self.background = pygame.image.load(
            'resources/images/background.png').convert()

        # Load plateform
        self.heightPlat = 100
        self.plat = []
        
        # Midle
        self.plat.append(Platform(1, (800, self.heightPlat * 2)))
        self.plat.append(Platform(1, (800, self.heightPlat * 4)))
        self.plat.append(Platform(1, (800, self.heightPlat * 6)))
        
        # left
        self.plat.append(Platform(1, (150, self.heightPlat * 2)))
        self.plat.append(Platform(1, (150, self.heightPlat * 6)))
        self.plat.append(Platform(1, (480, self.heightPlat * 1)))
        self.plat.append(Platform(1, (480, self.heightPlat * 3)))
        self.plat.append(Platform(1, (480, self.heightPlat * 5)))
        
        # Right
        self.plat.append(Platform(1, (1400, self.heightPlat * 2)))
        self.plat.append(Platform(1, (1400, self.heightPlat * 5)))
        self.plat.append(Platform(1, (1100, self.heightPlat * 3)))
      
        # self.plat.append(Platform(1, (1400, self.heightPlat * 4)))
        self.plat.append(Platform(0, (800, 700)))

    def display(self, screen):
        screen.blit(self.background, (-150, -200))
        for platform in self.plat:
            platform.display(screen)
