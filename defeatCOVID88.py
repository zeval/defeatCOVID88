# 2019-2020 Programação 2 (LTI)
# Grupo 12
# 55373 José Almeida
# 55371 Augusto Gouveia

import sys
from os import path
from SocialNetwork import SocialNetwork
from Subjects import Subjects


def calculate(networkFile, interactionsFile, outputFilename):
    """
    Calls functions required to output the program's results.
    Requires: networkFile, interactionsFile and outputFilename
    are strings, each representing the network/interactions/output
    file names, respectively.
    Ensures: an output file containing the desired data as indicated
    in the project sheet.
    """
    socialNetwork = SocialNetwork(networkFile) 
    subjectList = Subjects(interactionsFile)

    socialNetwork.writeFile(subjectList, outputFilename)


# Part of error detection is done here. Try/catch used to check validity of arguments
try:
    networkFileName, interactionsFileName, outputFile = sys.argv[1:]

    # Error raised if files mentioned in arguments don't exist in directory.
    if not path.isfile(networkFileName) or not path.isfile(interactionsFileName):
        raise FileNotFoundError

    calculate(networkFileName, interactionsFileName, outputFile)

except FileNotFoundError:
    print("Error: File not found. Double-check your input and try again.")
except ValueError as error:
    print("Error: Two input files are needed. You must also specify the output file's name. Double-check your input and try again.")