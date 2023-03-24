"""File contains main game loop"""

import sys
import pygame
import pygame_gui
from src.back.in_game_ui import Ui
from src.back.constants import *
from src.back import class_map
from src.back import class_player


def ProcessingLoop(screen, resume=False):
    """that function performs main game loop"""

    sys.setrecursionlimit(DEEP_OF_RECURSION)

    mappa = class_map.Map()
    player = class_player.Player()

    clock = pygame.time.Clock()

    mappa.SpawnPosition()

    ui = Ui()

    running = True
    while running:
        time_delta = clock.tick(FRAMES_PER_SEC)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            ui.ProcessEvents(event)

        player.move(mappa)

        screen.fill(COLOR_FOR_BACKGROUND)

        mappa.SetCurrentRoom(player.GetPosition())
        mappa.Render(screen)

        player.render(screen)

        ui.Blit(time_delta, screen=screen)

        pygame.display.flip()

    pygame.quit()
