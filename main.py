from utils.spawner import generateSpawnPoints
from classes.entity import Entity
from classes.map import Map
from classes.mapEntity import MapEntity
from classes.entityMap import EntityMap

def main():

    """                   MAP LAYOUT
    x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x
    x,x,x,x,x, ,x, , ,x, , , , , , , , , ,x, , ,x, ,x,x,x,x,x
    x,x,x,x,x, , , ,x,x,x, ,x,x,x,x,x, ,x,x,x, , , ,x,x,x,x,x
    x, , , ,x, ,x, , , , , , , ,x, , , , , , , ,x, ,x, , , ,x
    x,x,x, ,x, ,x, ,x,x,x,x,x, ,x, ,x,x,x,x,x, ,x, ,x, ,x,x,x
    x, , , , , , , , , ,x, , , , , , , ,x, , , , , , , , , ,x
    x,x,x,x, ,x,x,x,x, ,x, ,x,x, ,x,x, ,x, ,x,x,x,x, ,x,x,x,x
    x,x, , , ,x,x,x,x, ,x, ,x, , , ,x, ,x, ,x,x,x,x, , , ,x,x
    x,x, ,x,x,x,x, , , , , ,x, , , ,x, , , , , ,x,x,x,x, ,x,x
    x,x, ,x,x,x,x, ,x,x,x, ,x,x,x,x,x, ,x,x,x, ,x,x,x,x, ,x,x
    x,x, , , , , , , , ,x, , , , , , , ,x, , , , , , , , ,x,x
    x, , , ,x, ,x,x,x, ,x, ,x,x,x,x,x, ,x, ,x,x,x, ,x, , , ,x
    x,x,x, ,x, ,x, , , , , , , ,x, , , , , , , ,x, ,x, ,x,x,x
    x, , , ,x, , , ,x,x,x,x,x, ,x, ,x,x,x,x,x, , , ,x, , , ,x
    x, ,x,x,x,x,x, , , , , , , ,x, , , , , , , ,x,x,x,x,x, ,x
    x, , , , , , , ,x,x,x, ,x, , , ,x, ,x,x,x, , , , , , , ,x
    x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x
    """

    mapData = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,1,1,1,1],
        [1,1,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,0,0,1,1,1,1,1],
        [1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1],
        [1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,0,1,1,1,1,0,1,0,1,1,0,1,1,0,1,0,1,1,1,1,0,1,1,1,1],
        [1,1,0,0,0,1,1,1,1,0,1,0,1,0,0,0,1,0,1,0,1,1,1,1,0,0,0,1,1],
        [1,1,0,1,1,1,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,1,1,1,0,1,1],
        [1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,0,1,1],
        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1],
        [1,0,0,0,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,0,0,0,1],
        [1,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,1,1],
        [1,0,0,0,1,0,0,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,0,0,1,0,0,0,1],
        [1,0,1,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,1,1,1,0,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]

    # set game parameters
    strategy = "wavefront"
    numOfNpc = 5
    spawnPoints = generateSpawnPoints(mapData, numOfNpc + 2)
    playerSpawn = spawnPoints[0]
    goalPos = spawnPoints[1]
    npcsSpawn = spawnPoints[2:]

    # spawn entities
    player = Entity(playerSpawn, goalPos, "player")
    npcs = [(Entity(npcSpawn, playerSpawn, "npc")) for npcSpawn in npcsSpawn]
    entities = [player] + npcs

    entityMap = EntityMap()
    entityMap.addEntry("player", -1)
    entityMap.addEntry("npc", -2)

    # prepare map
    map = Map(mapData, goalPos)
    mapEntity = MapEntity(map, entities, entityMap)

    # prepare entity state
    for entity in mapEntity.entities:
        mapEntity.calculatePath(entity, strategy)

    # lets take a lookey-lookey
    isPlaying = True
    while(isPlaying):
        mapEntity.drawState()
        for entity in mapEntity.entities:
            entity.step()
            mapEntity.updateMapState()
            mapEntity.calculatePath(entity)
            if entity.stepToGoal == 0:
                isPlaying = False
                break
            if entity.entityType == "npc":
                entity.updateGoal(player.position)  
        
if __name__ == "__main__":
    main()
