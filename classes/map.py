from copy import deepcopy

class Map:
    def __init__(self, mapData=None, goal=None):
        assert mapData is not None, "Map must be provided."
        assert goal is not None, "Goal must be provided."

        self.mapData = deepcopy(mapData)
        self.mapState = deepcopy(mapData)
        self.goal = goal

    def setValue(self, position, value):
        self.mapState[position[0]][position[1]] = value