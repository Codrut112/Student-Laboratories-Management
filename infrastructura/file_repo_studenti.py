from domeniu.student import Student
from infrastructura.repo_studenti import RepoStudenti

class FileRepoStudenti(RepoStudenti):
    def __init__(self,cale_catre_fisier):
        RepoStudenti.__init__(self)
        self.__cale_catre_fisier=cale_catre_fisier

    def read_all_from_file(self):
        with open(self.__cale_catre_fisier,"r") as f:
            lines=f.readlines()
            self._studenti.clear()
            for line in lines:
                if line!="":
                    line = line.strip()
                    parti = line.split(",")
                    id_student = int(parti[0])
                    nume = parti[1]
                    grup = parti[2]
                    student = Student(id_student, nume, grup)
                    self._studenti[id_student] = student
    def write_all_to_file(self):
        with open(self.__cale_catre_fisier,"w") as f:
            for student in self._studenti.values():
                f.write(str(student)+"\n")
    def adauga_student(self,student):
        self.read_all_from_file()
        RepoStudenti.adauga_student(self,student)
        self.write_all_to_file()
    def sterge_student_dupa_id(self,id_student):
        self.read_all_from_file()
        RepoStudenti.sterge_student_dupa_id(self,id_student)
        self.write_all_to_file()
    def get_all(self):
        self.read_all_from_file()
        return RepoStudenti.get_all(self)
    def modifica_student(self,student):
        self.read_all_from_file()
        RepoStudenti.modifica_student(self,student)
        self.write_all_to_file()
    def cauta_student_dupa_id(self,id_student):
        self.read_all_from_file()
        return RepoStudenti.cauta_student_dupa_id(self,id_student)
    def __len__(self):
        self.read_all_from_file()
        return RepoStudenti.__len__(self)
    def clear(self):
        with open(self.__cale_catre_fisier,"w") as f:
            pass





