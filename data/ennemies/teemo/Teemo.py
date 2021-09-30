import pygame
import random
from math import *
from data.ennemies.teemo.Shroom import Shroom
import time


class Teemo:

    hp = 30

    # voice sound
    voiceSound = []
    voiceTime = 0
    nextVoice = 7

    # get hurt sound
    getHurtTime = 0
    hurtSound = False
    isGettingHurt = False

    changePosTime = 0

    shroom = []
    indiceDeadShroom = []
    haveDeadShroom = False

    # Send shroom
    isSendingShroom = False
    sendingShroomTime = 0
    lauchingShroomTime = 0
    speedSendShroom = 20
    
    # Hited
    getHitedTime = 0
    getHited = False

    # equation droite
    a = 0
    b = 0
    targetX = 0
    targetY = 0
    isNegatif = False

    # Hited
    getHitedTime = 0
    getHited = False

    # sound after a epxlosion shroom
    madeDammageTime = 0
    madeDammage = False
    madeDammageSound = True

    def __init__(self):

        # Teemo sprite
        self.teemoSprite = pygame.image.load(
            'resources/images/teemo-00.png').convert_alpha()
        self.teemoRect = self.teemoSprite.get_rect()
        self.teemoRect.topleft = [500, 250]
        self.hitbox = pygame.Rect((self.teemoRect.topleft), (50, 50))

        self.voiceSound.append(pygame.mixer.Sound(
            'resources/sound/teemoSound/teemo - laught 1.wav'))
        self.voiceSound.append(pygame.mixer.Sound(
            'resources/sound/teemoSound/teemo - laught 2.wav'))
        self.voiceSound.append(pygame.mixer.Sound(
            'resources/sound/teemoSound/teemo - laught 3.wav'))
        self.voiceSound.append(pygame.mixer.Sound(
            'resources/sound/teemoSound/voice1.wav'))
        self.voiceSound.append(pygame.mixer.Sound(
            'resources/sound/teemoSound/voice2.wav'))
        self.voiceSound.append(pygame.mixer.Sound(
            'resources/sound/teemoSound/voice3.wav'))
        self.voiceSound.append(pygame.mixer.Sound(
            'resources/sound/teemoSound/voice4.wav'))
        self.voiceSound.append(pygame.mixer.Sound(
            'resources/sound/teemoSound/voice5.wav'))
        self.voiceSound.append(pygame.mixer.Sound(
            'resources/sound/teemoSound/voice6.wav'))
        self.voiceSound.append(pygame.mixer.Sound(
            'resources/sound/teemoSound/getHurt1.wav'))
        self.voiceSound.append(pygame.mixer.Sound(
            'resources/sound/teemoSound/getHurt2.wav'))
        self.voiceSound.append(pygame.mixer.Sound(
            'resources/sound/teemoSound/didDammage.wav'))

    def display(self, screen):
        if self.hp > 0:
            self.hitbox = pygame.Rect((self.teemoRect.topleft), (50, 50))
            screen.blit(self.teemoSprite, self.teemoRect)

        self.displayShroom(screen)

    def gear(self):
        if self.hp > 0:
            self.hitTime()
            self.voice()
            self.changePos()
            self.getHurtSound()
            self.dammageSound()
            self.sendShroom(random.randint(0, 1600), random.randint(0, 500))
        for mushroom in self.shroom:
            mushroom.gear()
        self.shroomDead()

    def voice(self):
        if self.madeDammage == False:
            self.voiceTime += 1/60
            if self.voiceTime > self.nextVoice:
                pygame.mixer.Sound.play(self.voiceSound[random.randint(0, 8)])
                self.voiceTime = 0
                self.nextVoice = random.randint(5, 15)

    def changePos(self):
        self.changePosTime += 1/60
        if self.changePosTime > 2:
            self.changePosTime = 0
            self.teemoRect.top = random.randint(0, 700)
            self.teemoRect.right = random.randint(0, 1600)

    def displayShroom(self, screen):
        for mushroom in self.shroom:
            mushroom.display(screen)

    def getShroom(self):
        self.shroom.append(Shroom())
        self.shroom[-1].hitbox.right = self.teemoRect.right
        self.shroom[-1].hitbox.top = self.teemoRect.top

    def sendShroom(self, x, y):
        self.timeToSendShroom(x, y)
        if self.isSendingShroom == True:
            if self.isNegatif == True:
                self.shroom[-1].hitbox.right -= self.speedSendShroom
            else:
                self.shroom[-1].hitbox.right += self.speedSendShroom

            self.shroom[-1].hitbox.top = self.a * \
                self.shroom[-1].hitbox.right + self.b
            self.lauchingShroomTime += 1/60
            if (self.distance2vector(self.shroom[-1].hitbox.right, self.shroom[-1].hitbox.top) <= 50) | (self.lauchingShroomTime > 5):
                self.isSendingShroom = False
                self.shroom[-1].isLaunched = True
                self.lauchingShroomTime = 0

    def timeToSendShroom(self, x, y):
        try:
            if self.isSendingShroom == False:
                self.sendingShroomTime += 1/60

            if self.sendingShroomTime > 0.5:
                self.isSendingShroom = True
                self.sendingShroomTime = 0
                self.getShroom()
                self.targetX = x
                self.targetY = y
                self.a = (self.targetY - self.shroom[-1].hitbox.top) / \
                    (self.targetX - self.shroom[-1].hitbox.right)
                self.b = self.targetY - (self.a * self.targetX)
                if self.targetX < self.shroom[-1].hitbox.right:
                    self.isNegatif = True
                else:
                    self.isNegatif = False
        except:
            pass

    def distance2vector(self, x1, y1):
        return sqrt((self.targetX-x1)**2 + (self.targetY-y1)**2)

    def shroomDead(self):
        self.haveDeadShroom = False

        if len(self.shroom) > 0:

            for i in range(0, len(self.shroom)):
                if self.shroom[i].hp == 0:
                    self.haveDeadShroom = True
                    self.indiceDeadShroom.append(i)

        if self.haveDeadShroom == True:
            for i in range(0, len(self.indiceDeadShroom)):
                self.shroom.pop(self.indiceDeadShroom[i])
                if i < len(self.indiceDeadShroom) - 1:
                    self.indiceDeadShroom[i+1] -= 1
            self.indiceDeadShroom = []

    def hitTime(self):
        if self.getHited == True:
            self.getHitedTime += 1/60
            if self.getHitedTime > 0.2:
                self.getHited = False
                self.getHitedTime = 0

    def dammageSound(self):
        if self.madeDammage == True:
            if self.madeDammageSound == True:
                pygame.mixer.Sound.play(self.voiceSound[11])
                self.madeDammageSound = False
            self.madeDammageTime += 1/60
            if self.madeDammageTime > 10:
                self.madeDammage = False
                self.madeDammageSound = True
                self.madeDammageTime = 0
    
    def getHurtSound(self):
        if self.hurtSound == True:
            self.hurtSound = False
            if self.getHurtTime == 0:
                pygame.mixer.Sound.play(self.voiceSound[random.randint(9, 10)])
                self.isGettingHurt = True
        if self.isGettingHurt == True:
            self.getHurtTime += 1/60
            if self.getHurtTime > 1:
                self.getHurtTime = 0
                self.isGettingHurt = False
