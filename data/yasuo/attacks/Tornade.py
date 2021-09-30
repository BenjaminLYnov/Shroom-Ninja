import pygame


class Tornade():
    isChargingTornade = False
    jaugeTornade = 0
    tornadePosX = 0
    tornadeDirection = 0
    isTornade = False
    upKeyJ = False
    animationTornadePosX = 0
    animationTornadePosY = 0
    animationTornadeRectX = 0
    speedAnimationTornade = 0.05
    speedMoveTornade = 10
    animationTornadeTime = 0
    tornadeTime = 0

    def __init__(self):
        self.screen = pygame.display.set_mode((960, 539))
        pygame.display.set_caption('Shroom Ninja')
        

        self.tornadeSprite = pygame.image.load(
            'resources/images/attacks-spritesheet.png').convert_alpha()
        self.tornadeRect = self.tornadeSprite.get_rect()
        
        self.hitbox = pygame.Rect((self.tornadeRect.topleft), (self.animationTornadeRectX,  49))

        self.tornadeSound = pygame.mixer.Sound(
            'resources/sound/tornade/tornade.wav')
        self.hasagiSound = pygame.mixer.Sound(
            'resources/sound/yasuoSound/hasagi.wav')

    def display(self, screen):
        if self.isTornade:
            self.hitbox = pygame.Rect((self.tornadeRect.topleft), (self.animationTornadeRectX,  49))
            # pygame.draw.rect(screen, (255, 255, 255), self.hitbox)
            screen.blit(self.tornadeSprite, self.tornadeRect, (self.animationTornadePosX,
                                                               self.animationTornadePosY, self.animationTornadeRectX,  49))

    def animationTornade(self):
        if self.animationTornadeTime >= 0:
            self.animationTornadePosX = 327
            self.animationTornadePosY = 386
            self.animationTornadeRectX = 47
        if self.animationTornadeTime > self.speedAnimationTornade:
            self.animationTornadePosX = 379
        if self.animationTornadeTime > self.speedAnimationTornade * 2:
            self.animationTornadePosX = 432
            self.animationTornadeRectX = 47
        if self.animationTornadeTime > self.speedAnimationTornade * 3:
            self.animationTornadePosX = 485
            self.animationTornadeRectX = 46
        if self.animationTornadeTime > self.speedAnimationTornade * 4:
            self.animationTornadePosX = 537
            self.animationTornadeRectX = 43
        if self.animationTornadeTime > self.speedAnimationTornade * 5:
            self.animationTornadeTime = 0
        self.animationTornadeTime += 1/60

    def attackTornade(self):
        self.upChargeTornade()
        if self.isTornade and self.tornadeTime < 2:
            self.animationTornade()
            if self.tornadeDirection == 0:
                self.tornadeRect = self.tornadeRect.move(
                    [-self.speedMoveTornade, 0])
            else:
                self.tornadeRect = self.tornadeRect.move(
                    [self.speedMoveTornade, 0])
            self.tornadeTime += 1/60
        elif self.tornadeTime > 2:
            pygame.mixer.Sound.stop(self.tornadeSound)
            self.isTornade = False
            self.tornadeTime = 0

    def inputTornade(self, posR, posL, posY, playerDirection):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_j] and self.jaugeTornade == 100 and self.upKeyJ == True:
            self.upKeyJ = False
            pygame.mixer.Sound.play(self.tornadeSound)
            pygame.mixer.Sound.play(self.hasagiSound)
            self.jaugeTornade = 0
            self.isTornade = True
            self.tornadeRect.top = posY
            if playerDirection == 0:
                self.tornadeDirection = 0
                self.tornadeRect.right = posL
            else:
                self.tornadeDirection = 1
                self.tornadeRect.right = posR

        if keys[pygame.K_j] == False:
            self.upKeyJ = True
            self.isChargingTornade = False
        if keys[pygame.K_j]:
            self.isChargingTornade = True
            self.upKeyJ = False

    def upChargeTornade(self):
        if self.isChargingTornade == True and self.jaugeTornade < 100:
            self.jaugeTornade += 1
