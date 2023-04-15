import random
import string
from domeniu.student import Student
class ServiceStudenti:
    """
    aceacta clasa se ocupa cu gestionarea studentilor
    """

    def __init__(self,validator_student,repo_studenti):
        self.__validator_student=validator_student
        self.__repo_studenti=repo_studenti
    def adauga_student(self,id_student,nume,grup):
        '''
        adauga un student in aplicatie
        :param id_student: int
        :param nume: str
        :param grup: int
        :return: -
        '''
        student=Student(id_student,nume,grup)

        self.__validator_student.valideaza(student)
        self.__repo_studenti.adauga_student(student)
    def get_all_studenti(self):
        '''
        returneaza toti studenti din aplicatie
        :return: list
        '''
        return self.__repo_studenti.get_all()

    def modifica_student(self,id_student,nume,grup):
        """
        modifica datele unui student
        :param id_student: int
        :param nume: string
        :param grup: int
        :return: -
        """
        student=Student(id_student,nume,grup)
        self.__validator_student.valideaza(student)
        self.__repo_studenti.modifica_student(student)
    def cauta_student_dupa_id(self,id_student):
        """
        cauta studentul cu idul id_student
        :param id_student: int
        :return: student
        """
        return self.__repo_studenti.cauta_student_dupa_id(id_student)
    def __len__(self):
        """
        returneaza numarul de studenti in aplicatie
        :return: list
        """
        return self.__repo_studenti.__len__()
    def create_random_id(self):
        '''
        creaza un id random
        :return: -
        '''
        return random.randint(1, 100000000000000000)

    def generate_nume(self,size):

        chars = string.ascii_lowercase
        return "".join(random.choice(chars) for _ in range(size))


