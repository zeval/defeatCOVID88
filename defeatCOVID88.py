# 2019-2020 Programação 2 (LTI)
# Grupo 12
# 55373 José Almeida
# 55371 Augusto Gouveia


import sys
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
    calculate(networkFileName, interactionsFileName)
except FileNotFoundError:
    print("Error: File not found. Double-check your input and try again.")
except ValueError:
    print("Error: Two input files required. Double-check if you input two files and try again.")
except AssertionError as error:
    print(error)
