"""File contains constants"""

# chars for map
CHAR_FOR_PATH = 'P'
CHAR_FOR_EMPTY = 'E'
CHAR_FOR_BOARD = 'B'
CHAR_FOR_FLOOR = '-'
CHAR_FOR_CURRENT_POS = 'C'
CHAR_FOR_EXIT = 'X'

# sizes of rectangles
SIZE_OF_DISPLAY = [1920, 1000]
SIZE_OF_MOVE_BOX = [600, 300]
SIZE_OF_UNSCOPED_MINIMAP = [300, 300]
SIZE_OF_SCOPED_MINIMAP = [600, 600]
SIZE_OF_MINIMAP = SIZE_OF_UNSCOPED_MINIMAP
SIZE_OF_MAP = (16, 16)

# sizes of tiles
SIZE_OF_CHARACTER = 48
SIZE_OF_TILE = 72

# positions
POSITION_OF_MINIMAP = [SIZE_OF_DISPLAY[0] - SIZE_OF_MINIMAP[0], 0]

# character characteristic
SPEED_OF_CHARACTER = 7
SPAWN_POSITION = [SIZE_OF_DISPLAY[0] // 2, SIZE_OF_DISPLAY[1] // 2]

# path to pngs
PATH_TO_CHARACTER_PNG = "../tile_sets/tiles_for_chars/sprite_0.png"
PATH_TO_FLOOR_PNG = "../tile_sets/tiles_for_map/floor/sprite_"
PATH_TO_EMPTY_TILE_PNG = "../tile_sets/tiles_for_map/back_ground/sprite_078.png"
PATH_TO_EXIT_PNG = "../tile_sets/tiles_for_map/exit/sprite_038.png"

# specific colors
COLOR_FOR_BACKGROUND = (37, 19, 26)
COLOR_FOR_CURRENT_POSITION = (51, 255, 0)

# specific constants
LENGTH_OF_PATHS = 4
FRAMES_PER_SEC = 60
DEEP_OF_RECURSION = 10000000
NUM_OF_PNGS_FOR_FLOOR = 14
