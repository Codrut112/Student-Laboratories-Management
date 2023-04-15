
from domeniu.problema import Problema
class ServiceProbleme:
    '''
    aceasta clasa se ocupa cu gestionarea problemelor
    '''
    def __init__(self,validator_problema,repo_probleme):
        self.__validator_problema=validator_problema
        self.__repo_probleme=repo_probleme

    def __len__(self):
        return self.__repo_probleme.__len__()

    def adauga_problema(self, id_problema,laborator,numar_problema,descriere,deadline):
        '''
        aduga o problema in aplicatie
        :param id_problema: int
        :param laborator: int
        :param numar_problema:int
        :param descriere: str
        :param deadline: list
        :return: -
        '''
        problema =Problema(id_problema,laborator,numar_problema,descriere,deadline)

        self.__validator_problema.valideaza(problema)
        self.__repo_probleme.adauga_problema(problema)
    def modifica_problema(self, id_problema,laborator,numar_problema,descriere,deadline):
        """
        modifica o problema
        :param id_problema: int
        :param laborator: int
        :param numar_problema: int
        :param descriere: str
        :param deadline: list
        :return: -
        """
        problema = Problema(id_problema, laborator, numar_problema, descriere, deadline)
        self.__validator_problema.valideaza(problema)
        self.__repo_probleme.modifica_problema(problema)
    def get_all_probleme(self):
        '''
        returneaza toate problemele
        :return: list
        '''
        return self.__repo_probleme.get_all()
    def cauta_problema_dupa_id(self,id_problema):
        '''
        cauta o problema dupa id si o returneaza daca exista
        :param id_problema: int
        :return: problema
        '''
        return self.__repo_probleme.cauta_problema_dupa_id(id_problema)
