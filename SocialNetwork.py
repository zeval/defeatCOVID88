# 2019-2020 Programação 2 (LTI)
# Grupo 12
# 55373 José Almeida
# 55371 Augusto Gouveia

from Person import Person
from Connection import Connection

hoursInADay = 24


class SocialNetwork:
    def __init__(self, fileName):
        self._users = []
        self._connections = {}
        inputFile = open(fileName, "r")

        fileContent = inputFile.readlines()
        fileContent = fileContent[1:]

        for line in fileContent:
            userDetails = line.strip().split(", ")
            name = userDetails[0]
            idNb = userDetails[1]
            age = int(userDetails[2])
            fitness = int(userDetails[-2])
            immune = userDetails[-1]

            # checking validity of person details provided

            assert age > 0, "{}'s age should be above 0.".format(name)
            assert 0 < fitness < 6, "{}'s fitness should be between 0 and 5.".format(name)

            # organizing direct array
            direct = userDetails[3:-2]
            direct = [element.strip("<>") for element in direct]

            # creating Person object and adding it to the social network

            self.addPerson(Person(name, idNb, age, direct, fitness, immune))

        inputFile.close()

        for person in self._users:
            for contactID in person.getDirect():

                contactObject = self.contactInNetwork(contactID)
                destinations = [dest for dest, weight in self._connections[person]]

                # If contact person not in network & if connection doesn't already exist
                if (contactObject is not None) and (contactObject not in destinations):
                    newConnection = Connection(person, self.contactInNetwork(contactID))
                    self.addConnection(newConnection)
                    self.reverseConnection(newConnection)
                # TODO: else add people not in network to list of people who suck

    def contactInNetwork(self, query):
        if query[:3] == "cvd":
            for person in self._users:
                if person.getIdNb() == query:
                    return person
        else:
            for person in self._users:
                if person.getName() == query:
                    return person
        return None

    def addPerson(self, person):
        if self.contactInNetwork(person.getIdNb()) is None:
            self._users.append(person)
            self._connections[person] = []
        else:
            raise AssertionError('Duplicate person')

    def addConnection(self, connection):
        src = connection.getSource()
        dest = connection.getDestination()
        weight = connection.getWeight()

        # if not (src in self._users and dest in self._users):
        #     raise ValueError("User not in network")

        self._connections[src].append((dest, weight))

    def reverseConnection(self, connection):
        # Adding reverse edge

        revConnection = Connection(connection.getDestination(), connection.getSource())

        self.addConnection(revConnection)

    def directContact(self, person):
        """
        Returns everyone the person is in direct contact with
        """
        return self._connections[person]

    def inNetwork(self, person):
        """
        Returns boolean value stating if person is included in the network
        """
        return person in self._users

    def itemsUsers(self):
        """
        Supports iteration over the current instance
        """
        for elem in self._users:
            yield elem

    def itemsConnections(self):
        """
        Supports iteration over the current instance
        """
        for elem in self._connections:
            yield elem

    def contactsOf(self, person):
        """

        """

        return self._connections[person]

    # *****************************
    # noinspection PyMethodMayBeStatic
    def printPath(self, path):
        """
        Requires: path a list of nodes
        """
        result = ''
        for i in range(len(path)):
            result = result + str(path[i])
            if i != len(path) - 1:
                result = result + '->'
        return result

    def totalWeight(self, path):
        weightCounter = 0
        for person in range(len(path) - 1):
            for dest, weight in self._connections[path[person]]:
                if dest == path[person + 1]:
                    weightCounter += weight
        return weightCounter

    def DFS(self, start, end, path, shortest):
        """
        Requires:
        start and end nodes;
        path and shortest lists of nodes
        Ensures:
        a shortest path from start to end in graph
        """
        path = path + [start]
        # print('Current DFS path:', self.printPath(path), self.totalWeight(path) * hoursInADay)
        if start == end:
            return path
        for person, weight in self.contactsOf(start):
            if person not in path and not person.getImmune():  # avoid cycles
                if shortest is None or self.totalWeight(path) < self.totalWeight(shortest):
                    newPath = self.DFS(person, end, path, shortest)
                    if newPath is not None and (
                            shortest is None or self.totalWeight(newPath) < self.totalWeight(shortest)):
                        shortest = newPath
        return shortest

    def search(self, start, end):
        """
        Requires:
        start and end are nodes
        Ensures:
        shortest path from start to end in graph
        """

        startPerson = self.contactInNetwork(start)
        endPerson = self.contactInNetwork(end)

        if startPerson is None:
            return "{} out of the network".format(start)

        if endPerson is None:
            return "{} out of the network".format(end)

        if startPerson.getImmune() or endPerson.getImmune():
            return "No contagion between " + str(startPerson) + " and " + str(endPerson)

        finalPath = self.DFS(startPerson, endPerson, [], None)
        if finalPath is None:
            return "No contagion between " + str(startPerson) + " and " + str(endPerson)
        return self.printPath(finalPath) + ", " + str(round(self.totalWeight(finalPath) * hoursInADay))

    # *****************************

    def visualDataExport(self):
        userNames = []
        connectionList = []
        for user in self._users:
            userNames.append(user.getName())

        for source in self._connections:
            destinationList = [dest for dest, weight in self._connections[source]]
            for destination in destinationList:

                connectionList.append((source.getName(), destination.getName()))
        return userNames, connectionList

    def __str__(self):
        output = ""
        for person in self._users:
            output += person.getName() + " has contact with: \n"
            if len(self._connections) > 0:
                for contact, weight in self._connections[person]:
                    output += contact.getName() + ' (' + str(weight) + ')' + "\n"
        return output
