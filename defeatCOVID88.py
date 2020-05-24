# 2019-2020 Programação 2 (LTI)
# Grupo 12
# 55373 José Almeida
# 55371 Augusto Gouveia


import sys
from os import path
# from Person import Person
from SocialNetwork import SocialNetwork
from Subjects import Subjects


def calculate(networkFile, interactionsFile, outputFileName):
    socialNetwork = SocialNetwork(networkFile)
    subjectList = Subjects(interactionsFile)
    # print(socialNetwork)
    # print(subjectList)
    # for subjectA, subjectB in subjectList.items():
    #     print(socialNetwork.search(subjectA, subjectB))
    socialNetwork.writeFile(subjectList, outputFileName)


try:
    networkFileName, interactionsFileName, outputFile = sys.argv[1:]

    if not path.isfile(networkFileName) or not path.isfile(interactionsFileName):
        raise FileNotFoundError

    calculate(networkFileName, interactionsFileName, outputFile)

except FileNotFoundError:
    print("Error: File not found. Double-check your input and try again.")
except ValueError as error:
    print("Error: Two input files are needed. You must also specify the output file's name. Double-check your input and try again.")
except AssertionError as error:
    print("Error: " + str(error))
