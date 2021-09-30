import pygame
import random

class Skull:

    hp = 10
    # Animation Move

    animationMoveTime = 0
    rectPosX = 0
    rectPosY = 0
    skullRectX = 0
    skullRectY = 0
    speedMove = 0.1
    direction = 1
    canMove = True

    # Attack sword
    animationSwordTime = 0
    speedSword = 0.1
    isSword = False
    swordSoundOnceTime = True
    CDSword = 5
    CDTime = 0
    
    # Hited
    getHitedTime = 0
    getHited = False
    
    # return top
    returnTopTime = 0
    cdReturnTop = random.randint(10, 20)

    def __init__(self):

        self.sprite = pygame.image.load(
            'resources/images/sprite skull with hat.png').convert_alpha()
        self.rect = self.sprite.get_rect()
        self.hitbox = pygame.Rect((random.randint(0, 1600), random.randint(0, 500)), (27, 40))
        self.hitboxSword = pygame.Rect((1000000, 300), (57, 52))
        
        self.swordSound = pygame.mixer.Sound(
            'resources/sound/Skull/skullSound.wav')

    def display(self, screen):
        if self.hp > 0:
            screen.blit(self.sprite, self.rect,
                    (self.rectPosX, self.rectPosY, self.skullRectX, self.skullRectY))

    def gear(self):
        if self.hp > 0:
            self.hitTime()
            self.move()
            self.attackSword()
            self.returnOnTop()

    def animationMove(self):
        self.skullRectX = 40
        self.skullRectY = 53
        self.rect.left = self.hitbox.left
        self.rect.top = self.hitbox.top - 10
        self.animationMoveTime += 1/60
        if self.animationMoveTime > 0 * self.speedMove:
            if self.direction == 1:
                self.rectPosX = 9
                self.rectPosY = 715
            else:
                self.rectPosX = 18
                self.rectPosY = 587
        if self.animationMoveTime > 1 * self.speedMove:
            if self.direction == 1:
                self.rectPosX = 74
            else:
                self.rectPosX = 82
        if self.animationMoveTime > 2 * self.speedMove:
            if self.direction == 1:
                self.rectPosX = 138
            else:
                self.rectPosX = 145
        if self.animationMoveTime > 3 * self.speedMove:
            if self.direction == 1:
                self.rectPosX = 202
            else:
                self.rectPosX = 210
        if self.animationMoveTime > 4 * self.speedMove:
            if self.direction == 1:
                self.rectPosX = 266
            else:
                self.rectPosX = 274
        if self.animationMoveTime > 5 * self.speedMove:
            if self.direction == 1:
                self.rectPosX = 330
            else:
                self.rectPosX = 338
        if self.animationMoveTime > 6 * self.speedMove:
            if self.direction == 1:
                self.rectPosX = 393
            else:
                self.rectPosX = 402
        if self.animationMoveTime > 7 * self.speedMove:
            if self.direction == 1:
                self.rectPosX = 458
            else:
                self.rectPosX = 466
        if self.animationMoveTime > 8 * self.speedMove:
            if self.direction == 1:
                self.rectPosX = 522
            else:
                self.rectPosX = 530
        if self.animationMoveTime > 9 * self.speedMove:
            self.animationMoveTime = 0

    def animationSword(self):
        self.skullRectX = 103
        self.skullRectY = 53
        if self.direction == 1:
            self.rect.left = self.hitbox.left
            self.rect.top = self.hitbox.top - 10
        else:
            self.rect.left = self.hitbox.left - 60
            self.rect.top = self.hitbox.top - 10

        self.hitboxSword.left = 50000000

        self.animationSwordTime += 1/60
        if self.animationSwordTime > 5 * self.speedSword:
            self.animationSwordTime = 0
            self.CDTime = 0
            self.isSword = False
        elif self.animationSwordTime > 4 * self.speedSword:
            if self.direction == 1:
                self.rectPosX = 1035
            else:
                self.rectPosX = 975
        elif self.animationSwordTime > 3 * self.speedSword:
            if self.direction == 1:
                self.rectPosX = 843
                self.hitboxSword.left = self.hitbox.left + 45
                self.hitboxSword.top = self.hitbox.top + 0
            else:
                self.hitboxSword.left = self.hitbox.left - 58
                self.hitboxSword.top = self.hitbox.top + 0
                self.rectPosX = 783
        elif self.animationSwordTime > 2 * self.speedSword:
            if self.direction == 1:
                self.rectPosX = 650
            else:
                self.rectPosX = 592
        elif self.animationSwordTime > 1 * self.speedSword:
            if self.direction == 1:
                self.rectPosX = 460
            else:
                self.rectPosX = 400
        elif self.animationSwordTime > 0 * self.speedSword:
            if self.direction == 1:
                self.rectPosX = 268
                self.rectPosY = 1997
            else:
                self.rectPosX = 207
                self.rectPosY = 1613

    def move(self):
        self.rect.left = self.hitbox.left
        self.rect.top = self.hitbox.top - 10
        if self.isSword == False and self.canMove == True:
            if self.direction == 0:
                self.hitbox.left -= 3
            else:
                self.hitbox.left += 3
            self.animationMove()

    def attackSword(self):
        self.CDTime += 1/60
        if self.isSword == True:
            if self.swordSoundOnceTime == True:
                pygame.mixer.Sound.play(self.swordSound)
                self.swordSoundOnceTime = False
            self.animationSword()
        else:
            self.swordSoundOnceTime = True

    def hitTime(self):
        if self.getHited == True:
            self.getHitedTime += 1/60
            if self.getHitedTime > 0.2:
                self.getHited = False
                self.getHitedTime = 0
                
    def returnOnTop(self):
        self.returnTopTime += 1/60
        if self.returnTopTime > self.cdReturnTop:
            self.hitbox.top = 0
            self.hitbox.left = random.randint(0, 1500)
            self.cdReturnTop = random.randint(10, 20)
            self.returnTopTime = 0