class Student:
    '''
    aceasta clasa gestioneaza obiectul student
    '''
    def __init__(self,id_student,nume,grup):
        self.__id_student=id_student
        self.__nume=nume
        self.__grup=grup
        self.sters= False

    def sterge(self):
        '''
        seteaza studentul ca fiind sters
        :return: -
        '''

        self.sters= True
    def get_id_student(self):
        """
        returneaza idul studentului
        :return: int
        """
        return self.__id_student
    def get_nume(self):
        '''
        returneaza numele studentului
        :return: str
        '''
        return self.__nume
    def set_nume(self,nume):
        """
        seteaza un nou nume pentru student
        :param nume: str
        :return: -
        """
        self.__nume=nume
    def get_grup(self):
        '''
        returneaza grupul din care face parte studentul
        :return: int
        '''
        return self.__grup
    def set_grup(self,grup):
        '''
        seteaza noul grup al studentului
        :param grup: int
        :return: -
        '''
        self.__grup=grup
    def __eq__(self, other):
        """
        verifica daca doi studenti au acelasi id
        :param other: student
        :return: True daca cei doi studenti au acelasi id
                 False in caz contrar
        """

        return self.get_id_student()==other.get_id_student()
    def __str__(self):
        '''
        functie pentru afisare
        :return: datele studentului
        '''
        return f"{self.__id_student},{self.__nume},{self.__grup}"
    def stare(self):
        '''
        verifca daca studentul este marcat ca sters
        :return: True daca studentul este sters
                 False in caz contrar
        '''
        return self.sters

