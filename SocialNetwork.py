# 2019-2020 Programação 2 (LTI)
# Grupo 12
# 55373 José Almeida
# 55371 Augusto Gouveia

from Person import Person


class SocialNetwork:
    def __init__(self, fileName):
        self._network = []
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

    def __str__(self):
        output = ""
        for person in self.items():
            output += str(person) + "\n"
        return output

    def addPerson(self, person):
        self._network.append(person)

    def items(self):
        """
        Supports iteration over the current instance
        """
        for elem in self._network:
            yield elem

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
