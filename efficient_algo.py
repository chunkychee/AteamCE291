#this is the algo
#
# for efficient solver
import pygame

#SETTING START AND END NODES TO RED
START_NODE_ONE_COLOR=pygame.Color(255, 87, 87)
#SETTING START AND END NODES TO BLUE
START_NODE_TWO_COLOR=pygame.Color(0,74,173)

#SETTING CURRENT NODE
CURRENT_NODE_COLOR=pygame.Color(255,48,48)

#TILE OUTLINE
TILE_COLOR=pygame.Color(11, 11, 11)

class Node:
    def __init__(self, position = None, parent = None):
        self.position = position
        self.parent = parent
        self.G = 0
        self.H = 0
        self.F = 0

#uses AStar Algo
class Efficient_algo():
    #start_node and end node
    def __init__(self, app, wall_pos, begin_x_pos, begin_y_pos, end_destination_x, end_destination_y):
        self.app = app
        self.begin_x_pos = begin_x_pos
        self.begin_y_pos = begin_y_pos
        self.end_destination_x = end_destination_x
        self.end_destination_y = end_destination_y
        self.grids_to_visit_list = []
        self.grids_visited_list = []
        self.wall_pos = wall_pos
        self.route = []
        self.route_if_found = False

    def draw_all_paths(self, current):
        i, j = current

        ##### Draw each node the computer is visiting as it is searching SIMULTNEOUSLY
        pygame.draw.rect(self.app.screen, CURRENT_NODE_COLOR, (i * 24 + 240, j * 24, 24, 24), 0)

        ##### Redraw start/end nodes on top of all routes
        pygame.draw.rect(self.app.screen, START_NODE_ONE_COLOR, (240 + self.begin_x_pos * 24, self.begin_y_pos * 24, 24, 24), 0)
        pygame.draw.rect(self.app.screen, START_NODE_TWO_COLOR, (240 + self.end_destination_x * 24, self.end_destination_y * 24, 24, 24), 0)

        #use variable for setting grids would be helpful
        for x in range(52):
            pygame.draw.line(self.app.screen, TILE_COLOR, (260 + x * 24, 20), (260 + x * 24,740 ))
        for y in range(30):
            pygame.draw.line(self.app.screen, TILE_COLOR, (260, 20 + y * 24), (1500, 20 + y * 24))

        pygame.display.update()

    def get_children_node(self, parent, end_node):
        print('generating children')
        parent_pos = parent.position
        for m in [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]:
            child_pos = (parent_pos[0] + m[0], parent_pos[1] + m[1])
            if self.if_valid_move(child_pos):
                child = Node(child_pos, parent)
                self.g_calculator(child, parent, m)
                self.h_calculator(child, end_node)
                self.f_calculator(child)

                # If node not already added to the open list AND node isn't cutting corners around wall, then append
                if self.append_to_grids_to_visit(child) and self.check_wall_corner(m, parent_pos):
                    self.grids_to_visit_list.append(child)

    def append_to_grids_to_visit(self, child):
        for open_node in self.grids_to_visit_list:

            # If node is already in open list and the new node has a higher F-score than node about to be replaced,
            # return False
            # IMPORTANT NOTE: Even if another node with same position with different F value gets added, the node with
            # higher F-score will never be checked, so it's fine to have two nodes with same position.
            if child.position == open_node.position and child.F >= open_node.F:
                return False
        return True

    def check_wall_corner(self, move, parent_pos):
        if move == (-1, 1) or move == (1, 1) or move == (1, -1) or move == (-1, -1):
            i,j = parent_pos
            (m,n) = move
            # (x, y) = Orthogonal
            if move == (1,1):
                (x,y) = (0,1)
                (a,b) = (1,0)
            elif move == (1,-1):
                (x,y) = (1,0)
                (a, b) = (0,-1)
            elif move == (-1,-1):
                (x,y) = (0,-1)
                (a, b) = (-1,0)
            else:
                (x,y) = (-1,0)
                (a, b) = (0,1)

            # If cutting corner case, return False
            if (i+x, j+y) in self.wall_pos or (i+a, i+b) in self. wall_pos and (i+m, j+n) not in self.wall_pos:
                return False
            return True
        else:
            return True
    #cost of travel from start to n = g
    def g_calculator(self, child, parent, m):
        # Determine if move is orthogonal or diagonal
        sum_difference = abs(sum(m))
        # Add G-Score according to the type of move
        if sum_difference == 1:
            child.G = parent.G + 10
        elif sum_difference == 0 or sum_difference == 2:
            child.G = parent.G + 14
    #cost of travel from n to target =h
    def h_calculator(self, child, end_node):
        child.H = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
    # total cost of travel
    def f_calculatot(self, child):
        child.F = child.G + child.H

    def if_valid_move(self, move):
        if move not in self.wall_pos and move not in self.grids_visited_list:
            return True
        return False

    def if_end(self, current):
        if current == (self.end_destination_x, self.end_destination_y):
            return True
        return False

    # run efficient algo
    def run_efficient_algo(self):
        # Initialize Start/End Nodes
        start_node = Node((self.begin_x_pos, self.begin_y_pos), None)
        start_node.G = start_node.H = start_node.F = 0
        end_node = Node((self.end_destination_x, self.end_destination_y), None)
        end_node.G = end_node.H = end_node.F = 0

        self.grids_to_visit_list.append(start_node)

        print(start_node.position)
        print(end_node.position)

        while len(self.grids_to_visit_list) > 0:
            current_node = self.grids_to_visit_list[0]
            current_index = 0

            # Get the node with lowest F-Cost
            for index, node in enumerate(self.grids_to_visit_list):
                if node.F < current_node.F:
                    current_node = node
                    current_index = index

            # Check if route has been found
            if self.if_end(current_node.position):
                current = current_node
                # Append path until the current node becomes none (start node has a parent of None)
                while current is not None:
                    self.route.append(current.position)
                    current = current.parent
                self.route.pop(0)
                self.route_if_found = True
                break

            self.get_children_node(current_node, end_node)
            self.draw_all_paths(current_node.position)

            self.grids_to_visit_list.pop(current_index)
            self.grids_visited_list.append(current_node.position)
