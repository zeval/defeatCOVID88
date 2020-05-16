class Connection(object):
    def __init__(self, src, dest):
        """
        Requires: src and dst Nodes
        """
        self.src = src
        self.dest = dest
        hoursInADay = 24
        self.weight = (dest.getFitness() / src.getAge()) * hoursInADay

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def getWeight(self):
        return self.weight

    def __str__(self):
        return self.getSource().getName() + '->(' + str(self.weight) + ')' \
               + self.getDestination().getName()

    # when handed a Connection object, SocialNetwork must add it reciprocally
    # between source and destination given that we're working with a graph.
