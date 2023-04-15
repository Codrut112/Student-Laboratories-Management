from erori.repo_error import RepoError


class RepoNote:
    """
    reponote gestioneaza lista de note
    """
    def __init__(self):
        self._note={}
    def get_all(self):
        '''
        retunreaza lista de note
        :return: list
        '''
        note=[]
        for nota_id in self._note:
            note.append(self._note[nota_id])

        return note
    def adauga_nota(self,nota):
        '''
        adauga o nota in aplicatie
        :param nota: float
        :return: -
        '''

        if nota.get_nota() == "lab_asignat":
            self._note[nota.get_id_nota()] = nota
            return
        if nota.get_id_nota() in self._note :
            raise RepoError("nota existenta!")
        self._note[nota.get_id_nota()]=nota
    def sterge_nota(self,id_nota):
        '''
        sterge o nota din aplicatie pe baza idului
        :param id_nota: int
        :return: -
        '''
        if id_nota not in self._note:
            raise RepoError("nota inexistenta")
        del self._note[id_nota]

    def cauta_nota_dupa_id(self,id_nota):
        '''
        cauta nota dupa id
        :param id_nota: int
        :return: nota
        '''
        if id_nota not in self._note:
            raise RepoError("nota inexistenta")
        return self._note[id_nota]
    def modifica_nota(self,nota):
        '''
        modifca o nota
        :param nota: nota
        :return: -
        '''
        if nota.get_id_nota() not in self._note:
            raise RepoError("nota inexistenta")
        self._note[nota.get_id_nota()]=nota
    def __len__(self):
        return len(self._note)
