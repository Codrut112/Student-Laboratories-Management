from erori.validation_error import ValidError

class ValidatorNota:
    def __init__(self):
        pass
    def valideaza(self,nota):
        '''
        verifica daca o nota este valida
        :param nota: nota
        :return: raiseValidError daca nota este invalida
        '''


        erori = ""

        if nota.get_id_student()<0:
            erori+="id_student invalid"
        if nota.get_id_problema()<0:
            erori+="id_nota invalid"
        if nota.get_id_nota()<0:
            erori+="id invalid!"
        if nota.get_nota()!="lab_asignat":
            if nota.get_nota()<1 or nota.get_nota()>10 :
                erori+="nota invalida\n"
        if(len(erori)>0):
            raise ValidError(erori)