class Note_problema_cresc:
    """
    realizeaza sortarea unui list de studenti pe baza notelor la o problema
    """
    def __init__(self,nume_student,nota_student):
        self.__nume_student=nume_student
        self.__nota_student=nota_student
    def __str__(self):
        '''
        returneaza numele studentului si nota sa
        :return: string
        '''
        return f"student {self.__nume_student} cu nota {self.__nota_student}"
    def __lt__(self, other):
        """
        realizeaza sortarea pe baza notei in ordine crescatoare
        :param other: student
        :return: bool
        """
        return self.__nota_student < other.__nota_student
    def get_nume(self):
        return self.__nume_student
    def get_nota(self):
        return self.__nota_student
    def __eq__(self, other):
        """
           verifica echivalenta a doua note
           :param other: Note_problema_cresc
           :return: bool
           """
        return self.__nume_student==other.__nume_student and self.__nota_student==other.__nota_student
