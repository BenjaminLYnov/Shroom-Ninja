from data.yasuo.Yasuo import Yasuo
from data.Map.Map import Map
from data.ennemies.teemo.Teemo import Teemo
from data.ennemies.Skull import Skull
from data.ennemies.Mage import Mage
import pygame
from math import *


class Gameplay:

    map = Map()
    player = Yasuo()
    teemo = Teemo()
    skulls = []
    skulls.append(Skull())
    skulls.append(Skull())
    skulls.append(Skull())
    skulls.append(Skull())

    mages = []
    mages.append(Mage())
    mages.append(Mage())
    mages.append(Mage())
    mages.append(Mage())

    def gear(self):
        self.player.gear()
        self.teemo.gear()
        for skull in self.skulls:
            skull.gear()

        for mage in self.mages:
            mage.gear()

        self.collisionStep()
        self.gravityStep()
        self.dammageStep()

    def display(self, screen):
        self.map.display(screen)

        self.teemo.display(screen)

        for skull in self.skulls:
            skull.display(screen)

        for mage in self.mages:
            mage.display(screen)
            
        if self.player.hitbox.left <= 0:
            self.player.hitbox.left = 0
        elif self.player.hitbox.left >= 1500:
            self.player.hitbox.left = 1500
        self.player.display(screen)

    #  Collision

    def collisionStep(self):
        self.checkPlayerOnGround()
        for skull in self.skulls:
            self.checkGround(skull.hitbox)

        for mushroom in self.teemo.shroom:
            self.checkGround(mushroom.hitbox)

        self.collisionBeetweenShroom()

        # player get repousser
        for skull in self.skulls:
            self.wall(self.player.hitbox, skull.hitbox)

        # skull repousse skull
        for i in range(0, len(self.skulls)):
            for j in range(0, len(self.skulls)):
                if j != i:
                    if self.skulls[i].hitbox.colliderect(self.skulls[j].hitbox):
                        if self.skulls[i].hitbox.left > self.skulls[j].hitbox.left:
                            self.skulls[i].hitbox.left += 3
                        if self.skulls[i].hitbox.left < self.skulls[j].hitbox.left:
                            self.skulls[i].hitbox.left -= 3

    def collisionBeetweenShroom(self):
        for i in range(0, len(self.teemo.shroom)):
            for j in range(0, len(self.teemo.shroom)):
                if i != j:
                    if self.teemo.shroom[i].hitbox.colliderect(self.teemo.shroom[j].hitbox):
                        if self.teemo.shroom[i].hitbox.right >= self.teemo.shroom[j].hitbox.right:
                            self.teemo.shroom[i].hitbox.left = self.teemo.shroom[j].hitbox.right

    def checkPlayerOnGround(self):
        self.player.canJump = False
        self.player.canDash = False
        if self.checkGround(self.player.hitbox) == True:
            self.player.canJump = True
            self.player.canDash = True
            if self.player.canLangindSound == True:
                pygame.mixer.Sound.play(self.player.landingSound)
                self.player.canLangindSound = False

    def checkGround(self, spriteRect):
        for plat in self.map.plat:
            if spriteRect.colliderect(plat.hitbox):
                if spriteRect.bottom >= plat.hitbox.top and abs(spriteRect.bottom - plat.hitbox.top) < 10:
                    spriteRect.bottom = plat.hitbox.top + 1
                    return True

    def wall(self, onTheWall, wall):
        if onTheWall.colliderect(wall):
            if onTheWall.left >= wall.left:
                onTheWall.left += 5
            else:
                onTheWall.left -= 5

    # Gravity

    def gravityStep(self):
        self.gravityPlayer()
        self.gravityOnShroom()
        for skull in self.skulls:
            skull.hitbox.top += 3

    def gravityPlayer(self):
        if self.player.canJump == False and self.player.slash.isSlashing == False:
            self.player.hitbox.top = self.player.hitbox.top + 10
            self.player.canLangindSound = True

    def gravityOnShroom(self):
        for mushroom in self.teemo.shroom:
            if mushroom.isLaunched == True:
                mushroom.hitbox.top += 5

    #  dammage

    def dammageStep(self):
        for mushroom in self.teemo.shroom:
            self.playerMakeDammage(
                mushroom, self.player.slash.hitbox, 1, self.player.direction, 10)
            self.playerMakeDammage(
                mushroom, self.player.tornade.hitbox, 4, self.player.tornade.tornadeDirection, 50)
        for skull in self.skulls:
            self.playerMakeDammage(
                skull, self.player.slash.hitbox, 1, self.player.direction, 10)
            self.playerMakeDammage(
                skull, self.player.tornade.hitbox, 4, self.player.tornade.tornadeDirection, 50)
        for mage in self.mages:
            self.playerMakeDammage(
                mage, self.player.slash.hitbox, 1, self.player.direction, 10)
            self.playerMakeDammage(
                mage, self.player.tornade.hitbox, 4, self.player.tornade.tornadeDirection, 50)
            
        if (self.playerMakeDammage(self.teemo, self.player.slash.hitbox, 1, self.player.direction, 0)) == True | (self.playerMakeDammage(self.teemo, self.player.tornade.hitbox, 4, self.player.direction, 0)) == True:
            self.teemo.hurtSound = True

        self.dammageOnPlayerByShroom()
        self.dammageOnPlayerBySkull()
        self.dammageOnPlayerByMage()

        self.tornadeStep()

    def playerMakeDammage(self, ennemie,  attack, dammage, direction, projectionDistance):
        if attack.colliderect(ennemie.hitbox) and ennemie.getHited == False:
            ennemie.hp -= dammage
            try:
                if  self.player.slash.hitbox.colliderect(ennemie.hitbox) and self.player.slash.slashCombo == 4 and ennemie.direction == 0:
                    ennemie.hitbox.right = self.player.slash.hitbox.right + 50
                elif self.player.slash.hitbox.colliderect(ennemie.hitbox) and self.player.slash.slashCombo == 4:
                    ennemie.hitbox.right = self.player.slash.hitbox.right - 170
            except:
                pass
            if direction == 0:
                ennemie.hitbox.right = ennemie.hitbox.right - projectionDistance
            else:
                ennemie.hitbox.right = ennemie.hitbox.right + projectionDistance
            ennemie.getHited = True
            pygame.mixer.Sound.play(self.player.slash.slashHitedSound)
            if ennemie.hp <= 0:
                ennemie.hitbox.right = 5000000
            return True
        else:
            return False


    def dammageOnPlayerByShroom(self):
        for mushroom in self.teemo.shroom:
            if self.player.hitbox.colliderect(mushroom.hitbox) and mushroom.isAnimationExplosion == False:
                mushroom.isAnimationExplosion = True
                self.player.getHurtSound()
                self.player.hp -= 1
                self.teemo.madeDammage = True

    def dammageOnPlayerBySkull(self):

        for skull in self.skulls:
            # Changer direction to go on player
            if skull.isSword == False:
                if abs(self.player.hitbox.left - skull.hitbox.left) < 50:
                    skull.canMove = False
                elif self.player.hitbox.left >= skull.hitbox.left:
                    skull.direction = 1
                else:
                    skull.direction = 0

            # Calculer distance entre player et skull
            distance = sqrt((self.player.hitbox.left - skull.hitbox.left)
                            ** 2 + (self.player.hitbox.top - skull.hitbox.top)**2)
            if distance <= 50:
                skull.canMove = False
                if skull.CDTime >= skull.CDSword:
                    skull.isSword = True
            else:
                skull.canMove = True

            if self.player.hitbox.colliderect(skull.hitboxSword) and self.player.canGetHited == True:
                self.player.getHurtSound()
                self.player.isHited = True
                self.player.hp -= 1
                if skull.direction == 0:
                    self.player.hitbox.left = skull.hitboxSword.left - 30
                else:
                    self.player.hitbox.left = skull.hitboxSword.right

    def dammageOnPlayerByMage(self):

        for mage in self.mages:

            # Changer direction to go on player
            if mage.isFireBall == False and mage.isSpelling == False:
                if self.player.hitbox.left >= mage.hitbox.left:
                    mage.direction = 1
                else:
                    mage.direction = 0

            if abs(self.player.hitbox.top - mage.hitbox.top) <= 50 and mage.isFireBall == False:
                mage.isSpelling = True

            if self.player.hitbox.colliderect(mage.hitboxFireBall) and self.player.canGetHited == True:
                self.player.getHurtSound()
                self.player.isHited = True
                self.player.hp -= 1

    def tornadeStep(self):
        # disapear fireBall
        for mage in self.mages:
            if mage.hitboxFireBall.colliderect(self.player.tornade.hitbox):
                mage.isFireBall = False
                mage.hitboxFireBall.left = 5000000
                
    def checkAllEnnemieDead(self):
        for mage in self.mages:
            if mage.hp > 0:
                return False
        for skull in self.skulls:
            if skull.hp > 0:
                return False
        if self.teemo.hp > 0:
            return False
        return True
