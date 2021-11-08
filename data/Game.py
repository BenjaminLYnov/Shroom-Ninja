from data.Gameplay import Gameplay
from data.Menu import Menu
import pygame


class Game:

    def __init__(self):
        pygame.init()

        self.gameplay = Gameplay()
        self.menu = Menu()
        self.showMenu = True
        self.showGameOver = False
        self.gameOverSoundOnceTime = True
        self.isStarted = False
        self.isPause = False
        self.isWon = False
        self.wonSoundOnceTime = True
        self.mainThemeOnceTime = True

        # Make the game window
        self.height = 1080
        self.width = 1920
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        # self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Shroom Ninja')

        self.gameOverImage = pygame.image.load(
            "./resources/images/game over.png").convert()
        self.congrulationImage = pygame.image.load(
            "./resources/images/congrulation.png").convert()
        self.congrulationImage = pygame.transform.scale(
            self.congrulationImage, (1200 + 400, 675 + 200))
        self.gameOverImage = pygame.transform.scale(
            self.gameOverImage, (1200 + 400, 675 + 200))

        self.gameOverSound = pygame.mixer.Sound(
            'resources/sound/yasuoSound/snd_vc_link_Damage01.wav')

        # Make the clock for time and 60fps lock
        self.clock = pygame.time.Clock()

        # # Game loop
        self.running = True

    def run(self):

        while self.running:

            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if (self.isWon == True) | (self.gameplay.player.hp <= 0):
                            self.running = False
                        elif self.isPause == True:
                            self.isPause = False
                        else:
                            self.isPause = True
                            self.showMenu = True

            self.menuGear()

            self.runGame()

            self.gameOver()

            self.gameWon()

            # Update the self.screen
            pygame.display.flip()

            # Wait for the next frame, make 60fps
            self.clock.tick(60)

            # # Close the game
        pygame.quit()

    def runGame(self):
        if self.isStarted == True and self.isPause == False and self.gameplay.player.hp > 0:
            if self.mainThemeOnceTime == True:
                self.mainThemeOnceTime = False
            self.gameplay.gear()
            self.gameplay.display(self.screen)

    def gameOver(self):
        if self.gameplay.player.hp <= 0:
            self.isPause = True
            self.showGameOver = True
            pygame.mixer.music.stop()
            

        if self.showGameOver == True:
            self.screen.blit(self.gameOverImage, (0, 0))
            if self.gameOverSoundOnceTime == True:
                self.gameOverSoundOnceTime = False
                pygame.mixer.Sound.play(self.gameplay.player.deadSound)

    def gameWon(self):
        if self.gameplay.checkAllEnnemieDead() == True:
            self.isWon = True

        if self.isWon == True:
            self.screen.blit(self.congrulationImage, (0, 0))
            if self.wonSoundOnceTime == True:
                self.wonSoundOnceTime = False
                pygame.mixer.music.load(
                    "resources/sound/yasuoSound/Yasuo, the Unforgiven - Login Screen - League of Legends.wav")
                pygame.mixer.music.play(-1)

    def menuGear(self):
        if self.showMenu == True:
            self.menu.display(self.screen)
            if self.menu.play.check_click() == True:
                if self.isStarted == True:
                    if self.isPause == True:
                        self.isPause = False
                    else:
                        self.isPause = True
                        self.showMenu = True

                self.isStarted = True
                self.showMenu = False

            if self.menu.showInput.check_click() == True:
                if self.menu.isShowInput == True:
                    self.menu.isShowInput = False
                else:
                    self.menu.isShowInput = True
                    self.menu.isShowObjectif = False

            if self.menu.objectif.check_click() == True:
                self.menu.isShowObjectif = True
                self.menu.isShowInput = False

            if self.menu.quitter.check_click() == True:
                self.running = False

            if self.isStarted == True:
                gui_font = pygame.font.Font(None, 50)
                self.menu.play.text_surf = gui_font.render(
                    "Back", True, '#FFFFFF')
