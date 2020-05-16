# 2019-2020 Programação 2 (LTI)
# Grupo 12
# 55373 José Almeida
# 55371 Augusto Gouveia


class Connection:
    def __init__(self, src, dest):
        """
        Requires: src and dst Nodes
        """
        self._src = src
        self._dest = dest
        hoursInADay = 24
        self._weight = (dest.getFitness() / src.getAge()) * hoursInADay

    def getSource(self):
        return self._src

    def getDestination(self):
        return self._dest

    def getWeight(self):
        return self._weight

    def __str__(self):
        return self.getSource().getName() + '->(' + str(self.getWeight()) + ')' \
               + self.getDestination().getName()

    # when handed a Connection object, SocialNetwork must add it reciprocally
    # between source and destination given that we're working with a graph.
