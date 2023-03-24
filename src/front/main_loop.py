"""File contains main game loop"""

import sys
import pygame
from src.back.constants import *
from src.back import class_map
from src.back import class_player


def ProcessingLoop(screen):
    sys.setrecursionlimit(DEEP_OF_RECURSION)

    mappa = class_map.Map()
    player = class_player.Player()

    clock = pygame.time.Clock()

    mappa.SpawnPosition()

    running = True
    while running:
        clock.tick(FRAMES_PER_SEC)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.move(mappa)

        screen.fill(COLOR_FOR_BACKGROUND)

        mappa.SetCurrentRoom(player.GetPosition())
        mappa.Render(screen)
        player.render(screen)

        pygame.display.flip()

    pygame.quit()
