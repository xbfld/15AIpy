# -*- coding: utf8 -*-
__author__ = 'Dev1'

from field import *
from team import *
from slime import *


class Game:
    def __init__(self):
        self.teamA = Team(True)
        self.teamB = Team(False)
        self.field = Field(11,11)
        self.slime = []

    def moveSlimes(self):
        # 꼭지점 SID 초기화
        for slime in self.slime:
            x, y = slime.position
            self.field.getPoint(x,y)[slime.team] = 0

        # 슬라임 옮기기
        for slime in self.slime:
            slime.hasMoved = False
            # TODO: 아래 부분 슬라임 내부로 넣기
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
        # 충돌한 슬라임의 위치를 구한다.
        for aSlime in self.teamA.slime:
            if aSlime is None:
                continue
            pos = aSlime.position
            SID_B = self.field.getPoint(*pos)[Team.B]
            if SID_B != 0:
                targetPosition.append(pos)

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
            # 미구현

    def createSlime(self, teamType):
        team = self.teamA if teamType == Team.A else self.teamB
        # SID = team.minimumEmptySID()
        # position = team.spawn
        # direction = 0 if teamType == Team.A else 2
        # team.slime[SID] = slime

        slime = team.addSlime()
        self.slime.append(slime)

    # def removeSlime(self, slime):
    #     # 필드에서 슬라임 제거
    #     x, y = slime.position
    #     self.field.getPoint(x,y)[slime.team] &= ~SID
    #
    #     # 필드에서 슬라임 경로 제거
    #     for edges in self.field.horizontalEdge:
    #         for edge in edges:
    #             edge.removePath(SID, slime.team)
    #     for edges in self.field.verticalEdge:
    #         for edge in edges:
    #             edge.removePath(SID, slime.team)
    #
    #     # 슬라임 정보 제거
    #     SID = slime.SID
    #     team = self.teamA if slime.team == Team.A else self.teamB
    #     team.slime[SID] = None
    #     self.slime.remove(slime)

    def removeSlimes(self, SID, team):
        # 필드에서 슬라임 경로 제거
        for edges in self.field.horizontalEdge:
            for edge in edges:
                edge.removePath(SID)
        for edges in self.field.verticalEdge:
            for edge in edges:
                edge.removePath(SID)

        # 슬라임 정보 제거
        team = self.teamA if team == Team.A else self.teamB
        #team.slime[SID] = None
        team.discardSlimes(SID)