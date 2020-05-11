# # 2019-2020 Programação 2 (LTI)
# # Grupo 12
# # 55373 José Almeida
# # 55371 Augusto Gouveia
#
# from Person import Person
#
#
# def socialNetworkReader(fileName):
#     """
#
#     """
#
#     inputFile = open(fileName, "r")
#
#     fileContent = inputFile.readlines()
#     fileContent = fileContent[1:]
#
#     personList = []
#
#     for line in fileContent:
#         userDetails = line.strip().split(", ")
#         print(userDetails)
#         name = userDetails[0]
#         idNb = userDetails[1]
#         age = userDetails[2]
#         fitness = userDetails[-2]
#         immune = userDetails[-1]
#
#         # organizing direct array
#         direct = userDetails[3:-2]
#         direct = [element.strip("<>") for element in direct]
#         print(direct)
#
#         # creating Person object
#
#         personObject = Person(name, idNb, age, direct, fitness, immune)
#         print (personObject)
#         personList.append(personObject)
#
#     return personList
#
#
#
# personList = socialNetworkReader("socialNetwork.txt")
#
# # for person in personList:
# #     print(person.getName(), person.getIdNb(), person.getAge(), person.getDirect(), person.getFitness(), person.getImmune())
