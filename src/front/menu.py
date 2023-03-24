"""File contains menu"""

import pygame
import pygame_menu
from src.back.constants import *
from src.front.main_loop import ProcessingLoop


def ProcessingMenu():
    pygame.init()
    display = pygame.display.set_mode((SIZE_OF_DISPLAY[0], SIZE_OF_DISPLAY[1]))

    menu = pygame_menu.Menu('Welcome', 400, 300,
                            theme=pygame_menu.themes.THEME_BLUE)

    def start_the_game():
        ProcessingLoop(display)

    menu.add.text_input('Name :', default='John Doe')
    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(display)
