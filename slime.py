__author__ = 'Dev1'


class Slime():
    directionToCoord = {0: (1,0), 1: (0,1), 2: (-1,0), 3: (0,-1)}
    def __init__(self, teamType, SID, position, initialDirection):
        self.team = teamType
        self.SID = SID
        self.position = None
        self.direction = initialDirection
        self.hasMoved = False
        self.setPosition(position)

    def changeDirection(self, direction):
        self.direction = direction
    def setPosition(self, point):
        self.position = point
