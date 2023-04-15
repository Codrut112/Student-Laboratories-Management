from erori.repo_error import RepoError
class RepoProbleme:
    def __init__(self):
        self._probleme={}

    def adauga_problema(self,problema):
        '''
        aduaga o problema in lista de probleme
        :param problema: problema
        :return: -
        '''
        if problema.get_id_problema() in self._probleme:
            raise RepoError("problema existenta!")
        self._probleme[problema.get_id_problema()]=problema

    def sterge_problema_dupa_id(self,id_problema):
        """
        sterge o problema dein lista de probleme
        :param id_problema: int
        :return: -
        """
        if id_problema not in self._probleme:
            raise RepoError("problema inexistenta")
        del self._probleme[id_problema]
    def cauta_problema_dupa_id(self,id_problema):
        '''
        returneaza o problema cu idul id_problema
        :param id_problema: int
        :return: problema
        '''
        if id_problema not in self._probleme:
            raise RepoError("problema inexistenta!")
        return self._probleme[id_problema]
    def modifica_problema(self,problema):
        '''
        modifica o problema
        :param problema: problema
        :return: -
        '''
        if problema.get_id_problema() not in self._probleme:
            raise RepoError("problema inexistenta")
        self._probleme[problema.get_id_problema()]=problema

    def get_all(self):
        '''
        returneaza lista de probleme
        :return: list
        '''
        probleme = []
        for problema_id in self._probleme:
            probleme.append(self._probleme[problema_id])

        return probleme

    def __len__(self):
        '''
        returneaza numarul de probleme
        :return: int
        '''
        return len(self._probleme)