__author__ = 'Dev1'

from team import Team, TeamType
from slime import Slime


class Square:
    def __init__(self):
        self.state = None
        self.hadChanged = False

    def isNeutral(self):
        return self.state is None

    def changeState(self, teamType):
        self.state = teamType


class Area:
    def __init__(self, teamType):
        self.square = []
        self.edge = []
        self.team = teamType

    def contains(self, point):
        pass #¹Ì±¸Çö


class Edge:
    def __init__(self):
        self.isFenceA = False
        self.isFenceB = False
        self.isPathA = False
        self.isPathB = False
        self.SID = 0

    def isNeutral(self):
        return (not self.isFenceA) and (not self.isFenceB) and (not self.isPathA) and (not self.isPathB)

    def neutralize(self):
        self.__init__()

    def setFence(self, teamType):
        if teamType == Team.A:
            self.isFenceA = True
        else:
            self.isFenceB = True

    def setPath(self, slime):
        if slime.team == Team.A:
            self.isPathA = True
        else:
            self.isPathB = True
        self.SID |= (1 << slime.SID)

    def removePath(self, SID, team):
        if team == Team.A and not self.isPathA:
            return
        if team == Team.B and not self.isPathB:
            return
        self.SID = self.SID & ~SID
        if self.SID==0:
            self.isPathA = False
            self.isPathB = False


class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.square = [[Square() for y in range(height)] for x in range(width)]
        self.point = [[{Team.A: 0, Team.B: 0} for y in range(height+1)] for x in range(width+1)]
        self.horizontalEdge = [[Edge() for y in range(height+1)] for x in range(width)]
        self.verticalEdge = [[Edge() for y in range(height)] for x in range(width+1)]

    def getPoint(self, x, y):
        return self.point[x][y]

    def getSquare(self, x, y):
        return self.square[x][y]

    def getEdge(self, point, direction):
        x, y = point
        if direction%2==0: # horizontal
            return self.horizontalEdge[x-direction//2][y]
        else: #vertical
            return self.verticalEdge[x][y-direction//2]

    def getPointState(self, point):
        for direction in range(4):
            edge = self.getEdge(point, direction)
            if edge.isPathA:
                return Team.A
            elif edge.isPathB:
                return Team.B
        return None