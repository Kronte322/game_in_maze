"""File contains menu"""

import pygame
import pygame_menu
from src.back.constants import *
import src.back.constants
import src.front.main_loop

display = pygame.display.set_mode((SIZE_OF_DISPLAY[0], SIZE_OF_DISPLAY[1]))


def StartTheGame():
    """function that performs start of the game"""

    pygame.init()
    pygame.display.set_caption('Maze Enjoyer')
    ProcessingStartMenu()


def start_the_game():
    """function for start game button in menu"""

    src.front.main_loop.ProcessingLoop(display)


def ProcessingStartMenu():
    """this function perform start menu"""

    start_menu = pygame_menu.Menu('Welcome', 400, 300,
                                  theme=pygame_menu.themes.THEME_BLUE)

    start_menu.add.button('Play', start_the_game)
    start_menu.add.button('Settings', SettingsMenu)
    start_menu.add.button('Quit', pygame_menu.events.EXIT)
    start_menu.mainloop(display)


def retry_the_game():
    """function for retry game button in menu"""

    src.back.constants.DIFFICULTY = 1
    src.back.constants.ALGO_FOR_GENERATION = 'DFS'
    src.back.constants.SIZE_OF_MAP = [16, 16]
    ProcessingStartMenu()


def ProcessingEndMenu():
    """this function perform end menu"""

    end_menu = pygame_menu.Menu('You Won', 600, 300,
                                theme=pygame_menu.themes.THEME_BLUE)
    end_menu.add.button('Retry', retry_the_game)
    end_menu.add.button('Quit', pygame_menu.events.EXIT)
    end_menu.mainloop(display)


def SetDifficulty():
    """make difficulty futures alive"""

    if src.back.constants.DIFFICULTY == 1:
        src.back.constants.LENGTH_OF_PATHS = 7
    elif src.back.constants.DIFFICULTY == 2:
        src.back.constants.LENGTH_OF_PATHS = 4
    elif src.back.constants.DIFFICULTY == 3:
        src.back.constants.LENGTH_OF_PATHS = 4
    elif src.back.constants.DIFFICULTY in [4, 5]:
        src.back.constants.LENGTH_OF_PATHS = 1


def set_difficulty(value, difficult):
    """functions for set difficulty button in menu"""

    src.back.constants.DIFFICULTY = difficult
    SetDifficulty()


def set_algorithm(value, num):
    """functions for set type of algorithm button in menu"""

    src.back.constants.ALGO_FOR_GENERATION = value[0][0]


def set_size(value, num):
    """functions for size button in menu"""

    src.back.constants.SIZE_OF_MAP = num


def SettingsMenu():
    """this function perform settings menu"""

    settings_menu = pygame_menu.Menu('Settings', 600, 300,
                                     theme=pygame_menu.themes.THEME_BLUE)
    settings_menu.add.button('Back', ProcessingStartMenu)
    settings_menu.add.selector('Difficulty:', SET_WITH_DIFFICULTIES, onchange=set_difficulty)
    settings_menu.add.selector('Size:', SET_WITH_SIZES, onchange=set_size)
    settings_menu.add.selector('Algorithm for generator:', SET_WITH_ALGOS, onchange=set_algorithm)
    settings_menu.mainloop(display)


def InGameMenu():
    """this function perform in-game menu"""

    in_game_menu = pygame_menu.Menu('Menu', 600, 300,
                                    theme=pygame_menu.themes.THEME_BLUE)
    in_game_menu.add.button('Resume', in_game_menu.disable)
    in_game_menu.add.button('Retry', retry_the_game)
    in_game_menu.add.button('Quit', pygame_menu.events.EXIT)
    in_game_menu.mainloop(display)

