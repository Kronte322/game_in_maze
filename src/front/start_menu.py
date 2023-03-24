"""File contains menu"""

import pygame
import pygame_menu
from src.back.constants import *
import src.front.main_loop

display = pygame.display.set_mode((SIZE_OF_DISPLAY[0], SIZE_OF_DISPLAY[1]))


def ProcessingStartMenu():
    pygame.init()

    start_menu = pygame_menu.Menu('Welcome', 400, 300,
                                  theme=pygame_menu.themes.THEME_BLUE)

    def start_the_game():
        src.front.main_loop.ProcessingLoop(display)

    start_menu.add.text_input('Name :', default='John Doe')
    start_menu.add.button('Play', start_the_game)
    start_menu.add.button('Quit', pygame_menu.events.EXIT)
    start_menu.mainloop(display)


def ProcessingEndMenu():
    end_menu = pygame_menu.Menu('You Won', 400, 300,
                                theme=pygame_menu.themes.THEME_BLUE)

    def retry_the_game():
        src.front.main_loop.ProcessingLoop(display)

    end_menu.add.button('Retry', retry_the_game)
    end_menu.add.button('Quit', pygame_menu.events.EXIT)
    end_menu.mainloop(display)
