# 2019-2020 Programação 2 (LTI)
# Grupo 12
# 55373 José Almeida
# 55371 Augusto Gouveia

class Connection:
    def __init__(self, src, dest):
        """
        Unites two people (Person objects), representing a connection between them,
        complete with weight.
        Requires: src and dest are Person objects.
        Ensures: Connection object linking both Person objects and the connection's
        weight.
        """
        self._src = src
        self._dest = dest
        self._weight = (int(dest.getFitness()) / int(src.getAge()))

    def getSource(self):
        """
        Used to obtain src attribute of Connection.
        Ensures: a Person object representing the source of the connection. 
        """

        return self._src

    def getDestination(self):
        """
        Used to obtain dest attribute of Connection
        .
        Ensures: a Person object representing the destination of the connection. 
        """

        return self._dest

    def getWeight(self):
        """
        Used to obtain weight attribute of Connection.
        Ensures: a Person object representing the weight of the connection. 
        """

        return self._weight

    def __str__(self):
        """
        Printable representation of Connection.
        Ensures: a string representing the connection, 
        stating source, weight and destination.
        """
        return self.getSource().getName() + '->(' + str(self.getWeight()) + ')' \
               + self.getDestination().getName()