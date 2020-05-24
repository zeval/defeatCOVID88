# 2019-2020 Programação 2 (LTI)
# Grupo 12
# 55373 José Almeida
# 55371 Augusto Gouveia

from Person import Person
from Connection import Connection

hoursInADay = 24


class SocialNetwork:
    def __init__(self, fileName):
        """
        Integrates multiple connections (Connection objects) and persons (Person objects),
        in order to assemble a network. 
        Requires: fileName is a string representing the social network input file's name.
        Ensures: graph-like structure including all Person nodes and connections between them.
        """

        self._users = []
        self._connections = {}
        inputFile = open(fileName, "r", encoding="utf-8")

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
                    newConnection = Connection(person, contactObject)
                    self.addConnection(newConnection)
                    self.reverseConnection(newConnection)

    def contactInNetwork(self, query):
        """
        Identifies contact in network.
        Requires: query is a string representing either a name or an IdNb.
        Ensures: None if person isn't in network. Person object if a valid 
        user is found based on query submitted.
        """
        if query[:3] == "cvd":
            for person in self._users:
                if person.getIdNb() == query:
                    return person
        else:
            for person in self._users:
                if person.getName() == query:
                    return person
        return None

    def setUsers(self, users):
        """
        Setter for the users list.
        Requires: users is a list containing the various Person-type objects.
        Ensures: Updated users list.
        """
        self._users = users

    def setConnections(self, connections):
        """
        Setter for the connections dictionary.
        Requires: connections is a dictionary, containing Person-type objects as key and words.
        Ensures: Updated connections dictionary.
        """
        self._connections = connections

    def getUsers(self):
        """
        Getter for the users list.
        Ensures: A copy of the social network's users list.
        """
        return self._users.copy()

    def getConnections(self):
        """
        Getter for the connections dictionary.
        Ensures: A copy of the social network's connections dictionary.
        """
        return self._connections.copy()

    def addPerson(self, person):
        """
        Adds new person to list of users in network.
        Requires: person is a Person object not already in network.
        Ensures: Person object is added to self._users if not there
        already. Error is raised if person is already in network.
        """
        if self.contactInNetwork(person.getIdNb()) is None:
            self._users.append(person)
            self._connections[person] = []
        else:
            raise AssertionError('Duplicate person')

    def addConnection(self, connection):
        """
        Adds new connection to list of connections.
        Requires: connection is a Connection object.
        Ensures: new connection is added to self._connections.
        """
        src = connection.getSource()
        dest = connection.getDestination()
        weight = connection.getWeight()

        self._connections[src].append((dest, weight))

    def reverseConnection(self, connection):
        """
        Takes new connection and adds the reverse connection.
        Necessary so that SocialNetwork is a graph-like structure
        and not a digraph-like structure.
        Requires: connection is a Connection object.
        Ensures: reverse connection is added to self._connections.
        """
        # Adding reverse connection

        revConnection = Connection(connection.getDestination(), connection.getSource())

        self.addConnection(revConnection)

    def inNetwork(self, person):
        """
        Checks if given person in the network.
        Requires: person is a Person object.
        Ensures: boolean value stating if person is included in self._users.
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
        Returns everyone the person is in direct contact with.
        Requires: person is a Person object.
        Ensures: list of Person objects in direct contact with
        the provided Person object.
        """

        return self._connections[person]

    def printPath(self, path):
        """
        Prints a given path in an easy-to-read way.
        Requires: path is a list of Person objects.
        Ensures: easy-to-read string with the name of each Person object,
        in the correct order.
        """
        result = ''
        for i in range(len(path)):
            result = result + path[i].getName()
            if i != len(path) - 1:
                result = result + '->'
        return result

    def totalWeight(self, path):
        """
        Works over a given path to return the sum of the weight of it's connections.
        Requires: path is a list of Person objects.
        Ensures: int representing the sum of the path's weight.
        """
        weightCounter = 0
        for person in range(len(path) - 1):
            for dest, weight in self._connections[path[person]]:
                if dest == path[person + 1]:
                    weightCounter += weight
        return weightCounter

    def DFS(self, start, end, path, shortest):
        """
        Performs a depth-first-search on the social network.
        Requires: start and end are Person objects, path and shortest are lists of Person objects.
        Ensures: the path with the least weight between all of the available paths between start 
        and end Person objects.
        """
        path = path + [start]
    
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
        Simplified DFS function-call for ease-of-use.
        Requires: start and end are strings representing people.
        Ensures: string representing an adapted output of DFS result.
        """

        startPerson = self.contactInNetwork(start)
        endPerson = self.contactInNetwork(end)

        if startPerson is None:
            return "{} out of the social network".format(start)

        if endPerson is None:
            return "{} out of the social network".format(end)

        if startPerson.getImmune() or endPerson.getImmune():
            return "No contagion between " + startPerson.getName() + " and " + endPerson.getName()

        finalPath = self.DFS(startPerson, endPerson, [], None)
        if finalPath is None:
            return "No contagion between " + startPerson.getName() + " and " + endPerson.getName()
        return str(round(self.totalWeight(finalPath) * hoursInADay))

    def writeFile(self, subjectList, fileName):
        """
        Outputs self.search() results to a file.
        Requires: subjectList is a Subject collection (object) containing 
        the various pairs to be tested. fileName is a string representing
        the desired name of the output file.
        Ensures: file containing search results for every pair is created 
        using fileName as it's name.
        """
        outputFile = open(fileName, "w", encoding="utf-8")
        for subjectA, subjectB in subjectList.items():
            outputFile.write(self.search(subjectA, subjectB) + "\n")
        outputFile.close()

    # *****************************

    def __str__(self):
        output = ""
        for person in self._users:
            output += person.getName() + " has contact with: \n"
            if len(self._connections) > 0:
                for contact, weight in self._connections[person]:
                    output += contact.getName() + ' (' + str(weight) + ')' + "\n"
        return output
