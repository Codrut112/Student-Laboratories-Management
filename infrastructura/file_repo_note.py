from domeniu.nota import Nota
from infrastructura.repo_note import RepoNote

class FileRepoNote(RepoNote):
    def __init__(self,calea_catre_fisier):
        RepoNote.__init__(self)
        self.__calea_catre_fisier=calea_catre_fisier
    def read_all_from_file(self):
        with open(self.__calea_catre_fisier,"r") as f:
            lines=f.readlines()
            self._note.clear()
            for line in lines:

                if line!="":
                    line=line.strip()
                    parti=line.split(",")

                    id_nota=int(parti[0])
                    id_student=int(parti[1])
                    id_problema=int(parti[2])
                    valoare_nota=float(parti[3])
                    nota=Nota(id_nota,id_student,id_problema,valoare_nota)
                    self._note[id_nota]=nota
    def write_all_to_file(self):
        with open(self.__calea_catre_fisier,"w") as f:
            for nota in self._note.values():

                f.write(str(nota) +"\n")

    def adauga_nota(self,nota):
        self.read_all_from_file()
        RepoNote.adauga_nota(self,nota)
        self.write_all_to_file()
    def modifica_nota(self,nota):
        self.read_all_from_file()
        RepoNote.modifica_nota(self,nota)
        self.write_all_to_file()
    def get_all(self):
        self.read_all_from_file()
        return RepoNote.get_all(self)
    def sterge_nota(self,id_nota):
        self.read_all_from_file()
        RepoNote.sterge_nota(self,id_nota)
        self.write_all_to_file()
    def cauta_nota_dupa_id(self,id_nota):
        self.read_all_from_file()
        return RepoNote.cauta_nota_dupa_id(self,id_nota)

    def __len__(self):
        self.read_all_from_file()
        return RepoNote.__len__(self)

    def clear(self):
        with open(self.__calea_catre_fisier,"w") as f:
            pass






