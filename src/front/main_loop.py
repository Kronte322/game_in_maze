"""File contains main game loop"""

import sys
import pygame
import src.back.constants
from src.back.in_game_ui import Ui
from src.back.constants import *
from src.back import class_map
from src.back import class_player
from src.back.event_distributor import EventDistributor


def ProcessingLoop(screen):
    """this function performs main game loop"""

    # over 30 row but its main loop ().()
    sys.setrecursionlimit(DEEP_OF_RECURSION)

    if src.back.constants.DIFFICULTY == 5:
        src.back.constants.SIZE_OF_MAP = SET_WITH_SIZES[3][1]

    mappa = None
    player = None

    if src.back.constants.MAPPA is None:
        mappa = class_map.Map()
        player = class_player.Player()
        mappa.SpawnPosition()
        src.back.constants.MAPPA = mappa
        src.back.constants.PLAYER = player

    else:
        mappa = src.back.constants.MAPPA
        player = src.back.constants.PLAYER

    ui = Ui()
    event_distributor = EventDistributor(player, mappa, ui)

    clock = pygame.time.Clock()

    while src.back.constants.RUNNING:
        time_delta = clock.tick(FRAMES_PER_SEC)

        event_distributor.ProcessEvents()
        event_distributor.ProcessKeys()

        screen.fill(COLOR_FOR_BACKGROUND)

        mappa.SetCurrentRoom(player.GetPosition())
        mappa.Render(screen)

        player.Render(screen)

        ui.Blit(time_delta, screen=screen)

        pygame.display.flip()

    pygame.quit()
