# 2019-2020 Programação 2 (LTI)
# Grupo 12
# 55373 José Almeida
# 55371 Augusto Gouveia


class Subjects:
    """
    Lists all test-pairs in an easily accessible way.
    Requires: fileName is a string representing the subject file's name.
    Ensures: Subjects object linking two person names as a pair to be tested.
    """
    def __init__(self, fileName):
        self._pairs = []
        inputFile = open(fileName, "r", encoding="utf-8")

        fileContent = inputFile.readlines()

        for line in fileContent:
            subjects = line.strip().split(" ")
            assert len(subjects) == 2, "Badly formed subjects file. " \
                                    "Please double-check your subjects file and try again."

            assert subjects[0] != subjects[1], "Same person mentioned twice in the same line of subjects file. " \
                                         "Please double-check your subjects file and try again."

            pair = (subjects[0], subjects[1])
            self.addSubjects(pair)

    def addSubjects(self, subjects):
        """
        Used to add a new subject pair to the list of pairs.
        Requires: subjects is a list containing two strings.
        Ensures: new pair is added to self._pairs.
        """
        self._pairs.append(subjects)

    def items(self):
        """
        Supports iteration over the current instance.
        """
        for elem in self._pairs:
            yield elem

    def __str__(self):
        """
        Printable representation of a Subjects object.
        Ensures: string including all pairs displayed in an easy-to-read way.
        """
        output = ""
        for pair in self.items():
            output += pair[0] + "<-->" + pair[1] + "\n"
        return output
