import pygame
import time


class Shroom:

    isLaunched = False
    hp = 3
    getHitedTime = 0
    getHited = False

    # animation explosion
    isAnimationExplosion = False
    animationExplosionTime = 0
    speedanimationExplosion = 0.1
    explosionPosX = 0
    explosionPosY = 0
    getExplosionPosOncetime = True
    exploseOncetime = True
    explosionWidth = 0
    explosionHeight = 0
    explosionRectPosX = 500000
    explosionRectPosY = 500000

    def __init__(self):

        # Shroom sprite
        self.sprite = pygame.image.load(
            'resources/images/shroom.png').convert_alpha()
        self.hitbox = self.sprite.get_rect()

        self.explosion = pygame.image.load(
            'resources/images/animation-de-feuille-de-sprite-d-explosion-toxique-acide-de-bande-dessinée-69141844.png').convert_alpha()

        self.exploseSound = pygame.mixer.Sound(
            'resources/sound/teemoSound/teemo-shroom-explosion-sound.wav')

    def display(self, screen):
        if self.isAnimationExplosion == False and self.exploseOncetime == True:
            screen.blit(self.sprite, self.hitbox)
        elif self.exploseOncetime == True:
            screen.blit(self.explosion, (self.explosionPosX, self.explosionPosY),
                        (self.explosionRectPosX, self.explosionRectPosY, 160, 160))

        # screen.blit(self.explosion, (self.explosionPosX, self.explosionPosY),
            # (self.explosionRectPosX, self.explosionRectPosY, 160, 160))

    def gear(self):
        self.hitTime()
        self.explosionAnimation()

    def hitTime(self):
        if self.getHited == True:
            self.getHitedTime += 1/60
            if self.getHitedTime > 0.2:
                self.getHited = False
                self.getHitedTime = 0

    def explosionSound(self):
        pygame.mixer.Sound.play(self.exploseSound)

    def explosionAnimation(self):
        if self.isAnimationExplosion == True and self.exploseOncetime == True:
            if self.getExplosionPosOncetime == True:
                self.getExplosionPosOncetime = False
                self.explosionPosX = self.hitbox.left - 50
                self.explosionPosY = self.hitbox.top - 50
                pygame.mixer.Sound.play(self.exploseSound)

            self.animationExplosionTime += 1/60

            if self.animationExplosionTime > self.speedanimationExplosion * 8:
                self.explosionRectPosX = 0
                self.explosionRectPosY = 0
                self.hp = 0
                self.isAnimationExplosion = False
                self.exploseOncetime = False
                self.animationExplosionTime = 0

            elif self.animationExplosionTime > self.speedanimationExplosion * 7:
                self.explosionRectPosX = 563
            elif self.animationExplosionTime > self.speedanimationExplosion * 6:
                self.explosionRectPosX = 390
            elif self.animationExplosionTime > self.speedanimationExplosion * 5:
                self.explosionRectPosX = 220
            elif self.animationExplosionTime > self.speedanimationExplosion * 4:
                self.explosionRectPosX = 50
                self.explosionRectPosY = 280
            elif self.animationExplosionTime > self.speedanimationExplosion * 3:
                self.explosionRectPosX = 576
                self.explosionRectPosY = 68
            elif self.animationExplosionTime > self.speedanimationExplosion * 2:
                self.explosionRectPosX = 394
            elif self.animationExplosionTime > self.speedanimationExplosion * 1:
                self.explosionRectPosX = 217
                self.explosionRectPosY = 72
            elif self.animationExplosionTime > self.speedanimationExplosion * 0:
                self.explosionRectPosX = 58
                self.explosionRectPosY = 66
