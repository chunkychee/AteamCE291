import gui
import settings
import pygame  # might remove if not needed anymore
import tkinter
import tkinter.filedialog
import os
import maze


class MainMenu:
    def __init__(self, screen):
        # image
        self.logoImage = gui.Image(screen, "assets/images/Logo.png", (settings.SCREEN_WIDTH // 2, -20), size=(600, 338))
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
            gui.Text(screen, text="The A{gile} Team", pos=(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT - 20),
                     color=settings.GRAY, fontSize=24)
        )

        # creation of the buttons
        self.mazeGeneratorButton = gui.Button(screen, pos=(settings.SCREEN_WIDTH // 2 - 135, 480),
                                              text="Maze Generator")
        self.smartSolverButton = gui.Button(screen, pos=(settings.SCREEN_WIDTH // 2 + 135, 480), text="Smart Solver")


    def run(self, isLeftMouseButtonPressed):
        # image
        self.logoImage.draw()
        # texts
        for text in self.mainMenuTexts:
            text.draw()
        # buttons
        if self.mazeGeneratorButton.run(isLeftMouseButtonPressed):  # redirect the user to the MazeGenerator page
            return "MazeGenerator"
        self.smartSolverButton.run(isLeftMouseButtonPressed)



class MazeGeneratorPage:
    def __init__(self, screen):
        self.showTipsAndTricks = True  # will show the tips and tricks text
        self.screen = screen
        # creation of the images
        self.logoImage = gui.Image(screen, "assets/images/Logo.png",
                                   (settings.PANEL_WIDTH // 2, settings.SCREEN_HEIGHT - 120),
                                   size=(249, 135))
        self.dottedGridMImage = gui.Image(screen, "assets/images/Dotted Grid (m).png", (settings.PANEL_WIDTH, 0),
                                          positionType="topleft", size=(918, 680))

        # creation of the texts
        self.titleText = gui.Text(screen, text="Maze Generator", pos=(20, 20), positionType="topleft", fontSize=32,
                                  color=settings.DARK_BLUE)
        self.mazeGeneratorInfosParagraph = gui.Paragraph(screen, xPos=20, yStartPos=60,
                                                         text="Maze Number: \nMaze file Name: \nMaze Size: \n"
                                                              "\nStats For Nerds \nCells Explored: \nSolution Path: \nTime: ")
        self.TipsAndTricksTitleText = gui.Text(screen, text="Tips & Tricks", pos=(
        settings.PANEL_WIDTH + (settings.SCREEN_WIDTH - settings.PANEL_WIDTH) // 2, 80),
                                               positionType="center", fontSize=72, color=settings.DARK_BLUE,
                                               backgroundColor=settings.WHITE)
        self.TipsAndTricksParagraph = gui.Paragraph(screen, xPos=settings.PANEL_WIDTH + 95, yStartPos=150, fontSize=32,
                                                    backgroundColor=settings.WHITE, lineSpacing=77,
                                                    text="1.Click 'Generate Level' if this is your first attempt \n"
                                                         "2.Click 'Upload Level File' if you have one. Then Click on Generate Maze\n"
                                                         "3.Next go on to 'Solve Level'  \n"
                                                         "4.Once the level is solved select 'Go To Smart Solver'")
        # creation of the buttons
        buttonYStartPos = 260  # the first button y position
        buttonsSpaces = 20  # the space between each buttons
        self.uploadLevelFileButton = gui.Button(screen, pos=(settings.PANEL_WIDTH // 2, buttonYStartPos),
                                                text="Upload Level File")
        self.generateMazeButton = gui.Button(screen, pos=(
            settings.PANEL_WIDTH // 2, buttonYStartPos + buttonsSpaces + settings.DEFAULT_BUTTON_SIZE[1]),
                                             text="Generate Maze")
        self.solveLevelButton = gui.Button(screen, pos=(
            settings.PANEL_WIDTH // 2, buttonYStartPos + buttonsSpaces * 2 + settings.DEFAULT_BUTTON_SIZE[1] * 2),
                                           text="Solve Level")
        self.goToSmartSolverButton = gui.Button(screen, pos=(
            settings.PANEL_WIDTH // 2, buttonYStartPos + buttonsSpaces * 3 + settings.DEFAULT_BUTTON_SIZE[1] * 3),
                                                text="Go To Smart Solver")
        self.homeButton = gui.Button(screen, pos=(
            settings.PANEL_WIDTH // 2, buttonYStartPos + buttonsSpaces * 4 + settings.DEFAULT_BUTTON_SIZE[1] * 4),
                                     text="Home", color=settings.GRAY)
        self.reset()

    def reset(self):
        self.maze = None
        self.mazeNumber = 0
        self.mazeGeneratorInfosParagraph.resetText()

    def uploadLevelFileButtonAction(self):
        """ pressing on the 'Upload Level File' button will call this function
            :return fileName: the name of the maze txt file
        """
        # txt file selection prompt
        top = tkinter.Tk()
        top.withdraw()  # hide window
        filePath = tkinter.filedialog.askopenfilename(parent=top, initialdir=os.getcwd(),
                                                      filetypes=(('text files', 'txt'),),
                                                      title="Open your maze text file")
        top.destroy()
        # create the maze board
        try:
            with open(filePath, 'r') as f:
                mazeBoard = [list(line.replace("\n", "")) for line in f]
                print("")
                # convert all the string number to int
                for lineNb in range(len(mazeBoard)):
                    print(mazeBoard[lineNb])
                    for colNb in range(len(mazeBoard[lineNb])):
                        mazeBoard[lineNb][colNb] = int(mazeBoard[lineNb][colNb])
            self.fileName = filePath[filePath.rindex("/")+1: filePath.index(".txt")]  # keep just the file name
            self.mazeNumber += 1
            # create the maze
            self.maze = maze.Maze(self.screen, mazeBoard)
        except Exception as error:
            print(f"{error}\nThe file is not valid... Please try again")

    def run(self, isLeftMouseButtonPressed):
        pygame.draw.rect(self.screen, settings.WHITE,
                         (settings.PANEL_WIDTH, 0, settings.SCREEN_WIDTH - settings.PANEL_WIDTH,
                          settings.SCREEN_HEIGHT))  # show the panel
        # image
        self.logoImage.draw()
        # texts
        self.titleText.draw()
        self.mazeGeneratorInfosParagraph.draw()
        # buttons
        if self.uploadLevelFileButton.run(isLeftMouseButtonPressed) and self.maze is None:
            self.showTipsAndTricks = False
            self.uploadLevelFileButtonAction()  # will allow the user to select a maze

        elif self.generateMazeButton.run(isLeftMouseButtonPressed) and self.maze is not None:
            # self.showTipsAndTricks = False
            self.mazeGeneratorInfosParagraph.addText(self.mazeNumber, self.fileName, f"{len(self.maze.board[0])}x{len(self.maze.board)}")
            self.maze.show = True

        elif self.solveLevelButton.run(isLeftMouseButtonPressed) and self.maze is not None and self.maze.show:
            print(self.maze.DFS_Solve())
            pass

        elif self.goToSmartSolverButton.run(isLeftMouseButtonPressed):
            # self.showTipsAndTricks = False
            pass

        elif self.homeButton.run(isLeftMouseButtonPressed):  # redirect the user to the main menu page
            # self.showTipsAndTricks = True
            return "mainMenu"


        if self.showTipsAndTricks:
            self.dottedGridMImage.draw()
            self.TipsAndTricksTitleText.draw()
            self.TipsAndTricksParagraph.draw()

        if self.maze is not None and self.maze.show:
            self.maze.draw()
