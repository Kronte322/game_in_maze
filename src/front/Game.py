"""File contains initialization of the game"""

import pygame
from src.front.Menus import MenuUI
from src.back.Config import *


class Game:
    """this class for start the game"""

    def __init__(self):
        """initialization of the object"""

        pygame.init()
        pygame.display.set_caption(CAPTION)
        MenuUI.ProcessingStartMenu()
