class OrdenedVectorAdjacent:
    def __init__(self, size):
        self.numberOfElements = 0
        self.adjacents = [None] * size

    def insert(self, adjacent):
        if self.numberOfElements == 0:
            self.adjacents[0] = adjacent
            self.numberOfElements = 1
            return

        position = 0
        i = 0

        while i < self.numberOfElements:
            if adjacent.distanceAStar > self.adjacents[position].distanceAStar:
                position += 1
            i += 1

        for k in range(self.numberOfElements, position, -1):
            self.adjacents[k] = self.adjacents[k - 1]

        self.adjacents[position] = adjacent
        self.numberOfElements += 1

    def getSuccessor(self):
        return self.adjacents[0].node

    def toString(self):
        for i in range(0, self.numberOfElements):
            print('{} - {}'.format(self.adjacents[i].node.name, self.adjacents[i].distanceAStar))