# 2019-2020 Programação 2 (LTI)
# Grupo 12
# 55373 José Almeida
# 55371 Augusto Gouveia


class Connections:
    def __init__(self, fileName):
        self._connections = []
        inputFile = open(fileName, "r")

        fileContent = inputFile.readlines()

        for line in fileContent:
            birds = line.strip().split(" ")
            assert len(birds) == 2, "Error: Badly formed connections file. PLease double-check your connections file" \
                                    " and try again."
            connection = birds[0] + " --> " + birds[1]
            self.add(connection)

    def __str__(self):
        output = ""
        for connection in self.items():
            output += connection + "\n"
        return output

    def add(self, birds):
        self._connections.append(birds)

    def items(self):
        """
        Supports iteration over the current instance
        """
        for elem in self._connections:
            yield elem
