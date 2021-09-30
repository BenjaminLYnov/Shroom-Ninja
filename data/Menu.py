from data.Button import Button
import pygame

class Menu:    
    
    def __init__(self):
        self.isShowInput = False
        self.isShowObjectif = False
        self.play = Button('Jouer', 250, 80 ,(50, 100),6)
        self.showInput = Button('Commandes', 250, 80, (50,210),6)
        self.objectif = Button('Objectif', 250, 80, (50,320),6)
        self.quitter = Button('Quitter', 250, 80, (50,430),6)
        self.background = pygame.image.load("./resources/images/backgroundMenu.png").convert()
        self.input = pygame.image.load("./resources/images/input.png").convert_alpha()
        self.objectifImage = pygame.image.load("./resources/images/objectif.png").convert_alpha()
        
    def display(self, screen):
        screen.blit(self.background, (-200, 0))
        if self.isShowInput == True:
            screen.blit(self.input, (400, 200))
            
        if self.isShowObjectif == True:
            screen.blit(self.objectifImage, (400, 200))
            
        self.showInput.display(screen)
        self.objectif.display(screen)
        self.quitter.display(screen)
        self.play.display(screen)
        

