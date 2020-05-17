# 2019-2020 Programação 2 (LTI)
# Grupo 12
# 55373 José Almeida
# 55371 Augusto Gouveia


import sys
from os import path
# from Person import Person
from SocialNetwork import SocialNetwork
from Subjects import Subjects


def calculate(networkFile, interactionsFile):
    socialNetwork = SocialNetwork(networkFile)
    subjectList = Subjects(interactionsFile)
    print(socialNetwork)
    print(subjectList)


try:
    networkFileName, interactionsFileName = sys.argv[1:]
    if path.isfile(networkFileName) and path.isfile(interactionsFileName):
        calculate(networkFileName, interactionsFileName)
    else:
        raise FileNotFoundError
except FileNotFoundError:
    print("Error: File not found. Double-check your input and try again.")
except ValueError as error:
    print("Error: Two input files are needed. Double-check your input and try again.")
except AssertionError as error:
    print("Error: " + str(error))
