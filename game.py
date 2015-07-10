__author__ = 'Dev1'

from field import *
from team import *
from slime import *

class Game():
    def __init__(self):
        self.teamA = Team(True)
        self.teamB = Team(False)
        self.field = Field(11,11)
        self.slime = []

    def moveSlimes(self):
        # ������ SID �ʱ�ȭ
        for slime in self.slime:
            x, y = slime.position
            self.field.getPoint(x,y)[slime.team] = 0

        # ������ �ű��
        for slime in self.slime:
            slime.hasMoved = False
            x, y = slime.position
            dx, dy = Slime.directionToCoord[slime.direction]
            nx, ny = x+dx, y+dy
            if nx<0 or nx>self.field.width or ny<0 or ny>self.field.height:
                nextPosition = (x, y)
                # Cannot move
            else:
                nextPosition = (nx, ny)
                slime.hasMoved = True

            slime.setPosition(nextPosition)
            x, y = nextPosition
            self.field.getPoint(x,y)[slime.team] |= (1<<slime.SID)

    def overlapPenalty(self):
        targetPosition =[]
        for aSlime in self.teamA.slime:
            if aSlime is None:
                continue
            x, y = aSlime.position
            SID_B = self.field.getPoint(x, y)[Team.B]
            if SID_B != 0:
                SID_A = self.field.getPoint(x, y)[Team.A]
                ######################################################
                # 2^32-1�� 0~31 �� ������ �ٲٱ�!

        for position in targetPosition:
            position.slime = 0

    def changeEdges(self):
        for slime in self.slime:
            if not slime.hasMoved:
                continue
            # Moved slime only
            point = slime.position
            antiDirection = (slime.direction+2)%4
            edge = self.field.getEdge(point, antiDirection)
            # �̱���

    def createSlime(self, teamType):
        team = self.teamA if teamType == Team.A else self.teamB
        SID = team.minimumEmptySID()
        position = team.spawn
        direction = 0 if teamType == Team.A else 2

        slime = Slime(teamType, SID, position, direction)
        self.slime.append(slime)
        team.slime[SID] = slime

    # def removeSlime(self, slime):
    #     # �ʵ忡�� ������ ����
    #     x, y = slime.position
    #     self.field.getPoint(x,y)[slime.team] &= ~SID
    #
    #     # �ʵ忡�� ������ ��� ����
    #     for edges in self.field.horizontalEdge:
    #         for edge in edges:
    #             edge.removePath(SID, slime.team)
    #     for edges in self.field.verticalEdge:
    #         for edge in edges:
    #             edge.removePath(SID, slime.team)
    #
    #     # ������ ���� ����
    #     SID = slime.SID
    #     team = self.teamA if slime.team == Team.A else self.teamB
    #     team.slime[SID] = None
    #     self.slime.remove(slime)

    def removeSlimes(self, SID, team):
        # �ʵ忡�� ������ ��� ����
        for edges in self.field.horizontalEdge:
            for edge in edges:
                edge.removePath(SID)
        for edges in self.field.verticalEdge:
            for edge in edges:
                edge.removePath(SID)

        # ������ ���� ����
        team = self.teamA if team == Team.A else self.teamB
        team.slime[SID] = None
        self.slime.remove(slime)