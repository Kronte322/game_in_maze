"""File contains class that process all events"""

import pygame
import src.front.Menus
import src.back.Config
from src.back.Config import *


class EventDistributor:
    """class that control all events"""

    def __init__(self, player, mappa, ui):
        """initialization of the class"""

        self.player = player
        self.mappa = mappa
        self.ui = ui

    def ProcessKeys(self):
        """this function processing keyboards events"""

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            src.back.Config.STATE = IN_GAME_MENU_STATE
            src.front.Menus.MenuUI.InGameMenu()
        if keys[pygame.K_w]:
            self.player.MoveUp(self.mappa)
        if keys[pygame.K_a]:
            self.player.MoveLeft(self.mappa)
        if keys[pygame.K_s]:
            self.player.MoveDown(self.mappa)
        if keys[pygame.K_d]:
            self.player.MoveRight(self.mappa)

    def ProcessEvents(self):
        """this function window events"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                src.back.Config.RUNNING = False
            self.ui.ProcessEvents(event, self.mappa)
