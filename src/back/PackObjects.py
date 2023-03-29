"""File contains classes for packing session into file and unpack when it needed"""

import pygame
import src.back.class_map
import src.back.class_player


class MapForPack:
    """class for prepare map to pack into file"""

    def __init__(self, mappa: src.back.class_map.Map):
        """initialization of the object"""

        self.matrix_with_map = mappa.matrix_with_map

        self.tiles_for_current_room = {}

        self.visited_tiles = mappa.visited_tiles
        self.matrix_with_visited = mappa.matrix_with_visited

        self.global_map_position = mappa.global_map_position
        self.current_room_position = mappa.current_room_position

        self.answer = mappa.answer

    def UnPack(self):
        """create map from packed version"""

        return src.back.class_map.Map(self.matrix_with_map, self.tiles_for_current_room, self.visited_tiles,
                                      self.matrix_with_visited, self.global_map_position, self.current_room_position,
                                      self.answer)


class PlayerForPack:
    """class for prepare player to pack into file"""

    def __init__(self, player: src.back.class_player):
        """initialization of the object"""

        self.character = player.character
        self.side = player.side
        self.hit_box = ((player.hit_box.x, player.hit_box.y), player.hit_box.size)

    def UnPack(self):
        """create player from packed version"""

        return src.back.class_player.Player(self.character, self.side, self.hit_box)
