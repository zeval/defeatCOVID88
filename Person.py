# 2019-2020 Programação 2 (LTI)
# Grupo 12
# 55373 José Almeida
# 55371 Augusto Gouveia

from copy import deepcopy


class Person:
    """
    Creates object representing a person.
    Requires: name, idnb and immune are strings representing the person's
    name, ID number and immunity status, respectively. direct is a list
    containing the ID numbers of people this person is in direct contact with.
    age is an int representing the person's age and fitness is an int representing
    the person's fitness level, from 1 to 5.
    Ensures: Person object representing the person and it's attributes.
    """
    def __init__(self, name=None, idnb=None, age=None, direct=None, fitness=None, immune=None):
        if direct is None:
            direct = []
        self._name = name
        self._idnb = idnb
        self._age = age
        self._direct = deepcopy(direct)
        self._fitness = fitness
        if immune == "Yes":
            self._immune = True
        else:
            self._immune = False

    # Setters

    def setName(self, newName):
        """
        Allows for setting a new name.
        Requires: newName is a string representing the desired name.
        Ensures: self._name = newName.
        """

        self._name = newName

    def setIdNb(self, newIdNb):
        """
        Allows for setting a new ID number.
        Requires: newIdNb is a string representing the desired ID number.
        Ensures: self._idnb = newIdNb.
        """
        self._idnb = newIdNb

    def setAge(self, newAge):
        """
        Allows for setting a new age.
        Requires: newAge is an int representing the age.
        Ensures: self._age = newAge.
        """
        self._age = newAge

    def setDirect(self, newDirect):
        """
        Allows for setting a new direct list.
        Requires: newDirect is a list representing the person's close contacts.
        Ensures: self._direct = newDirect.
        """
        self._direct = newDirect

    def setFitness(self, newFitness):
        """
        Allows for setting a new fitness level.
        Requires: newFitness is an int representing the fitness leve.
        Ensures: self._fitness = newFitness.
        """

        self._fitness = newFitness

    def setImmune(self, newImmune):
        """
        Allows for setting a new immunity status.
        Requires: newImmune is an boolean value representing the immunity status.
        Ensures: self._immune = newImmune.
        """

        self._immune = newImmune
    

    # Getters

    def getName(self):
        """
        Used to obtain name attribute of Person.
        Ensures: a string representing the name of the person. 
        """
        return self._name

    def getIdNb(self):
        """
        Used to obtain idnb attribute of Person.
        Ensures: a string representing the ID number of the person.
        """
        return self._idnb

    def getAge(self):
        """
        Used to obtain age attribute of Person.
        Ensures: an int representing the age of the person.
        """
        return self._age

    def getDirect(self):
        """
        Used to obtain direct attribute of Person.
        Ensures: a list with the ID numbers of everyone in direct
        contact with the person.
        """
        return deepcopy(self._direct)

    def getFitness(self):
        """
        Used to obtain fitness attribute of Person.
        Ensures: an int representing the fitness level of the person.
        """
        return self._fitness

    def getImmune(self):
        """
        Used to obtain immune attribute of Person.
        Ensures: a string representing the immunity status of the person.
        """
        return self._immune

    def __str__(self):
        """
        Printable representation of a Person object.
        Ensures: string including all of the person's attributes in an easy-to-read way.
        """
        return "{}, {}, {}, <{}>, {}, {}".format(str(self._name), str(self._idnb), str(self._age),
        str(self._direct).replace("'","").replace("[","").replace("]",""), str(self._fitness), str(self._immune))
