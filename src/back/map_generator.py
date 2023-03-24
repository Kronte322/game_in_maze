"""File contains map generator"""

import random
from src.back.constants import *
import src.back.constants
import time

random.seed(time.time())
# random.seed(12)


class MapGenerator:

    @staticmethod
    def GenerateMaze(size=(30, 20)):
        maze = []
        MapGenerator.FillMatrix(maze, size)
        MapGenerator.SetBoardsOfMap(maze)
        MapGenerator.SetPathsOnMap(maze)
        return maze

    @staticmethod
    def GetClearMap(size=(30, 20)):
        result = []
        MapGenerator.FillMatrix(result, size)
        return result

    @staticmethod
    def GetTile(position: tuple, matrix):
        return matrix[position[0]][position[1]]

    @staticmethod
    def GetNeighbours(position: tuple, matrix):
        result = []
        if position[0] > 0:
            result.append((position[0] - 1, position[1]))
        if position[0] < len(matrix) - 1:
            result.append((position[0] + 1, position[1]))
        if position[1] > 0:
            result.append((position[0], position[1] - 1))
        if position[1] < len(matrix[0]) - 1:
            result.append((position[0], position[1] + 1))
        return result

    @staticmethod
    def GetAround(position: tuple, matrix):
        result = []
        interm = []

        if position[0] > 0 and position[1] > 0:
            interm.append((position[0] - 1, position[1] - 1))
        else:
            interm.append((-1, -1))
        if position[0] > 0:
            interm.append((position[0] - 1, position[1]))
        else:
            interm.append((-1, -1))
        if position[0] > 0 and position[1] < len(matrix[0]) - 1:
            interm.append((position[0] - 1, position[1] + 1))
        else:
            interm.append((-1, -1))
        result.append(interm.copy())

        interm.clear()

        if position[1] > 0:
            interm.append((position[0], position[1] - 1))
        else:
            interm.append((-1, -1))
        interm.append((position[0], position[1]))
        if position[1] < len(matrix[0]) - 1:
            interm.append((position[0], position[1] + 1))
        else:
            interm.append((-1, -1))
        result.append(interm.copy())

        interm.clear()

        if position[0] < len(matrix) - 1 and position[1] > 0:
            interm.append((position[0] + 1, position[1] - 1))
        else:
            interm.append((-1, -1))
        if position[0] < len(matrix) - 1:
            interm.append((position[0] + 1, position[1]))
        else:
            interm.append((-1, -1))
        if position[0] < len(matrix) - 1 and position[1] < len(matrix[0]) - 1:
            interm.append((position[0] + 1, position[1] + 1))
        else:
            interm.append((-1, -1))
        result.append(interm.copy())

        interm.clear()

        return result

    @staticmethod
    def GetLeftAround(position, matrix):
        around = MapGenerator.GetAround(position, matrix).copy()
        around.pop()
        return around

    @staticmethod
    def GetUpAround(position, matrix):
        around = MapGenerator.GetAround(position, matrix)
        res = []
        for i in range(len(around)):
            interm = []
            for j in range(len(around[0]) - 1):
                interm.append(around[i][j])
            res.append(interm)
        return res

    @staticmethod
    def GetRightAround(position, matrix):
        around = MapGenerator.GetAround(position, matrix)
        res = []
        for i in range(1, len(around)):
            res.append(around[i])
        return res

    @staticmethod
    def GetDownAround(position, matrix):
        around = MapGenerator.GetAround(position, matrix)
        res = []
        for i in range(len(around)):
            interm = []
            for j in range(1, len(around[0])):
                interm.append(around[i][j])
            res.append(interm)
        return res

    @staticmethod
    def GetAroundForDFS(position, parent, matrix):
        if position[0] > parent[0]:
            return MapGenerator.GetLeftAround(parent, matrix)
        if position[0] < parent[0]:
            return MapGenerator.GetRightAround(parent, matrix)
        if position[1] > parent[1]:
            return MapGenerator.GetUpAround(parent, matrix)
        if position[1] < parent[1]:
            return MapGenerator.GetDownAround(parent, matrix)

    @staticmethod
    def FillMatrix(matrix, size):
        for i in range(size[0]):
            interm = []
            for j in range(size[1]):
                interm.append(CHAR_FOR_EMPTY)
            matrix.append(interm)

    @staticmethod
    def SetBoardsOfMap(matrix):
        for i in range(len(matrix)):
            matrix[i][0] = CHAR_FOR_BOARD
        for i in range(len(matrix[0])):
            matrix[len(matrix) - 1][i] = CHAR_FOR_BOARD
        for i in range(len(matrix)):
            matrix[i][len(matrix[0]) - 1] = CHAR_FOR_BOARD
        for i in range(len(matrix[0])):
            matrix[0][i] = CHAR_FOR_BOARD

    @staticmethod
    def SetPathsOnMap(matrix):
        dfs = DFSAlgo()
        prima = PrimaAlgo()
        first_coord = random.randrange(1, src.back.constants.SIZE_OF_MAP[0] - 1)
        second_coord = random.randrange(1, src.back.constants.SIZE_OF_MAP[1] - 1)
        test = src.back.constants.ALGO_FOR_GENERATION
        if src.back.constants.ALGO_FOR_GENERATION == 'DFS':
            dfs.DFSForPaths((first_coord, second_coord), matrix)
            for i in dfs.GetPath():
                matrix[i[0]][i[1]] = CHAR_FOR_PATH
            dfs.Clear()
        elif src.back.constants.ALGO_FOR_GENERATION == 'Prima':
            prima.PrimaForPaths((first_coord, second_coord), matrix)
            for i in prima.GetPath():
                matrix[i[0]][i[1]] = CHAR_FOR_PATH
            prima.Clear()

    @staticmethod
    def ClearMatrix(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = CHAR_FOR_EMPTY


class DFSAlgo:
    def __init__(self):
        self.used = {}
        self.parents = {}
        self.path = []

    def GetPath(self):
        return self.path

    def Clear(self):
        self.parents.clear()
        self.path.clear()
        self.used.clear()

    def DFSForPaths(self, vertex, matrix):
        sign = False
        for i in MapGenerator.GetAround(vertex, matrix):
            for j in i:
                if j not in [(-1, -1), vertex]:
                    if j == self.parents.get(vertex):
                        continue
                    if MapGenerator.GetTile(j, matrix) not in [CHAR_FOR_EMPTY, CHAR_FOR_BOARD]:
                        sign = True
                        continue
                    if self.used.get(j):
                        second_sign = False
                        for k in MapGenerator.GetAroundForDFS(vertex, self.parents[vertex], matrix):
                            if j in k:
                                second_sign = True
                                break
                        if second_sign:
                            continue
                        sign = True
                        continue
        if sign:
            return
        self.used[vertex] = True
        self.path.append(vertex)
        neighbours = MapGenerator.GetNeighbours(vertex, matrix).copy()
        while len(neighbours) != 0:
            i = random.choice(neighbours)
            neighbours.remove(i)
            if self.used.get(i) is None and i != self.parents.get(vertex) and MapGenerator.GetTile(i, matrix) not in [
                CHAR_FOR_BOARD]:
                self.parents[i] = vertex
                self.DFSForPaths(i, matrix)

    def RecursiveCall(self, vertex, matrix, set_of_tiles, tiles, current_depth, depth):
        self.used[vertex] = True
        self.path.append(vertex)
        set_of_tiles.append((vertex, MapGenerator.GetTile(vertex, matrix)))
        if current_depth >= depth:
            return
        for i in MapGenerator.GetNeighbours(vertex, matrix):
            if MapGenerator.GetTile(i, matrix) in tiles:
                if self.used.get(i) is None and i != self.parents.get(vertex):
                    self.parents[i] = vertex
                    self.RecursiveCall(i, matrix, set_of_tiles, tiles, current_depth=current_depth + 1, depth=depth)

    def DFSOnTheSpecificTiles(self, vertex, matrix, set_of_tiles, tiles, depth=1000000):
        self.Clear()
        self.RecursiveCall(vertex, matrix, set_of_tiles, tiles, current_depth=0, depth=depth)


class PrimaAlgo:
    def __init__(self):
        self.opened = {}
        self.closed = {}
        self.parents = {}
        self.path = []

    def GetPath(self):
        return self.path

    def Clear(self):
        self.opened.clear()
        self.closed.clear()
        self.path.clear()

    def PrimaForPaths(self, vertex, matrix):
        self.opened[vertex] = vertex
        while len(self.opened) != 0:
            current = [0, 0]
            if len(self.opened) == 1:
                current = list(self.opened.items())[0][0]
            else:
                current = random.choice(list(self.opened.values()))
            self.opened.pop(current)
            sign = False
            for i in MapGenerator.GetAround(current, matrix):
                for j in i:
                    if j not in [(-1, -1), current]:
                        if j == self.parents.get(current):
                            continue
                        if MapGenerator.GetTile(j, matrix) not in [CHAR_FOR_EMPTY, CHAR_FOR_BOARD]:
                            sign = True
                            continue
                        if self.closed.get(j):
                            second_sign = False
                            for k in MapGenerator.GetAroundForDFS(current, self.parents[current], matrix):
                                if j in k:
                                    second_sign = True
                                    break
                            if second_sign:
                                continue
                            sign = True
                            continue
            if sign:
                continue
            self.path.append(current)
            self.closed[current] = current
            for i in MapGenerator.GetNeighbours(current, matrix):
                if i not in self.closed and MapGenerator.GetTile(i, matrix) not in [CHAR_FOR_BOARD]:
                    self.opened[i] = i
                    self.parents[i] = current
