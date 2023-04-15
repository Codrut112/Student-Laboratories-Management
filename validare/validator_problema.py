from erori.validation_error import ValidError
from validare.validator_data import Validator_data
class ValidatorProblema:
    def __init__(self):
        pass
    def valideaza(self,problema):
        '''
        verifica daca o problema este valida
        :param problema: problema
        :return: ValidErori(erori) daca problema este invalida
        '''
        erori=""
        validator=Validator_data()
        if problema.get_id_problema()<0:
            erori+="id invalid!\n"
        if problema.get_numar_problema()<0:
            erori+="numar problema invalid!\n"
        if problema.get_descriere()=="":
            erori+="descriere invalida!\n"
        if problema.get_laborator()<0:
            erori+="laborator invalid!\n"
        if validator.valideaza(problema.get_deadline())==False:
            erori+="deadline invalid!\n"
        if len(erori)>0:
            raise ValidError(erori)
