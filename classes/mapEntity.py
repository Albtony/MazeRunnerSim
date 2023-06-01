from colorama import init, Style, Fore
from copy import deepcopy
from classes.entity import Entity
from classes.map import Map
from classes.entityMap import EntityMap
from classes.search import Wavefront, Djikstra, AStar

class MapEntity:
    def __init__(self, map: Map, entities: list[Entity], entityMap: EntityMap):
        self.map = map    
        self.entities = entities
        self.entityMap = entityMap
        self.updateMapState()
    
    def addEntity(self, entity):
        self.entity.appends(entity)

    def removeEntity(self, entity):
        self.entity

    def updateMapState(self):
        self.map.mapState = deepcopy(self.map.mapData)
        for entity in self.entities: 
            self.map.setValue(entity.position, self.entityMap.getEntry(entity.entityType))

    def updateEntityGoal(self, entity: Entity, goal, strategy="wavefront"):
        entity.goal = goal
        self.calculatePath(self, entity, strategy)

    def calculatePath(self, entity: Entity, strategy="wavefront"):
        mapState = deepcopy(self.map.mapState)
        if strategy == "wavefront":
            wavefont = Wavefront(mapState, entity.position, entity.goal)
            entity.path = wavefont.search()
            entity.stepToGoal = -1 if entity.path is None else len(entity.path)
        elif strategy == "djikstra":
            djikstra = Djikstra(mapState, entity.position, entity.goal)
            entity.path = djikstra.search()
            entity.stepToGoal = -1 if entity.path is None else len(entity.path)
        elif strategy == "a-star":
            astar = AStar(mapState, entity.position, entity.goal)
            entity.path = astar.search()
            entity.stepToGoal = -1 if entity.path is None else len(entity.path)
        else:
            return []
        
    def drawEntityPath(self, entity: Entity):
        counter = 2
        entityPathing = deepcopy(self.map.mapState)
        fullpath = entity.path
        drawpath = fullpath[:-1]
        for path in drawpath:
            entityPathing[path[0]][path[1]] = counter
            counter += 1
        self.drawState(entityPathing)

    def drawState(self, mapState=None):
        init()
        RESET = Style.RESET_ALL
        RED = Fore.RED
        GREEN = Fore.GREEN
        YELLOW = Fore.YELLOW
        BLUE = Fore.BLUE

        output = ""

        if mapState is None:
            mapState = self.map.mapState

        for i, row in enumerate(mapState):
            for j, element in enumerate(row):
                if [i, j] == self.map.goal:
                    output += f"{GREEN}G{RESET},"
                elif element == 1:
                    output += "X,"
                elif element == 0:
                    output += " ,"
                elif element == -1:
                    output += f"{YELLOW}P{RESET},"
                elif element == -2:
                    output += f"{RED}N{RESET},"
                elif element > 1:
                    output += f"{BLUE}{(element-1) % 10}{RESET},"
            output += "\n"
        print(output)

    