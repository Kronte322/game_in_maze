"""File contains initialization of the game"""

import pygame
from src.front.ui import MenuUI
from src.back.constants import *


class Game:
    """this class for start the game"""

    def __init__(self):
        """initialization of the object"""

        pygame.init()
        pygame.display.set_caption(CAPTION)
        MenuUI.ProcessingStartMenu()
