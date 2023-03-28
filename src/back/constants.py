"""File contains constants"""

# chars for map
CHAR_FOR_PATH = 'P'
CHAR_FOR_EMPTY = 'E'
CHAR_FOR_BOARD = 'B'
CHAR_FOR_FLOOR = '-'
CHAR_FOR_CURRENT_POS = 'C'
CHAR_FOR_EXIT = 'X'
CHAR_FOR_ANSWER = 'A'

# sizes of rectangles
SIZE_OF_DISPLAY = [1920, 1000]
SIZE_OF_MOVE_BOX = [600, 300]
SIZE_OF_UNSCOPED_MINIMAP = [450, 450]
SIZE_OF_SCOPED_MINIMAP = [600, 600]
SIZE_OF_MINIMAP = SIZE_OF_UNSCOPED_MINIMAP
SIZE_OF_MAP = [16, 16]

# sizes of tiles
SIZE_OF_CHARACTER = 48
SIZE_OF_TILE = 72

# positions
POSITION_OF_MINIMAP = [SIZE_OF_DISPLAY[0] - SIZE_OF_MINIMAP[0], 0]

# character characteristic
SPEED_OF_CHARACTER = 7
SPAWN_POSITION = [SIZE_OF_DISPLAY[0] // 2, SIZE_OF_DISPLAY[1] // 2]

# path to pngs
PATH_TO_CHARACTER_PNG = "images/tiles_for_chars/"
PATH_TO_FLOOR_PNG = "images/tiles_for_map/floor/sprite_"
PATH_TO_EMPTY_TILE_PNG = "images/tiles_for_map/back_ground/sprite_078.png"
PATH_TO_EXIT_PNG = "images/tiles_for_map/exit/sprite_038.png"

# specific colors
COLOR_FOR_BACKGROUND = (37, 19, 26)
COLOR_FOR_CURRENT_POSITION = (51, 255, 0)
COLOR_FOR_ANSWER_TILES = (255, 255, 0)

# specific constants
LENGTH_OF_PATHS = 4
FRAMES_PER_SEC = 60
DEEP_OF_RECURSION = 10000000
NUM_OF_PNGS_FOR_FLOOR = 14

# preferences for menus
SET_WITH_DIFFICULTIES = [('I’m Too Young to Die', 1), ('Hurt Me Plenty', 2), ('Ultra Violence', 3), ('Nightmare', 4),
                         ('Just A Psycho', 5)]
SET_WITH_ALGOS = [('DFS', 'DFS'), ('Prima', 'Prima')]
SET_WITH_SIZES = [('Tiny [16, 16]', [16, 16]), ('Classic [32, 32]', [32, 32]), ('Large [64, 64]', [64, 64]),
                  ('Huge [128, 128]', [128, 128])]
SET_WITH_CHARACTERS = [('Necromancer', 'necromancer'), ('Knight', 'knight'), ('Priest', 'priest'),
                       ('Skeleton', 'skeleton'), ('Spirit', 'spirit')]

# cases
DIFFICULTY = 1
CHARACTER = 'necromancer'
ALGO_FOR_GENERATION = 'DFS'

# places for in-game ui
SIZE_OF_SETTINGS_BUTTON = [100, 50]
PLACE_OF_SETTINGS_BUTTON = [10, 10]

SIZE_OF_SHOW_ANSWER_BUTTON = [160, 50]
PLACE_OF_SHOW_ANSWER_BUTTON = [SIZE_OF_DISPLAY[0] // 2 - SIZE_OF_SHOW_ANSWER_BUTTON[0] // 2, 10]
