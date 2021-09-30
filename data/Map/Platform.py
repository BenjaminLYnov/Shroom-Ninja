import pygame


class Platform:

    def __init__(self, type, pos):
        self.image = pygame.image.load(
            f'resources/images/platform-0{type}.png').convert_alpha()
        self.rect = self.image.get_rect(midtop=pos)

        self.hitbox = pygame.Rect(pos, (290, 10))
        self.hitbox.right = self.hitbox.right - 140
        self.hitbox.top = self.hitbox.top

        if type == 0:
            self.image.set_colorkey((255, 255, 255))
            self.hitbox = pygame.Rect((0, 735), (2000, 10))

    def display(self, screen):
        screen.blit(self.image, self.rect)
        # pygame.draw.rect(screen, (255, 255, 255, 255), self.hitbox)
