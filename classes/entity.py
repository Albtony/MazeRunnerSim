class Entity:
    def __init__(self, position, goal, entityType):
        self.position = position
        self.goal = goal
        self.path = None
        self.stepToGoal = -1
        self.entityType = entityType

    def step(self):
        if self.path == None or self.path == []:
            return
        self.stepToGoal = len(self.path)
        self.position = self.path.pop(0)
    
    def updateGoal(self, goal):
        self.goal = goal