"""File contains map class"""

import pygame
import random
import time
import sys
from src.back.map_generator import *
from src.back.constants import *
import src.back.constants
import src.front.ui

random.seed(time.time())
# random.seed(12)

list_with_floor = []

image_for_empty = pygame.image.load(PATH_TO_EMPTY_TILE_PNG)
image_for_empty = pygame.transform.scale(image_for_empty, (SIZE_OF_TILE, SIZE_OF_TILE))

image_for_exit = pygame.image.load(PATH_TO_EXIT_PNG)
image_for_exit = pygame.transform.scale(image_for_exit, (SIZE_OF_TILE, SIZE_OF_TILE))

generated_floor = {}


def SetImage(path, number):
    result = pygame.image.load(path + str(number) + ".png")
    result = pygame.transform.scale(result, (SIZE_OF_TILE, SIZE_OF_TILE))
    return result


def SetTiles():
    for i in range(1, NUM_OF_PNGS_FOR_FLOOR + 1):
        list_with_floor.append(SetImage(PATH_TO_FLOOR_PNG, i))


class Map:
    def __init__(self):
        SetTiles()

        if src.back.constants.DIFFICULTY == 5:
            src.back.constants.SIZE_OF_MAP = [128, 128]

        self.matrix_with_map = MapGenerator.GenerateMaze(src.back.constants.SIZE_OF_MAP).copy()
        self.mappa = pygame.Surface(
            (len(self.matrix_with_map) * SIZE_OF_TILE, len(self.matrix_with_map[0]) * SIZE_OF_TILE))

        self.tiles_for_current_room = {}
        self.current_room = pygame.Surface((0, 0))

        self.visited_tiles = {}
        self.visited_mappa = pygame.Surface(
            (len(self.matrix_with_map) * SIZE_OF_TILE, len(self.matrix_with_map[0]) * SIZE_OF_TILE))
        self.matrix_with_visited = MapGenerator.GetClearMap(src.back.constants.SIZE_OF_MAP).copy()

        self.global_map_position = [0, 0]
        self.current_room_position = [0, 0]

        self.dfs = DFSAlgo()

        self.SetTilesOnMatrix(self.mappa, self.matrix_with_map, (0, 0))

    def BlitSpecificMap(self, list_with_map):
        left_upper_corner = (
            min(list_with_map, key=lambda item: item[0][0])[0][0],
            min(list_with_map, key=lambda item: item[0][1])[0][1])
        right_down_corner = (
            max(list_with_map, key=lambda item: item[0][0])[0][0],
            max(list_with_map, key=lambda item: item[0][1])[0][1])
        width = right_down_corner[0] - left_upper_corner[0] + 1
        height = right_down_corner[1] - left_upper_corner[1] + 1
        self.current_room = pygame.Surface((width * SIZE_OF_TILE, height * SIZE_OF_TILE))
        matrix_with_map = []
        for i in range(width):
            intermediate = []
            for j in range(height):
                intermediate.append(CHAR_FOR_EMPTY)
            matrix_with_map.append(intermediate)

        for i in list_with_map:
            matrix_with_map[i[0][0] - left_upper_corner[0]][i[0][1] - left_upper_corner[1]] = i[1]
        self.SetTilesOnMatrix(self.current_room, matrix_with_map, left_upper_corner)
        return left_upper_corner

    @staticmethod
    def SetTilesOnMatrix(surface, matrix, left_corner):
        x, y = 0, 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] in [CHAR_FOR_PATH]:
                    if (i + left_corner[0], j + left_corner[1]) in generated_floor:
                        surface.blit(generated_floor[(i + left_corner[0], j + left_corner[1])], (x, y))
                    else:
                        generated_floor[(i + left_corner[0], j + left_corner[1])] = random.choice(list_with_floor)
                        surface.blit(generated_floor[(i + left_corner[0], j + left_corner[1])], (x, y))
                elif matrix[i][j] in [CHAR_FOR_EXIT]:
                    surface.blit(image_for_exit, (x, y))
                else:
                    surface.blit(image_for_empty, (x, y))
                y += SIZE_OF_TILE
            x += SIZE_OF_TILE
            y = 0

    @staticmethod
    def SetSpecificOnMatrix(matrix, list_of_tiles):
        for i in list_of_tiles:
            matrix[i[0][0]][i[0][1]] = i[1]

    @staticmethod
    def BlitSpecificOnMap(surface, list_of_tiles):
        for i in list_of_tiles:
            x = SIZE_OF_TILE * i[0][0]
            y = SIZE_OF_TILE * i[0][1]
            if i[1] in [CHAR_FOR_PATH]:
                if (i[0][0], i[0][1]) in generated_floor:
                    surface.blit(generated_floor[(i[0][0], i[0][1])], (x, y))
                else:
                    generated_floor[(i[0][0], i[0][1])] = random.choice(list_with_floor)
                    surface.blit(generated_floor[(i[0][0], i[0][1])], (x, y))
            if i[1] in [CHAR_FOR_CURRENT_POS]:
                pygame.draw.rect(surface, color=COLOR_FOR_CURRENT_POSITION, rect=[x, y, SIZE_OF_TILE, SIZE_OF_TILE])
            elif i[1] in [CHAR_FOR_EXIT]:
                surface.blit(image_for_exit, (x, y))
            else:
                surface.blit(image_for_empty, (x, y))

    def GetTile(self, position):
        return self.matrix_with_map[position[0] // SIZE_OF_TILE][position[1] // SIZE_OF_TILE]

    @staticmethod
    def GetPositionOfTile(position):
        return position[0] // SIZE_OF_TILE, position[1] // SIZE_OF_TILE

    def CanStandThere(self, position):
        tile = self.GetTile((position[0] - self.global_map_position[0], position[1] - self.global_map_position[1]))
        return tile in [CHAR_FOR_PATH, CHAR_FOR_EXIT]

    def SetCurrentRoom(self, player_position, flag=False):
        if not flag:
            player_position = [player_position[0] - self.global_map_position[0],
                               player_position[1] - self.global_map_position[1]]
        if (self.GetPositionOfTile(player_position), self.GetTile(player_position)) not in self.tiles_for_current_room:
            current_room = []
            self.tiles_for_current_room = {}
            if self.GetTile(player_position) in [CHAR_FOR_PATH]:
                self.dfs.DFSOnTheSpecificTiles(self.GetPositionOfTile(player_position), self.matrix_with_map,
                                               current_room, [CHAR_FOR_PATH, CHAR_FOR_EXIT],
                                               depth=src.back.constants.LENGTH_OF_PATHS)
                self.tiles_for_current_room[
                    (self.GetPositionOfTile(player_position), self.GetTile(player_position))] = True
            elif self.GetTile(player_position) in [CHAR_FOR_EXIT]:
                src.front.ui.ProcessingEndMenu()

            for i in current_room:
                self.visited_tiles[i] = True
            self.SetSpecificOnMatrix(self.matrix_with_visited, current_room)
            left_upper_corner = self.BlitSpecificMap(current_room)
            self.current_room_position = [
                self.global_map_position[0] + left_upper_corner[0] * SIZE_OF_TILE,
                self.global_map_position[1] + left_upper_corner[1] * SIZE_OF_TILE]
            current_room.append([self.GetPositionOfTile(player_position), CHAR_FOR_CURRENT_POS])
            self.BlitSpecificOnMap(self.visited_mappa, current_room)

    def Render(self, display):
        # display.blit(self.mappa, self.global_map_position)
        # print(src.back.constants.DIFFICULTY)
        display.blit(self.current_room, self.current_room_position)
        if src.back.constants.DIFFICULTY < 3:
            display.blit(pygame.transform.scale(self.visited_mappa, SIZE_OF_MINIMAP), POSITION_OF_MINIMAP)

    def MoveMap(self, position):
        self.global_map_position[0] += position[0]
        self.global_map_position[1] += position[1]
        self.current_room_position[0] += position[0]
        self.current_room_position[1] += position[1]

    def SpawnPosition(self):
        while True:
            x_coord_spawn = 0
            y_coord_spawn = 0
            sign = False
            for i in range(src.back.constants.SIZE_OF_MAP[0]):
                for j in range(src.back.constants.SIZE_OF_MAP[0]):
                    if self.matrix_with_map[i][j] in [CHAR_FOR_PATH]:
                        x_coord_spawn = i
                        y_coord_spawn = j
                        sign = True
                        break
                if sign:
                    break
            x_coord_end = 0
            y_coord_end = 0
            sign = False
            for i in range(src.back.constants.SIZE_OF_MAP[0])[::-1]:
                for j in range(src.back.constants.SIZE_OF_MAP[0])[::-1]:
                    if self.matrix_with_map[i][j] in [CHAR_FOR_PATH]:
                        x_coord_end = i
                        y_coord_end = j
                        sign = True
                        break
                if sign:
                    break
            self.matrix_with_map[x_coord_end][y_coord_end] = CHAR_FOR_EXIT

            self.global_map_position = [-x_coord_spawn * SIZE_OF_TILE + SPAWN_POSITION[0],
                                        -y_coord_spawn * SIZE_OF_TILE + SPAWN_POSITION[1]]
            self.SetCurrentRoom((x_coord_spawn * SIZE_OF_TILE, y_coord_spawn * SIZE_OF_TILE), flag=True)
            return None
