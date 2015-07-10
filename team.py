# -*- coding: utf8 -*-
__author__ = 'Dev1'

from slime import Slime


class TeamType:
    pass


class Gauge:
    def __init__(self, team, max=25):
        self.team = team
        self.maxValue = max
        self.value = 0
        self.complete = 0


class Team:
    A = TeamType()
    B = TeamType()

    def __init__(self, teamType):
        self.team = teamType
        self.slime = [None for i in range(32)]
        self.gauge = Gauge(self)
        self.spawn = None
        self.SID = 0

    def setSpawn(self, point):
        self.spawn = point

    # def minimumEmptySID(self):
    #     # i = 0
    #     # while self.slime[i] is not None:
    #     #     i += 1
    #     #     if i>=32:
    #     #         return -1
    #     # return i
    #     div, mod = self.SID, 0
    #     for i in range(32):
    #         div, mod = divmod(div, 2)
    #         if mod is 0:
    #             return 1<<i

    def addSlime(self):
        div, mod = self.SID, 0
        for i in range(32):
            div, mod = divmod(div, 2)
            if mod is not 0:
                continue
            team = self.team
            newSID = 1 << i
            pos = self.spawn
            direction = 0 if team == Team.A else 2
            slime = Slime(team, newSID, pos, direction)
            return slime

    def discardSlimes(self, sid):
        div, mod = sid, 0
        for i in range(32):
            div, mod = divmod(div, 2)
            if mod is 0:
                continue
            self.slime[i] = None


