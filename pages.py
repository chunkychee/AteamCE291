import gui
import settings


class MainMenu:
    def __init__(self, screen):
        # creation of the texts
        self.mainMenuTexts = []
        # self.mainMenuTexts.append(gui.Text(screen, text="maze & smart solver", pos=(settings.SCREEN_WIDTH // 2, 100),
        #                                    fontSize=84, color=settings.DARK_BLUE))
        self.mainMenuTexts.append(gui.Text(screen, text="Instructions", pos=(settings.SCREEN_WIDTH // 2, 340),
                                           fontSize=int(settings.DEFAULT_FONT_SIZE * 1.5)))
        self.mainMenuTexts.append(gui.Paragraph(screen, xPos=None, yStartPos=380,
                                                text="In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate\n"
                                                     "the visual form of a document or a typeface without relying on meaningful content.\n"
                                                     "Lorem ipsum may be used as a placeholder before final copy is available."))
        self.mainMenuTexts.append(
            gui.Text(screen, text="The A{gile} Team", pos=(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT - 10),
                     color=settings.GRAY, fontSize=18))

        # creation of the buttons
        self.mazeGeneratorButton = gui.Button(screen, pos=(settings.SCREEN_WIDTH // 2 - 135, 480),
                                              text="Maze Generator")
        self.smartSolverButton = gui.Button(screen, pos=(settings.SCREEN_WIDTH // 2 + 135, 480), text="Smart Solver")

        # image
        self.logoImage = gui.Image(screen, "assets/images/Logo.png", (settings.SCREEN_WIDTH // 2, -20), size=(560, 425))

    def run(self, isLeftMouseButtonPressed):
        # image
        self.logoImage.draw()
        # texts
        for text in self.mainMenuTexts:
            text.draw()
        # buttons
        self.mazeGeneratorButton.run(isLeftMouseButtonPressed)
        self.smartSolverButton.run(isLeftMouseButtonPressed)
