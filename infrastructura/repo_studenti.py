from erori.repo_error import RepoError


class RepoStudenti:
    '''
    aceasta clasa se ocupa cu gestionarea listei de studenti
    '''
    def __init__(self):
        self._studenti={}
    def adauga_student(self,student):
        '''
        adauga un student in aplicatie
        :param student: student
        :return:
        '''
        if student.get_id_student() in self._studenti:
            raise RepoError("student existent!")
        self._studenti[student.get_id_student()]=student
    def sterge_student_dupa_id(self,id_student):
        '''
        sterege un student dupa id
        :param id_student: int
        :return: -
        '''
        student=self._studenti[id_student]
        if id_student not in self._studenti or student.sters==True:
            raise RepoError("student inexistent!")
        del self._studenti[id_student]
    def cauta_student_dupa_id(self,id_student):
        '''
        returneaza studentul cu idul id_student
        :param id_student: int
        :return: -
        '''

        if id_student not in self._studenti or self._studenti[id_student].sters==True:
            raise RepoError("student inexistent!")
        return self._studenti[id_student]
    def modifica_student(self,student):
        '''
        modifica datele unui student
        :param student: Student
        :return: -
        '''
        if student.get_id_student() not in self._studenti or student.sters==True:
            raise RepoError("student inexistent!")
        self._studenti[student.get_id_student()]=student
    def get_all(self):
        '''
        returneaza lista de studenti
        :return: list
        '''
        studenti=[]
        for student_id in self._studenti:
            if self._studenti[student_id].sters==False:
                studenti.append(self._studenti[student_id])


        return studenti
    def __len__(self):
        '''
        returneaza numarul de student din aplicatie
        :return: int
        '''
        studenti = []
        for student_id in self._studenti:
            if self._studenti[student_id].sters == False:
                studenti.append(self._studenti[student_id])
        return (len(studenti))




