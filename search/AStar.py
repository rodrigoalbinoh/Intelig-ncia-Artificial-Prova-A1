from search.utils.OrdenedVectorAdjacent import OrdenedVectorAdjacent


class AStar:
    def __init__(self, target):
        self.target = target
        self.found = False
        self.border = None

    def search(self, current):
        if current.visitable:
            print('\nAtual: {}'.format(current.name))
            current.visited = True

            if current == self.target:
                self.found = True
            else:
                self.border = OrdenedVectorAdjacent(len(current.adjacents))
                for a in current.adjacents:
                    if not a.node.visited:
                        a.node.visited = True
                        self.border.insert(a)
                self.border.toString()
                if self.border.getSuccessor() is not None:
                    AStar.search(self, self.border.getSuccessor())
            return
        AStar.search(self, self.border.getSuccessor())