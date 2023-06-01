import random as rand

def generateSpawnPoints(map, num):
    """
    Generate a list of valid spawn points within the given map.
    Args:
        map (list[list[int]]): The map data.
        num (int): The number of spawn points to generate.
    Returns:
        list[list[int]]: List of valid spawn points.
    Raises:
        ValueError: If the requested number of spawn points exceeds the possible spawn points.
    """
    spawnPoints = []
    maxSpawnPoints = countOccurence2DArray(map, 0)

    if num > maxSpawnPoints:
        raise ValueError("Requested spawn points exceed the possible spawn points")
    
    for _ in range(num):
        point = generateValidPoint(map, spawnPoints)
        spawnPoints.append(point)
    
    return spawnPoints

def countOccurence2DArray(arr2D, val): 
    """
    Count the occurrence of a value in a 2D array.
    Args:
        arr2D (list[list]): The 2D array.
        val: The value to count.
    Returns:
        int: The count of occurrences.
    """
    flatList = [element for row in arr2D for element in row]
    count = flatList.count(val)
    return count

def generateValidPoint(map, spawnPoints):
    """
    Generate a valid point within the given map and spawn points.
    Args:
        map (list[list[int]]): The map data.
        spawnPoints (list[list[int]]): List of spawn points.
    Returns:
        list[int]: A valid point [x, y].
    """
    map_size = [len(map), len(map[0])]
    
    while True:
        x = rand.randint(0, map_size[0]-1)
        y = rand.randint(0, map_size[1]-1)

        point = [x, y]
        
        if isValid(map, spawnPoints, point):
            return point

def isValid(map, spawnPoints, point):
    """
    Check if a point is valid based on the map and spawn points.
    Args:
        map (list[list[int]]): The map data.
        spawnPoints (list[list[int]]): List of spawn points.
        point (list[int]): The point to check.
    Returns:
        bool: True if the point is valid, False otherwise.
    """

    is_not_wall = map[point[0]][point[1]] == 0
    is_not_exist = not isExist(spawnPoints, point)
    
    if is_not_wall and is_not_exist:
        return True
    return False

def isExist(spawnPoints, point):
    """
    Check if a point exists in the list of spawn points.
    Args:
        spawnPoints (list[list[int]]): List of spawn points.
        point (list[int]): The point to check.
    Returns:
        bool: True if the point exists, False otherwise.
    """
    for spawnPoint in spawnPoints:
        if spawnPoint == point:
            return True
    return False