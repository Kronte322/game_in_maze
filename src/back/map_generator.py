"""File contains map generator"""

import random
from src.back.constants import *
import src.back.constants
import time
from collections import deque

random.seed(time.time())
# random.seed(12)


class MapGenerator:
    """this class make able to generate maze and make able to operate with it"""

    @staticmethod
    def GenerateMaze(size=(30, 20)):
        """generate maze as matrix with following size"""

        maze = []
        MapGenerator.CreateMatrix(maze, size)
        MapGenerator.SetBoardsOfMap(maze)
        MapGenerator.SetPathsOnMap(maze)
        return maze

    @staticmethod
    def GetClearMap(size=(30, 20)):
        """generate empty matrix with following size"""

        result = []
        MapGenerator.CreateMatrix(result, size)
        return result

    @staticmethod
    def GetTile(position: tuple, matrix):
        """return what tile on following position in matrix"""

        return matrix[position[0]][position[1]]

    @staticmethod
    def GetNeighbours(position: tuple, matrix):
        """return nearby tiles by cross on following position in matrix"""

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
        """return all nearby tiles on following position in matrix"""

        result = []
        intermediate = []

        if position[0] > 0 and position[1] > 0:
            intermediate.append((position[0] - 1, position[1] - 1))
        else:
            intermediate.append((-1, -1))
        if position[0] > 0:
            intermediate.append((position[0] - 1, position[1]))
        else:
            intermediate.append((-1, -1))
        if position[0] > 0 and position[1] < len(matrix[0]) - 1:
            intermediate.append((position[0] - 1, position[1] + 1))
        else:
            intermediate.append((-1, -1))
        result.append(intermediate.copy())

        intermediate.clear()

        if position[1] > 0:
            intermediate.append((position[0], position[1] - 1))
        else:
            intermediate.append((-1, -1))
        intermediate.append((position[0], position[1]))
        if position[1] < len(matrix[0]) - 1:
            intermediate.append((position[0], position[1] + 1))
        else:
            intermediate.append((-1, -1))
        result.append(intermediate.copy())

        intermediate.clear()

        if position[0] < len(matrix) - 1 and position[1] > 0:
            intermediate.append((position[0] + 1, position[1] - 1))
        else:
            intermediate.append((-1, -1))
        if position[0] < len(matrix) - 1:
            intermediate.append((position[0] + 1, position[1]))
        else:
            intermediate.append((-1, -1))
        if position[0] < len(matrix) - 1 and position[1] < len(matrix[0]) - 1:
            intermediate.append((position[0] + 1, position[1] + 1))
        else:
            intermediate.append((-1, -1))
        result.append(intermediate.copy())

        intermediate.clear()

        return result

    @staticmethod
    def GetLeftAround(position, matrix):
        """return all nearby tiles on following position without right column"""

        around = MapGenerator.GetAround(position, matrix).copy()
        around.pop()
        return around

    @staticmethod
    def GetUpAround(position, matrix):
        """return all nearby tiles on following position bottom row"""

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
        """return all nearby tiles on following position without left column"""

        around = MapGenerator.GetAround(position, matrix)
        res = []
        for i in range(1, len(around)):
            res.append(around[i])
        return res

    @staticmethod
    def GetDownAround(position, matrix):
        """return all nearby tiles on following position without top row"""

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
        """return nearby tiles on following position for dfs algorithm according to parent of the tile"""

        if position[0] > parent[0]:
            return MapGenerator.GetLeftAround(parent, matrix)
        if position[0] < parent[0]:
            return MapGenerator.GetRightAround(parent, matrix)
        if position[1] > parent[1]:
            return MapGenerator.GetUpAround(parent, matrix)
        if position[1] < parent[1]:
            return MapGenerator.GetDownAround(parent, matrix)

    @staticmethod
    def CreateMatrix(matrix, size):
        """create matrix with specific size"""

        for i in range(size[0]):
            interm = []
            for j in range(size[1]):
                interm.append(CHAR_FOR_EMPTY)
            matrix.append(interm)

    @staticmethod
    def SetBoardsOfMap(matrix):
        """set boards on matrix like picture frame, for avoiding some troubles with boarders"""

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
        """set paths on map using specific algorithm"""

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
        """fill matrix with empty tile"""

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = CHAR_FOR_EMPTY


class DFSAlgo:
    """this class represents deep first search algorithm"""

    def __init__(self):
        """initialize all that DFS algorithm requires"""

        self.used = {}
        self.parents = {}
        self.path = []

    def GetPath(self):
        """return passed during algorithm path"""

        return self.path

    def Clear(self):
        """clear variables of member class"""

        self.parents.clear()
        self.path.clear()
        self.used.clear()

    def DFSForPaths(self, vertex, matrix):
        """random depth first search for generate random maze on empty matrix"""

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
        """help function for DFSOnTHeSpecificTIles"""

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
        """DFs which goes across the following tiles"""

        self.Clear()
        self.RecursiveCall(vertex, matrix, set_of_tiles, tiles, current_depth=0, depth=depth)


class PrimaAlgo:
    """this class represents prima algorithm"""

    def __init__(self):
        """initialize all that requires prima algorithm"""

        self.opened = {}
        self.closed = {}
        self.parents = {}
        self.path = []

    def GetPath(self):
        """return passed during algorithm path"""

        return self.path

    def Clear(self):
        """clear variables of member class"""

        self.opened.clear()
        self.closed.clear()
        self.path.clear()

    def PrimaForPaths(self, vertex, matrix):
        """prima algorithm with random choice from open tiles"""

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


class BFSAlgo:
    """this class represents best first search algorithm"""

    def __init__(self):
        """initialize all that bfs algorithm requires"""

        self.deque = deque()
        self.closed = {}
        self.parents = {}
        self.path = []

    def BFSForFindShortestPath(self, vertex, matrix):
        """this method perform a search the shortest path that complete maze using bfs algorithm"""

        self.deque.appendleft(vertex)
        current = vertex
        self.parents[current] = current
        while len(self.deque) != 0:
            current = self.deque.pop()
            self.closed[current] = True
            if MapGenerator.GetTile(current, matrix) in [CHAR_FOR_EXIT]:
                break
            for i in MapGenerator.GetNeighbours(current, matrix):
                if MapGenerator.GetTile(i, matrix) in [CHAR_FOR_PATH, CHAR_FOR_EXIT]:
                    if i not in self.closed:
                        self.parents[i] = current
                        self.deque.appendleft(i)

        while current != self.parents[current]:
            self.path.append([current, CHAR_FOR_ANSWER])
            current = self.parents[current]
        self.path.append([current, CHAR_FOR_ANSWER])

    def GetPath(self):
        """this method returns path that bfs algorithm has traveled"""

        return self.path
