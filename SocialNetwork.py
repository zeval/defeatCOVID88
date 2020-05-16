# 2019-2020 Programação 2 (LTI)
# Grupo 12
# 55373 José Almeida
# 55371 Augusto Gouveia

from Person import Person


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
            age = userDetails[2]
            fitness = userDetails[-2]
            immune = userDetails[-1]

            # organizing direct array
            direct = userDetails[3:-2]
            direct = [element.strip("<>") for element in direct]

            # creating Person object and adding it to the social network

            self.addPerson(Person(name, idNb, age, direct, fitness, immune))

    def addPerson(self, person):
        self._users.append(person)

    def addConnection(self, connection):
        src = connection.getSource()
        dest = connection.getDestination()
        weight = connection.getWeight()

        if not (src in self._users and dest in self._users):
            raise ValueError("User not in network")

        self._connections[src].append((dest, weight))

        # Adding reverse edge
        self._connections[dest].append((src, weight))

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

    def __str__(self):
        output = ""
        for person in self._users:
            output += person + " has contact with: \n" 
            for contact in self._connections[person]:
                output += contact + "\n"
        return output


    # def readFile(self, fileName):
    #     inputFile = open(fileName, "r")
    #
    #     fileContent = inputFile.readlines()
    #     fileContent = fileContent[1:]
    #
    #     personList = []
    #
    #     for line in fileContent:
    #         userDetails = line.strip().split(", ")
    #
    #         name = userDetails[0]
    #         idNb = userDetails[1]
    #         age = userDetails[2]
    #         fitness = userDetails[-2]
    #         immune = userDetails[-1]
    #
    #         # organizing direct array
    #
    #         direct = userDetails[3:-2]
    #         direct = [element.strip("<>") for element in direct]
    #
    #         # creating Person object
    #
    #         self.add(Person(name, idNb, age, direct, fitness, immune))
