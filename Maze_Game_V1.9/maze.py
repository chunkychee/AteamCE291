import pygame
import settings

class Maze:
    def __init__(self, surface, board):
        self.surface = surface
        self.board = board  # a board looks like this : [[1,1,0], [0,1,2],[3,0,0]]
        self.show = False
        mazeBorderSpace = 20  # the border size between the screen top and maze top, and the screen bottom and maze bottom
        self.mazeSize = min(settings.SCREEN_WIDTH - settings.PANEL_WIDTH - 2*mazeBorderSpace, settings.SCREEN_HEIGHT - 2*mazeBorderSpace)
        self.tileSize = self.mazeSize // len(self.board)
        self.linesWidth = 2
        self.linesColor = settings.BLACK


    def draw(self):
        """ Center the maze and draw every tile and draw the lines between the tiles
        """

        mazeXStartPos = settings.PANEL_WIDTH + (settings.SCREEN_WIDTH - settings.PANEL_WIDTH)//2 - self.mazeSize//2  # the X position of the top left tile
        mazeYStartPos = settings.SCREEN_HEIGHT//2 - self.mazeSize//2  # the y position of the top left tile
        # draw the tiles
        for lineNb, line in enumerate(self.board):
            yPos = mazeYStartPos + lineNb*self.tileSize
            for colNb, tile in enumerate(line):
                xPos = mazeXStartPos + colNb*self.tileSize
                pygame.draw.rect(self.surface, settings.MAZE_COLOR[tile], (xPos, yPos, self.tileSize, self.tileSize))
            #pygame.draw.line(self.surface, self.linesColor, (mazeXStartPos, yPos), (mazeXStartPos+self.mazeSize, yPos), self.linesWidth)
        # draw the lines
        for nb in range(len(self.board) + 1):
            # draw the horizontal lines
            yPos = mazeYStartPos + nb*self.tileSize
            pygame.draw.line(self.surface, self.linesColor, (mazeXStartPos, yPos),
                             (mazeXStartPos + self.tileSize*len(self.board), yPos), self.linesWidth)
            # draw the vertical lines
            xPos = mazeXStartPos + nb * self.tileSize
            pygame.draw.line(self.surface, self.linesColor, (xPos, mazeYStartPos),
                             (xPos, mazeYStartPos + self.tileSize*len(self.board)), self.linesWidth)

    def makeGraphFromBoard(self, board):
        graph = {}
        boardSize = len(board)
        directions = ((0, -1), (1, 0), (0, 1), (-1, 0))
        for lineNb, line in enumerate(board):
            for colNb, tile in enumerate(line):
                if tile != 1:  # if the tile is not a wall
                    neighbours = []
                    for direction in directions:  # looks in the 4 directions and add the tile to the neighbour list if it is not a wall
                        colIndex = colNb + direction[0]
                        lineIndex = lineNb + direction[1]
                        if colIndex < 0 or colIndex >= boardSize:  # checks the colIndex is out of the board
                            continue
                        if lineIndex < 0 or lineIndex >= boardSize:  # checks the lineIndex is out of the board
                            continue
                        if board[lineIndex][colIndex] != 1:  # checks if the neighbour tile is not a wall
                            neighbours.append((colIndex, lineIndex))
                    graph[(colNb, lineNb)] = set(neighbours)
        return graph

    def DFS_Solve(self):
        graph = self.makeGraphFromBoard(self.board)
        print(graph)




class Tile:
    def __init__(self, colNb):
        tileDico = {0: "Path", 1: "Wall", 2: "Start", 3:"Goal"}


