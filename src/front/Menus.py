"""File contains menu"""

import pygame
import pygame_menu
import pickle
from src.back.Config import *
import src.back.Config
import src.front.MainLoop
import os
from src.back.PackObjects import MapForPack, PlayerForPack

display = pygame.display.set_mode((SIZE_OF_DISPLAY[0], SIZE_OF_DISPLAY[1]))


class MenuUI:
    """class that contains all menus UI"""

    name_of_save = DEFAULT_NAME_FOR_SAVE
    name_of_load = None
    if len(os.listdir(PATH_TO_SAVED_MAZES)) != 0:
        name_of_load = os.listdir(PATH_TO_SAVED_MAZES)[0]

    list_with_saves = [(name, name) for name in os.listdir(PATH_TO_SAVED_MAZES)]

    @staticmethod
    def SetDifficultyFromMenu(key, value):
        """functions for set difficulty button in menu"""

        src.back.Config.DIFFICULTY = value
        MenuUI.SetDifficulty()

    @staticmethod
    def StartTheGame():
        """function for start game button in menu"""

        src.back.Config.STATE = IN_GAME_STATE
        src.front.MainLoop.ProcessingLoop(display)

    @staticmethod
    def SetDifficulty():
        """make difficulty futures alive"""

        src.back.Config.LENGTH_OF_PATHS = LENGTHS_PATHS_ACCORDING_TO_DIFFICULTY[src.back.Config.DIFFICULTY]

    @staticmethod
    def RetryTheGame():
        """function for retry game button in menu"""

        src.back.Config.MAPPA = MAPPA
        src.back.Config.PLAYER = PLAYER
        src.back.Config.CHARACTER = CHARACTER
        src.back.Config.DIFFICULTY = DIFFICULTY
        src.back.Config.ALGO_FOR_GENERATION = DFS
        src.back.Config.SIZE_OF_MAP = SIZE_OF_MAP
        src.back.Config.STATE = START_MENU_STATE
        MenuUI.ProcessingStartMenu()

    @staticmethod
    def SetAlgorithm(key, value):
        """functions for set type of algorithm button in menu"""

        src.back.Config.ALGO_FOR_GENERATION = value

    @staticmethod
    def SetSize(key, value):
        """functions for size button in menu"""

        src.back.Config.SIZE_OF_MAP = value

    @staticmethod
    def SetCharacter(key, value):
        """function for character selection"""

        src.back.Config.CHARACTER = value

    @staticmethod
    def ProcessingStartMenu():
        """this function perform start menu"""
        src.back.Config.STATE = START_MENU_STATE
        start_menu = pygame_menu.Menu(WELCOME_CONDITION_STRING, SIZE_OF_MENUS[0], SIZE_OF_MENUS[1],
                                      theme=pygame_menu.themes.THEME_BLUE)
        start_menu.add.button(PLAY_CONDITION_STRING, MenuUI.StartTheGame)
        start_menu.add.selector(CHARACTER_SELECTION_STRING, SET_WITH_CHARACTERS, onchange=MenuUI.SetCharacter)
        start_menu.add.button(LOAD_STRING, MenuUI.ProcessingLoadMenu)
        start_menu.add.button(SETTINGS_CONDITION_STRING, MenuUI.SettingsMenu)
        start_menu.add.button(QUIT_CONDITION_STRING, pygame_menu.events.EXIT)

        start_menu.mainloop(display)

    @staticmethod
    def SetNameOfLoad(key, value):
        """this function set name of loading file"""

        MenuUI.name_of_load = value

    @staticmethod
    def ProcessingLoadMenu():
        """this function performs load menu"""

        load_menu = pygame_menu.Menu(LOAD_STRING, SIZE_OF_MENUS[0], SIZE_OF_MENUS[1],
                                     theme=pygame_menu.themes.THEME_BLUE)

        def LoadFile():
            """this function load saved session"""

            with open(PATH_TO_SAVED_MAZES + MenuUI.name_of_load, 'rb') as file:
                src.back.Config.MAPPA = pickle.load(file).UnPack()
                src.back.Config.PLAYER = pickle.load(file).UnPack()
                first_test = src.back.Config.MAPPA
                second_test = src.back.Config.PLAYER
            load_menu.disable()

        load_menu.add.button(BACK_CONDITION_STRING, load_menu.disable)
        load_menu.add.selector(CHOOSE_FILE_STRING, MenuUI.list_with_saves, onchange=MenuUI.SetNameOfLoad)
        load_menu.add.button(LOAD_STRING, LoadFile)
        load_menu.mainloop(display)

    @staticmethod
    def ProcessingEndMenu():
        """this function perform end menu"""

        src.back.Config.STATE = END_GAME_MENU_STATE
        end_menu = pygame_menu.Menu(WIN_CONDITION_STRING, SIZE_OF_MENUS[0], SIZE_OF_MENUS[1],
                                    theme=pygame_menu.themes.THEME_BLUE)
        end_menu.add.button(RETRY_CONDITION_STRING, MenuUI.RetryTheGame)
        end_menu.add.button(QUIT_CONDITION_STRING, pygame_menu.events.EXIT)
        end_menu.mainloop(display)

    @staticmethod
    def SettingsMenu():
        """this function perform settings menu"""

        settings_menu = pygame_menu.Menu(SETTINGS_CONDITION_STRING, SIZE_OF_MENUS[0], SIZE_OF_MENUS[1],
                                         theme=pygame_menu.themes.THEME_BLUE)
        settings_menu.add.button(BACK_CONDITION_STRING, MenuUI.ProcessingStartMenu)
        settings_menu.add.selector(DIFFICULTY_SELECTION_STRING, SET_WITH_DIFFICULTIES,
                                   onchange=MenuUI.SetDifficultyFromMenu)
        settings_menu.add.selector(SIZE_SELECTION_STRING, SET_WITH_SIZES, onchange=MenuUI.SetSize)
        settings_menu.add.selector(ALGORITHM_CONDITION_STRING, SET_WITH_ALGOS, onchange=MenuUI.SetAlgorithm)
        settings_menu.mainloop(display)

    @staticmethod
    def InGameMenu():
        """this function perform in-game menu"""

        src.back.Config.STATE = IN_GAME_MENU_STATE

        in_game_menu = pygame_menu.Menu(MENU_CONDITION_STRING, SIZE_OF_MENUS[0], SIZE_OF_MENUS[1],
                                        theme=pygame_menu.themes.THEME_BLUE)

        def MyDisable():
            src.back.Config.STATE = IN_GAME_STATE
            in_game_menu.disable()

        in_game_menu.add.button(RESUME_CONDITION_STRING, MyDisable)
        in_game_menu.add.button(SAVE_MAZE_STRING, MenuUI.SaveMazeMenu)
        in_game_menu.add.button(RETRY_CONDITION_STRING, MenuUI.RetryTheGame)
        in_game_menu.add.button(QUIT_CONDITION_STRING, pygame_menu.events.EXIT)
        in_game_menu.mainloop(display)

    @staticmethod
    def SetNameOfSave(string):
        """this function set name of save"""

        MenuUI.name_of_save = string

    @staticmethod
    def SaveMazeMenu():
        """this function performs save menu"""

        save_menu = pygame_menu.Menu(SAVE_MAZE_STRING, SIZE_OF_MENUS[0], SIZE_OF_MENUS[1],
                                     theme=pygame_menu.themes.THEME_BLUE)

        def SaveFile():
            """this function save session into file"""

            with open(PATH_TO_SAVED_MAZES + MenuUI.name_of_save, 'wb') as file:
                pickle.dump(MapForPack(src.back.Config.MAPPA), file, protocol=pickle.HIGHEST_PROTOCOL)
                pickle.dump(PlayerForPack(src.back.Config.PLAYER), file, protocol=pickle.HIGHEST_PROTOCOL)
            save_menu.disable()

        save_menu.add.button(BACK_CONDITION_STRING, save_menu.disable)
        save_menu.add.text_input(NAME_MAZE_STRING, maxwidth=MAX_SIZE_OF_NAME_OF_FILE, default=MenuUI.name_of_save,
                                 onchange=MenuUI.SetNameOfSave)
        save_menu.add.button(SAVE_MAZE_STRING, SaveFile)
        save_menu.mainloop(display)
