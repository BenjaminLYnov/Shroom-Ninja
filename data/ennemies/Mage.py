import pygame
import random


class Mage:

    hp = 6
    # Animation call spell

    animationSpellingTime = 0
    direction = 0
    rectPosX = 0
    rectPosY = 64
    isSpelling = False
    speedSpellingTime = 0.2

    # Fire Ball

    animationFireBallTime = 0
    speedAnimationFireBall = 0.1
    speedFireBall = 5
    isFireBall = False
    fireBallRectPosX = 0

    # teleportation

    teleportationTime = 0
    cdTeleportaion = 10
    
    # Hited
    getHitedTime = 0
    getHited = False

    def __init__(self):

        self.sprite = pygame.image.load(
            'resources/images/Mage spell casting sheet.png').convert_alpha()
        self.hitbox = pygame.Rect((random.randint(0, 1600), random.randint(0, 500)), (33, 53))

        self.fireBallSprite = pygame.image.load(
            'resources/images/fire ball.png').convert_alpha()
        self.hitboxFireBall = pygame.Rect((5000000, 300), (154, 122))

        self.lauchFireBallSound = pygame.mixer.Sound('resources/sound/mage/firered_00CF.wav')
        self.teleportationSound = pygame.mixer.Sound('resources/sound/mage/SiteBoss_Warp_Appear.wav')
        self.getHurtSound = pygame.mixer.Sound('resources/sound/mage/FantomGanon_Vo_CryDamage00.wav')
        self.lauchFireBallSoundOnceTime = True

    def display(self, screen):
        if self.hp > 0:
            screen.blit(self.sprite, (self.hitbox.left - 15, self.hitbox.top - 11),
                        (self.rectPosX, self.rectPosY, 64, 64))
            if self.direction == 0:
                screen.blit(pygame.transform.flip(self.fireBallSprite, True, False), (self.hitboxFireBall.left,
                                                                                    self.hitboxFireBall.top), (self.fireBallRectPosX, 0, 154, 122))
            else:
                screen.blit(self.fireBallSprite, (self.hitboxFireBall.left,
                                              self.hitboxFireBall.top), (self.fireBallRectPosX, 0, 154, 122))
        else:
            self.hitboxFireBall.left = 5000000
            
    def gear(self):
        if self.hp > 0:
            self.hitTime()
            self.fireBallLaucnhed()
            self.speelingFireBall()
            self.teleportation()

    def animationFireBall(self):
        self.animationFireBallTime += 1/60
        if self.animationFireBallTime > 6 * self.speedAnimationFireBall:
            self.animationFireBallTime = 0
        elif self.animationFireBallTime > 5 * self.speedAnimationFireBall:
            self.fireBallRectPosX = 154 * 5
        elif self.animationFireBallTime > 4 * self.speedAnimationFireBall:
            self.fireBallRectPosX = 154 * 4
        elif self.animationFireBallTime > 3 * self.speedAnimationFireBall:
            self.fireBallRectPosX = 154 * 3
        elif self.animationFireBallTime > 2 * self.speedAnimationFireBall:
            self.fireBallRectPosX = 154 * 2
        elif self.animationFireBallTime > 1 * self.speedAnimationFireBall:
            self.fireBallRectPosX = 154
        elif self.animationFireBallTime > 0 * self.speedAnimationFireBall:
            self.fireBallRectPosX = 0

    def fireBallLaucnhed(self):
        if self.isFireBall == True:
            self.animationFireBall()
            self.hitboxFireBall.top = self.hitbox.top - 25
            if self.direction == 0:
                self.hitboxFireBall.left -= self.speedFireBall
            else:
                self.hitboxFireBall.left += self.speedFireBall
        if (self.hitboxFireBall.left > 2000) | (self.hitboxFireBall.left < -300):
            self.isFireBall = False

    def animationSpellFireBall(self):
        self.animationSpellingTime += 1/60
        if self.animationSpellingTime > self.speedSpellingTime * 7:
            self.animationSpellingTime = 0
            self.isSpelling = False
            self.lauchFireBallSoundOnceTime = True
        elif self.animationSpellingTime > self.speedSpellingTime * 6:
            self.rectPosX = 64 * 6
        elif self.animationSpellingTime > self.speedSpellingTime * 5:
            self.rectPosX = 64 * 5
            self.isFireBall = True
            if self.lauchFireBallSoundOnceTime == True:
                self.lauchFireBallSoundOnceTime = False
                pygame.mixer.Sound.play(self.lauchFireBallSound)
            if self.direction == 0:
                self.hitboxFireBall.left = self.hitbox.left - 150
            else:
                self.hitboxFireBall.left = self.hitbox.left
            self.hitboxFireBall.top = self.hitbox.top - 25
        elif self.animationSpellingTime > self.speedSpellingTime * 4:
            self.rectPosX = 64 * 4
        elif self.animationSpellingTime > self.speedSpellingTime * 3:
            self.rectPosX = 64 * 3
        elif self.animationSpellingTime > self.speedSpellingTime * 2:
            self.rectPosX = 64 * 2
        elif self.animationSpellingTime > self.speedSpellingTime * 1:
            self.rectPosX = 64 * 1
        elif self.animationSpellingTime > self.speedSpellingTime * 0:
            self.rectPosX = 64 * 0
            if self.direction == 0:
                self.rectPosY = 64
            else:
                self.rectPosY = 192

    def speelingFireBall(self):
        if self.isSpelling == True:
            self.animationSpellFireBall()
        else:
            self.rectPosX = 0

    def hitTime(self):
        if self.getHited == True:
            self.getHitedTime += 1/60
            if self.getHitedTime > 0.2:
                self.getHited = False
                self.getHitedTime = 0
                pygame.mixer.Sound.play(self.getHurtSound)
                
                
    def teleportation(self):
        self.teleportationTime += 1/60
        if self.teleportationTime > self.cdTeleportaion and self.isSpelling == False and self.isFireBall == False:
            self.hitbox.left = random.randint(0, 1600)
            self.hitbox.top = random.randint(0, 500)
            self.teleportationTime = 0
            pygame.mixer.Sound.play(self.teleportationSound)
            
