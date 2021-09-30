import pygame


class Slash:
    upKeyJ = True
    isSword = False
    isSlashing = False
    speedAttackSword = 1
    slashCombo = 0
    canSlash = True
    swordPosX = 0
    swordPosY = 0
    swordRectX = 0
    swordRectY = 0
    swordComboTime = 0
    swordCombo4Time = 0
    canSlashTime = 0
    direction = 1

    def __init__(self):
        self.screen = pygame.display.set_mode((960, 539))
        pygame.display.set_caption('Shroom Ninja')

        self.swordSprite = pygame.image.load('resources/images/slash.png').convert_alpha()
        self.swordRect = self.swordSprite.get_rect()
        
        self.hitbox = pygame.Rect((self.swordRect.topleft), (self.swordRectX, self.swordRectY))

        self.slash1Sound = pygame.mixer.Sound('resources/sound/slashSound/slash1.wav')
        self.slash2Sound = pygame.mixer.Sound('resources/sound/slashSound/slash2.wav')
        self.slashHitedSound = pygame.mixer.Sound('resources/sound/slashSound/firered_000D.wav')

    def display(self, screen):
        if self.slashCombo > 0 and self.swordComboTime < 1:
            self.hitbox = pygame.Rect((self.swordRect.topleft), (self.swordRectX, self.swordRectY))
            # pygame.draw.rect(screen, (255, 255, 255), self.hitbox)
            if self.direction == 0:
                screen.blit(pygame.transform.flip(self.swordSprite, True, False), self.swordRect,
                            (self.swordPosX, self.swordPosY, self.swordRectX, self.swordRectY))
            else:
                screen.blit(self.swordSprite, self.swordRect, (self.swordPosX,
                            self.swordPosY, self.swordRectX, self.swordRectY))
        else:
            self.hitbox = pygame.Rect((0, 0), (0, 0))

    def attackSword(self):
        self.swordSlash()

    def inputAttackSword(self, 
                        posRightPlayer1, posUpPlayer1,
                        posRightPlayer2, posUpPlayer2,
                        posRightPlayer3, posUpPlayer3,
                        posRightPlayer4, posUpPlayer4,
                        posLeftPlayer1,
                        posLeftPlayer2,
                        posLeftPlayer3,
                        posLeftPlayer4):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_j] and self.upKeyJ == True and self.canSlash == True:
            self.slashCombo += 1
            if self.slashCombo == 4:
                pygame.mixer.Sound.play(self.slash2Sound)
            else:
                pygame.mixer.Sound.play(self.slash1Sound)
            self.swordComboTime = 0
            self.upKeyJ = False
            self.animationSlash(posRightPlayer1, posUpPlayer1,
                                posRightPlayer2, posUpPlayer2,
                                posRightPlayer3, posUpPlayer3,
                                posRightPlayer4, posUpPlayer4,
                                posLeftPlayer1,
                                posLeftPlayer2,
                                posLeftPlayer3,
                                posLeftPlayer4)

        if not keys[pygame.K_j]:
            self.upKeyJ = True

    def swordSlash(self):
        if self.slashCombo > 0:
            self.isSlashing = True
            if self.slashCombo == 4:
                self.canSlash = False
                self.swordCombo4Time += 1/60
                if self.swordCombo4Time > 0.3:
                    self.canSlash = True
                    self.isSlashing = False
                    self.slashCombo = 0
                    self.swordCombo4Time = 0
                    self.swordComboTime = 0
            else:
                self.swordComboTime += 1/60
                if self.swordComboTime > 0.2:
                    self.slashCombo = 0
                    self.isSlashing = False
                    self.swordComboTime = 0

    def animationSlash(self,
                       posRightPlayer1, posUpPlayer1,
                       posRightPlayer2, posUpPlayer2,
                       posRightPlayer3, posUpPlayer3,
                       posRightPlayer4, posUpPlayer4,
                       posLeftPlayer1,
                       posLeftPlayer2,
                       posLeftPlayer3,
                       posLeftPlayer4):

        if self.slashCombo == 1:
            self.swordRect.top = posUpPlayer1
            if self.direction == 1:
                self.swordRect.right = posRightPlayer1
                self.swordPosX = 1017
                self.swordPosY = 40
                self.swordRectX = 100
                self.swordRectY = 127
            else:
                self.swordRect.right = posLeftPlayer1
                self.swordPosX = 1130
                self.swordPosY = 40
                self.swordRectX = 100
                self.swordRectY = 127
        elif self.slashCombo == 2:
            self.swordRect.top = posUpPlayer2
            if self.direction == 1:
                self.swordRect.right = posRightPlayer2
                self.swordPosX = 1160
                self.swordPosY = 50
                self.swordRectX = 100
                self.swordRectY = 127
            else:
                self.swordRect.right = posLeftPlayer2
                self.swordPosX = 978
                self.swordPosY = 50
                self.swordRectX = 100
                self.swordRectY = 127
        elif self.slashCombo == 3:
            self.swordRect.top = posUpPlayer3
            if self.direction == 1:
                self.swordRect.right = posRightPlayer3
                self.swordPosX = 1318
                self.swordPosY = 60
                self.swordRectX = 110
                self.swordRectY = 127
            else:
                self.swordRect.right = posLeftPlayer3
                self.swordPosX = 825
                self.swordPosY = 60
                self.swordRectX = 110
                self.swordRectY = 127
        elif self.slashCombo == 4:
            self.swordRect.top = posUpPlayer4
            if self.direction == 1:
                self.swordRect.right = posRightPlayer4
                self.swordPosX = 1480
                self.swordPosY = 40
                self.swordRectX = 155
                self.swordRectY = 160
            else:
                self.swordRect.right = posLeftPlayer4
                self.swordPosX = 614
                self.swordPosY = 40
                self.swordRectX = 155
                self.swordRectY = 160
