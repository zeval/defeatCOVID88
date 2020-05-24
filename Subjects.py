# 2019-2020 Programação 2 (LTI)
# Grupo 12
# 55373 José Almeida
# 55371 Augusto Gouveia


class Subjects:
    def __init__(self, fileName):
        self._pairs = []
        inputFile = open(fileName, "r", encoding="utf-8")

        fileContent = inputFile.readlines()

        for line in fileContent:
            birds = line.strip().split(" ")
            assert len(birds) == 2, "Error: Badly formed subjects file. " \
                                    "Please double-check your subjects file and try again."
            pair = (birds[0], birds[1])
            self.addSubjects(pair)

    def addSubjects(self, birds):
        self._pairs.append(birds)

    def items(self):
        """
        Supports iteration over the current instance
        """
        for elem in self._pairs:
            yield elem

    def __str__(self):
        output = ""
        for pair in self.items():
            output += pair[0] + "<-->" + pair[1] + "\n"
        return output
