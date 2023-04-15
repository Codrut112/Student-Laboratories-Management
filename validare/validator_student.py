from erori.validation_error import ValidError


class ValidatorStudent:
    def __init__(self):
        pass
    def valideaza(self,student):
        '''
        verifica daca studentul are datele valide
        :param student: student
        :return: ValidError daca studentul este invalid
        '''
        erori=""
        if student.sters==True:
            erori += "student inexistent!\n"

        if student.get_id_student()<0:
            erori+="id invalid!\n"
        if student.get_grup()<0:
            erori+="grup invalid!\n"
        if student.get_nume()=="":
            erori+="nume invalid!\n"

        if len(erori)>0:
            raise ValidError(erori)


