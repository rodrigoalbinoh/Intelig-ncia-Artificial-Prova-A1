class OrdenedVector:
    def __init__(self, size):
        self.numberOfElements = 0
        self.objects = [None] * size

    def insert(self, obj):
        if self.numberOfElements == 0:
            self.objects[0] = obj
            self.numberOfElements = 1
            return

        position = 0
        i = 0

        while i < self.numberOfElements:
            if obj.targetDistance > self.objects[position].targetDistance:
                position += 1

            i += 1

        for k in range(self.numberOfElements, position, -1):
            self.objects[k] = self.objects[k - 1]

        self.objects[position] = obj
        self.numberOfElements += 1

    def getSuccessor(self):
        return self.objects[0]

    def toString(self):
        for i in range(0, self.numberOfElements):
            print('{} - {}'.format(self.objects[i].name, self.objects[i].targetDistance))
