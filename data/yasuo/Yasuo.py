import pygame
from data.yasuo.attacks.Tornade import Tornade
from data.yasuo.attacks.Slash import Slash
import random


class Yasuo:
    pygame.init()

    # Init Var
    direction = 1  # 1 -> droite    0 -> gauche
    hp = 20
    
    # get hited
    isHited = False
    canGetHited = True
    getHitedTime = 0

    #    Move
    canMove = True
    isMoving = False
    speedMove = 5
    moveTimer = 0
    right = False
    left = False
    animationMovePosX = 0
    animationMovePosY = 82
    speedAnimationMove = 0.1

    # Jump
    canJump = False
    isJumping = False
    jumpTime = 0
    upKeyK = True
    canLangindSound = True

    # dash
    isDashing = False
    upKeyl = True
    canDash = False
    speedDash = 10
    dashTime = 0
    dashSound = pygame.mixer.Sound('resources/sound/yasuoSound/dash.wav')

    # Tornade
    tornade = Tornade()

    # Slash
    slash = Slash()

    def __init__(self):

        # Yasuo sprite
        self.yasuoSprite = pygame.image.load(
            'resources/images/yasuo-spritesheet.png').convert_alpha()
        self.hitbox = pygame.Rect((500, 300), (27, 40))
        self.landingSound = pygame.mixer.Sound(
            'resources/sound/yasuoSound/downOnGround.wav')

        self.hurtSound = []
        self.hurtSound.append(pygame.mixer.Sound('resources/sound/yasuoSound/snd_vc_link_Damage01.wav'))
        self.hurtSound.append(pygame.mixer.Sound('resources/sound/yasuoSound/snd_vc_link_Damage02.wav'))
        self.deadSound = pygame.mixer.Sound('resources/sound/yasuoSound/fortnite-death-sound-effect-hd.wav')
        
        self.heart = pygame.image.load('resources/images/heart.png').convert_alpha()
        self.heart_rect = self.heart.get_rect()
        
    def display(self, screen):

        # display tornade
        self.tornade.display(screen)
        if self.tornade.jaugeTornade == 100:
            self.tornade.animationTornade()
            screen.blit(self.tornade.tornadeSprite, (self.hitbox.left - 7, self.hitbox.top - 10), (self.tornade.animationTornadePosX,
                                                               self.tornade.animationTornadePosY, self.tornade.animationTornadeRectX,  49))
        # display yasuo
        self.hitbox = pygame.Rect(
            (self.hitbox.left, self.hitbox.top), (27, 40))
        # pygame.draw.rect(screen, (4, 255, 255), self.hitbox)
        screen.blit(self.yasuoSprite, (self.hitbox.left, self.hitbox.top),
                    (self.animationMovePosX, self.animationMovePosY, 27, 40))


        # display sword slash
        self.slash.display(screen)
        self.display_life(screen)

    def display_life(self, screen):
        for x in range(self.hp):
            screen.blit(self.heart, (self.heart_rect.width * x, 0))
        
    def input(self):
        self.inputJump()
        self.inputDash()
        self.inputMove()
        self.slash.inputAttackSword(self.hitbox.right + 2230, self.hitbox.top - 80,
                                    self.hitbox.right + 2240, self.hitbox.top - 80,
                                    self.hitbox.right + 2240, self.hitbox.top - 80,
                                    self.hitbox.right + 2155, self.hitbox.top - 80,
                                    self.hitbox.right + 2150,
                                    self.hitbox.right + 2140,
                                    self.hitbox.right + 2140,
                                    self.hitbox.right + 2155)
        self.tornade.inputTornade(
            self.hitbox.right + 780, self.hitbox.right + 700, self.hitbox.top - 10, self.direction)

    def inputMove(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] and not keys[pygame.K_q]:
            self.right = True
            self.direction = 1

        if keys[pygame.K_q] and not keys[pygame.K_d]:
            self.left = True
            self.direction = 0

        if not keys[pygame.K_d]:
            self.right = False
        if not keys[pygame.K_q]:
            self.left = False

    def inputJump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_k] and self.upKeyK == True and self.canJump == True:
            self.isJumping = True
            self.canJump = False
        elif not keys[pygame.K_k]:
            self.isJumping = False
            self.jumpTime = 0
            self.upKeyK = True

    def inputDash(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_l] and self.upKeyl == True and self.canDash == True:
            self.isDashing = True
            self.upKeyl = False
            pygame.mixer.Sound.play(self.dashSound)
        elif not keys[pygame.K_l]:
            self.isDashing = False
            self.dashTime = 0
            self.upKeyl = True

    def jump(self):
        if self.isJumping == True:
            self.jumpTime += 1/60
            self.hitbox = self.hitbox.move([0, -25])
            if self.jumpTime > 0.2:
                self.isJumping = False
                self.jumpTime = 0
                self.upKeyK = False
        else:
            self.speedJump = 0

    def moving(self):
        if self.isDashing:
            self.speedMove = 0
        else:
            self.speedMove = 5

        if self.slash.slashCombo > 0:
            self.canMove = False
        elif self.slash.slashCombo == 0:
            self.canMove = True

        if self.canMove == True:
            if self.right | self.left:
                self.animationMove()
                self.isMoving = True
            else:
                self.isMoving = False
            if self.right:
                self.hitbox = self.hitbox.move([self.speedMove, 0])
                self.animationMovePosY = 82
                self.slash.direction = 1
            elif self.left:
                self.hitbox = self.hitbox.move([-self.speedMove, 0])
                self.animationMovePosY = 42
                self.slash.direction = 0
            else:
                self.animationMovePosX = 32

    def dash(self):
        if self.slash.isSlashing == True:
            self.isDashing = False
        if self.isDashing == True:
            if self.direction == 0:
                self.hitbox.right = self.hitbox.right - self.speedDash
            else:
                self.hitbox.right = self.hitbox.right + self.speedDash
            self.dashTime += 1/60
            if self.dashTime > 0.7:
                self.dashTime = 0
                self.isDashing = False

    def animationMove(self):
        if self.moveTimer >= 0:
            self.animationMovePosX = 64
        if self.moveTimer > self.speedAnimationMove:
            self.animationMovePosX = 0
        if self.moveTimer > self.speedAnimationMove * 2:
            self.moveTimer = 0
        self.moveTimer += 1/60

    def attack(self):
        self.slash.attackSword()
        self.tornade.attackTornade()

    def gear(self):
        self.input()
        self.attack()
        self.moving()
        self.jump()
        self.dash()
        self.hitedGear()

    def getHurtSound(self):
        pygame.mixer.Sound.play(self.hurtSound[random.randint(0, 1)])
        
    def hitedGear(self):
        if self.isHited == True and self.canGetHited == True:
            self.canGetHited = False    
            
        if self.isHited == True :
            self.getHitedTime += 1/60
            if self.getHitedTime > 1:
                self.canGetHited = True
                self.isHited = False
                self.getHitedTime = 0
