class Nota:
    """
    prin intermediul acestei clasa s-a creat obiectul nota
    """
    def __init__(self, id_nota, id_student, id_problema, nota):
        self.__id_nota=id_nota
        self.__id_student=id_student
        self.__id_problema=id_problema
        self.__nota=nota
        self.__sters=False
    def get_id_problema(self):
        return self.__id_problema
    def get_sters(self):
        '''
        returneaza starea notei(daca este stearsa)
        :return: bool
        '''
        return self.__sters
    def get_nota(self):
        '''
        returneaza nota
        :return: flaot
        '''
        return self.__nota
    def sterge(self):
        """
        marcheaza nota ca fiind stearsa
        :return: -
        """
        self.__sters=True
    def get_id_student(self):
        """
        returneaza elevul la care i-a fost atribuita nota
        :return: student
        """
        return self.__id_student
    def get_id_nota(self):
        """
        returneaza idul notei
        :return:id
        """
        return self.__id_nota

    def __str__(self):
        '''
        functie pentru afisare
        :return: datele studentului
        '''
        return f"{self.__id_nota},{self.__id_student},{self.__id_problema},{self.__nota}"
    def __eq__(self, other):
        """
        returneaza True daca cele doua note au acelasi id,False in caz contrar
        :param other: nota
        :return: bool
        """
        return self.__id_nota==other.get_id_nota()
