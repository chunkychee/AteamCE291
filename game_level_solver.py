import pygame

#SETTING START AND END NODES TO RED
START_NODE_ONE_COLOR=pygame.Color(255, 87, 87)
#SETTING START AND END NODES TO BLUE
START_NODE_TWO_COLOR=pygame.Color(0,74,173)

#SETTING CURRENT NODE
CURRENT_NODE_COLOR=pygame.Color(255,48,48)

#TILE OUTLINE
TILE_COLOR=pygame.Color(11, 11, 11)

#uses DFS algo
class Game_level_solver():
    def __init__(self, app, wall_pos,begin_x_pos, begin_y_pos, end_destination_x, end_destination_y):
        self.app = app
        self.begin_x_pos = begin_x_pos
        self.begin_y_pos = begin_y_pos
        self.end_destination_x = end_destination_x
        self.end_destination_y = end_destination_y
        self.wall_pos = wall_pos
        self.visited_list = [(self.begin_x_pos, self.begin_y_pos)]
        self.route = None
        self.route_if_found = False

    def draw_all_paths(self, i, j):
        ##### Draw each node the computer is visiting as it is searching SIMULTNEOUSLY
        pygame.draw.rect(self.app.screen, CURRENT_NODE_COLOR, (i * 24 + 240, j * 24, 24, 24), 0)

        ##### Redraw start and end nodes on top of all routes
        pygame.draw.rect(self.app.screen, START_NODE_ONE_COLOR,
                         (240 + self.begin_x_pos * 24, self.begin_y_pos * 24, 24, 24), 0)
        pygame.draw.rect(self.app.screen, START_NODE_TWO_COLOR,
                         (240 + self.end_destination_x * 24, self.end_destination_y * 24, 24, 24), 0)

        # use variable for setting grids would be helpful
        for x in range(52):
            pygame.draw.line(self.app.screen, TILE_COLOR, (260 + x * 24, 20), (260 + x * 24, 740))
        for y in range(30):
            pygame.draw.line(self.app.screen, TILE_COLOR, (260, 20 + y * 24), (1500, 20 + y * 24))

        pygame.display.update()

    def if_valid_move(self, move):
        if move not in self.wall_pos and move not in self.visited_list:
            self.visited_list.append(move)
            return True
        return False

    def if_end(self, first_in):
        if first_in == (self.end_destination_x, self.end_destination_y):
            return True
        return False

    def run_game_level_solver(self):
        stack = []
        #tuple
        first_in = (self.begin_x_pos, self.begin_y_pos)
        stack.append(first_in)

        moves_stack = []
        moves_first_in = ''
        moves_stack.append(moves_first_in)

        while len(stack) > 0:
            last_out = stack.pop()
            moves_last_out = moves_stack.pop()

            for move_direction in ['L', 'R', 'U', 'D']:
                horizontal_move, vertical_move = last_out
                if move_direction == 'L':
                    horizontal_move -= 1
                elif move_direction == 'R':
                    horizontal_move += 1
                elif move_direction == 'U':
                    vertical_move -= 1
                elif move_direction == 'D':
                    vertical_move += 1

                move_update = moves_last_out + move_direction
                #x and y co-ords
                if self.if_end((horizontal_move, vertical_move)):
                    self.route = move_update
                    self.route_if_found = True
                    break

                if self.if_valid_move((horizontal_move, vertical_move)):
                    stack.append((horizontal_move, vertical_move))
                    moves_stack.append(move_update)
                    self.draw_all_paths(horizontal_move, vertical_move)

            if self.route_if_found:
                break





