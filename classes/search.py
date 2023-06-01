import queue
from copy import deepcopy

class Wavefront:
    def __init__(self, mapData, start, goal):
        self.mapData = deepcopy(mapData)
        self.mapProcess = deepcopy(mapData)
        self.start = start
        self.goal = goal

    def search(self):
        self.mapProcess = deepcopy(self.mapData)
        self.setValue(self.goal, 0)
        self.setValue(self.start, 2)
        toBeVisited = queue.Queue()
        toBeVisited.put(self.start)

        while not toBeVisited.empty():
            current = toBeVisited.get()
            neighbors = self.getNeighbors(current, "search")
            for neighbor in neighbors:
                currentValue = self.getValue(current)
                self.setValue(neighbor, currentValue + 1)
                toBeVisited.put(neighbor)
                if list(neighbor) == list(self.goal):
                    return self.reconstructPath()
        if list(self.start) == list(self.goal):
            return []
        return None

    def getNeighbors(self, position, strategy):
        init = []
        neighbors = []
        x = position[0]
        y = position[1]

        if x > 0:
            init.append((x - 1, y))
        if x < len(self.mapProcess) - 1:
            init.append((x + 1, y))
        if y > 0:
            init.append((x, y - 1))
        if y < len(self.mapProcess[0]) - 1:
            init.append((x, y + 1))

        if strategy == "search":
            for neighbor in init:
                if self.isValidPosition(neighbor):
                    neighbors.append(neighbor)
        elif strategy == "reconstruction":
            for neighbor in init:
                if self.isValidPath(neighbor):
                    neighbors.append(neighbor)
        
        return neighbors
    
    def isValidPosition(self, position):
        return self.mapProcess[position[0]][position[1]] == 0

    def isValidPath(self, position):
        return self.mapProcess[position[0]][position[1]] > 1

    def setValue(self, position, value):
        self.mapProcess[position[0]][position[1]] = value
    
    def getValue(self, position):
        return self.mapProcess[position[0]][position[1]]
    
    def reconstructPath(self):
        path = []
        current = self.goal
        while list(current) != list(self.start):
            path.append(current)
            neighbors = self.getNeighbors(current, "reconstruction")
            minNeighbor = None

            for neighbor in neighbors:
                currValue = self.getValue(current)
                neighValue = self.getValue(neighbor)
                if neighValue < currValue:
                    minNeighbor = neighbor
                    break
            
            if minNeighbor == None:
                raise ValueError("Cannot reconstruct path")
                # path.pop()
                # break

            current = minNeighbor
        return path[::-1]

class Djikstra:
    def __init__(self, mapData, start, goal):
        self.mapData = mapData
        self.start = start
        self.goal = goal
        raise NotImplementedError("This function is not implemented yet.")

class AStar:
    def __init__(self, mapData, start, goal):
        self.mapData = mapData
        self.start = start
        self.goal = goal
        raise NotImplementedError("This function is not implemented yet.")
