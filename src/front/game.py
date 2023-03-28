import pygame
from src.front.ui import ProcessingStartMenu


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Maze Enjoyer')
        ProcessingStartMenu()
