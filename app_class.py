import pygame
import os
import sys
import settings
import gui
import pages


class App:
    def __init__(self):
        # Setup pygame/window
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 32)  # windows position on the user screen
        pygame.init()
        pygame.display.set_caption('maze & smart solver')  # name of the app window
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT), 0, 32)

        # creation of the buttons
        self.buttonTest1 = gui.Button(self.screen, (200, 200), text="bTest1")
        self.buttonTest2 = gui.Button(self.screen, (400, 200), text="bTest2", rectSize=(200, 200), roundedCornerRadius=0, color="#797979")

        # creation of the texts
        self.textTest1 = gui.Text(self.screen, text="textTest1", pos=(200, 400))
        self.textTest2 = gui.Text(self.screen, text="textTest2", pos=(0, 0), positionType="topleft", fontSize=60,
                                  color=(22, 210, 111))

        # creation of the pages
        self.mainMenu = pages.MainMenu(self.screen)

    def checkQuit(self, events):
        """ Checks if the user want to close the app"""
        for event in events:
            if event.type == pygame.QUIT:  # checks if the user is pressing on the window close button
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # checks if the user is pressing the ESC key
                    pygame.quit()
                    sys.exit()

    def getEvents(self):
        """ pygame.event.get() should only be called one time in the loop and will be used several time throughout the program
            :return: the user events (for example the key pressed, mouse click...)
        """
        return pygame.event.get()

    def isLeftMouseButtonPressed(self, events):
        """
        :param events: all user events
        :return: True if the left mouse button is pressed
        """
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    return True
        return False

    def run(self):
        """ Makes the app run"""
        state = "mainMenu"

        while True:
            # get the events and quit the app if needed
            events = self.getEvents()
            isLeftMouseButtonPressed = self.isLeftMouseButtonPressed(events)
            self.checkQuit(events)

            # make the mainMenu functional
            if state == "mainMenu":
                nextState = self.mainMenu.run(isLeftMouseButtonPressed)

            elif state == "aboutPage":
                nextState = self.aboutPage.run(isLeftMouseButtonPressed)
            state = nextState if nextState is not None else state  # change to the new state if it is not None

            # update the screen
            pygame.display.update()
            self.screen.fill(settings.BACKGROUND_COLOR)
