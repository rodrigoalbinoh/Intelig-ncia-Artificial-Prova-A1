class Node:
    def __init__(self, name, targetDistance, visitable=True):
        self.name = name
        self.visited = False
        self.visitable = visitable
        self.targetDistance = targetDistance
        self.adjacents = []

    def addAdjacent(self, obj):
        self.adjacents.append(obj)
