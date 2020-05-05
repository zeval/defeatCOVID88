# 2019-2020 Programação II (LTI)
# Grupo 12
# 55373 José Almeida
# 55371 Augusto Gouveia


import copy


class Person:
    def __init__(self, name=None, idnb=None, age=None, direct=None, fitness=None, immune=None):
        if direct is None:
            direct = []
        self._name = name
        self._idnb = idnb
        self._age = age
        self._direct = copy.deepcopy(direct)
        self._fitness = fitness
        self._immune = immune

    # Getters

    def getName(self):
        return self._name

    def getIdNb(self):
        return self._idnb

    def getAge(self):
        return self._age

    def getDirect(self):
        return self._direct

    def getFitness(self):
        return self._fitness

    def getImmune(self):
        return self._immune
