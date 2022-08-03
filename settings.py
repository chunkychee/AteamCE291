
# ----- Colors Settings ----- #
LIGHT_GRAY = "#FAFAFA"  # Background
DARK_BLUE = "#004AAD"  # Title & Starting Square
BLACK = "#0B0B0B"  # all dark color text
BLUE = "#0357C8"  # buttons
GRAY = "#797979"  # Home Button in Maze Generator & Smart Solver
LIGHT_BLUE = "#5CE1E6"  # Explored Path
RED = "#FF1616"  # Smart Solver Title
LIGHT_RED = "#FF5757"  # Smart Solver Button
YELLOW = "#FFDE59"  # Solution Path
WHITE = (255, 255, 255)

MAZE_COLOR = {0: WHITE, 1: GRAY, 2: DARK_BLUE, 3:LIGHT_RED}  # color of the maze tiles, 0: path, 1: wall, 2: start, 3: goal


# ----- Screen Settings ----- #
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 680
BACKGROUND_COLOR = LIGHT_GRAY


# ----- Fonts Settings ----- #
DEFAULT_FONT = None  # for example "Arial Black"
DEFAULT_FONT_SIZE = 24
DEFAULT_TEXT_COLOR = BLACK


# ----- Buttons Settings ----- #
DEFAULT_BUTTON_SIZE = (206, 45)  # default width and height of the buttons
DEFAULT_BUTTON_COLOR = BLUE
DEFAULT_ROUNDED_CORNER = 12  # default rounded corners value (0 to deactivate)
DEFAULT_OUTLINE_RADIUS = 2  # will make an outline of X px when the mouse is over the button
DEFAULT_OUTLINE_COLOR = GRAY
DEFAULT_BUTTON_TEXT_COLOR = LIGHT_GRAY
DEFAULT_BUTTON_FONT = DEFAULT_FONT
DEFAULT_BUTTON_FONT_SIZE = 28
DEFAULT_BUTTON_ZOOM_FACTOR = 2  # will make the button text bigger when the mouse is over the button (0 or False to deactivate)


# ----- Maze Generator Settings -----#
PANEL_WIDTH = 280  # width of the panel which contains the stats and buttons

