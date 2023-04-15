from domeniu.problema import Problema
from infrastructura.repo_probleme import RepoProbleme


class FileRepoProbleme(RepoProbleme):
    def __init__(self,calea_catre_fisier):
        RepoProbleme.__init__(self)
        self.__calea_catre_fisier=calea_catre_fisier
    def read_all_from_file(self):
        with open(self.__calea_catre_fisier,"r") as f:
            lines=f.readlines()
            self._probleme.clear()
            for line in lines:

                if line!="":
                    line = line.strip()
                    parti=line.split(",")

                    id_problema=int(parti[0])
                    laborator=int(parti[1])
                    numar_problema=int(parti[2])
                    descriere=parti[3]
                    deadline=parti[4][1:]
                    lenn=len(deadline)

                    deadline=deadline[0:(lenn-2)]

                    zi_deadline=int(parti[4][1:])
                    luna_deadline=int(parti[5])
                    an_deadline=int(parti[6][0:len(parti[6])-1])
                    deadline=[zi_deadline,luna_deadline,an_deadline]
                    problema=Problema(id_problema,laborator,numar_problema,descriere,deadline)
                    self._probleme[id_problema]=problema
    def write_all_to_file(self):
        with open(self.__calea_catre_fisier,"w") as f:
            for problema in self._probleme.values():
                f.write(str(problema)+"\n")
    def adauga_problema(self,problema):
        self.read_all_from_file()
        RepoProbleme.adauga_problema(self,problema)
        self.write_all_to_file()
    def sterge_problema_dupa_id(self,id_problema):
        self.read_all_from_file()
        RepoProbleme.sterge_problema_dupa_id(self,id_problema)
        self.write_all_to_file()
    def get_all(self):
        self.read_all_from_file()
        return RepoProbleme.get_all(self)
    def __len__(self):
        self.read_all_from_file()
        return RepoProbleme.__len__(self)
    def cauta_problema_dupa_id(self,id_problema):
        self.read_all_from_file()
        return RepoProbleme.cauta_problema_dupa_id(self,id_problema)
    def modifica_problema(self,problema):
        self.read_all_from_file()
        RepoProbleme.modifica_problema(self,problema)
        self.write_all_to_file()
    def clear(self):
        with open(self.__calea_catre_fisier,"w") as f:
            pass



