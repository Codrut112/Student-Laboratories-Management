class Problema:
    def __init__(self,id_problema,laborator,numar_problema,descriere,deadline):
        self.__id_problema=id_problema
        self.__laborator=laborator
        self.__numar_problema=numar_problema
        self.__descriere=descriere
        self.__deadline=deadline

    def get_id_problema(self):
        '''
        returneaza idul problemei
        :return: int
        '''
        return self.__id_problema
    def get_laborator(self):
     """
     reurneaza laboratorul din care face parte problema
     :return: int
     """""
     return self.__laborator
    def get_numar_problema(self):
        '''
        returneaz numar problemei
        :return: int
        '''
        return self.__numar_problema
    def get_descriere(self):
        '''
        returneaza descrierea problemei
        :return: str
        '''
        return self.__descriere
    def get_deadline(self):
        """
        returneaza data la care problema trebbuie terminata
        :return: list
        """
        return self.__deadline
    def set_laborator(self,laborator):
        """
        seteaza laboratorul din care face parte problema
        :param laborator: int
        :return: -
        """

        self.__laborator=laborator
    def set_numar_problema(self,numar_problema):
        '''
        seteaza numarul problemei
        :param numar_problema:int
        :return: -
        '''
        self.__numar_problema=numar_problema
    def set_descriere(self,descriere):
        '''
        seteaza descrierea problemei
        :param descriere: str
        :return: -
        '''
        self.__descriere=descriere
    def set_deadline(self,deadline):
        '''
        seteaz un nou deadline pentru problema
        :param deadline: list
        :return: -
        '''
        self.__deadline=deadline
    def __str__(self):
        '''
        returneaza problema, prin acesta metoda se face accesarea problemei din exterior
        :return: problema
        '''
        return f"{self.__id_problema},{self.__laborator},{self.__numar_problema},{self.__descriere},{self.__deadline}"
    def __eq__(self, other):
        """
        verifica daca doua probleme sunt egale
        :param other: problema
        :return: True-daca cele doua probleme sunt egale
                 False-daca cele doua probleme sunt diferite
        """
        return self.__id_problema==other.__id_problema
