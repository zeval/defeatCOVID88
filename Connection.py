class Connection(object):
    def __init__(self, src, dest):
        """
        Requires: src and dst Nodes
        """
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()

    # when handed a Connection object, SocialNetwork must add it reciprocally
    # between source and destination given that we're working with a graph.