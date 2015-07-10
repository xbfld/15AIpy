__author__ = 'Dev1'

class TeamType():
    pass

class Gauge():
    def __init__(self, team, max=25):
        self.team = team
        self.maxValue = max
        self.value = 0
        self.complete = 0

class Team():
    A = TeamType()
    B = TeamType()
    def __init__(self, teamType):
        self.team = teamType
        self.slime = [None for i in range(32)]
        self.gauge = Gauge(self)
        self.spawn = None

    def setSpawn(self, point):
        self.spawn = point

    def minimumEmptySID(self):
        i = 0
        while self.slime[i] is not None:
            i += 1
            if i>=32:
                return -1
        return i