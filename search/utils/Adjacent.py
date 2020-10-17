class Adjacent:
    def __init__(self, node, distance):
        self.node = node
        self.distance = distance
        self.distanceAStar = self.node.targetDistance + self.distance
