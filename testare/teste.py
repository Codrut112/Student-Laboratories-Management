from domeniu.problema import Problema
from domeniu.student import Student
from infrastructura.file_repo_studenti import FileRepoStudenti
from infrastructura.file_repo_probleme import FileRepoProbleme
from infrastructura.file_repo_note import FileRepoNote
import unittest
class Teste():
    def __init__(self,service_student,service_probleme,service_note,student,validator_student,repo_studenti,repo_note,nota,repo_error,valid_error,problema,validator_problema,repo_probleme,validator_nota):
        self.__service_studenti=service_student
        self.__service_probleme=service_probleme
        self.__service_note=service_note
        self.__student=student
        self.__validator_student=validator_student
        self.__repo_studenti=repo_studenti
        self.__repo_note=repo_note
        self.__nota=nota
        self.__repo_error=repo_error
        self.__valid_error=valid_error
        self.__problema=problema
        self.validator_problema=validator_problema
        self.__repo_probleme=repo_probleme
        self.__validator_nota=validator_nota
        self.__file_repo_studenti=FileRepoStudenti
        self.__file_repo_probleme=FileRepoProbleme
        self.__file_repo_note=FileRepoNote
    def teste_file_repo_note(self):
        self.clear_file("testare/test_file_repo_note.txt")
        repo=self.__file_repo_note("testare/test_file_repo_note.txt")

        assert repo.__len__()==0
        st=self.__student(1,"andrei",22)
        pb=self.__problema(1, 1, 1, "scadere", [1, 2, 3])
        nota = self.__nota(99, 1,1, 10)
        repo.adauga_nota(nota)

        assert repo.cauta_nota_dupa_id(99)==nota
        nota=self.__nota(99,1,1,9)
        repo.modifica_nota(nota)
        nota=repo.cauta_nota_dupa_id(99)
        assert nota.get_nota()==9
        nota_other=self.__nota(98,1,1,8)
        repo.adauga_nota(nota_other)
        assert repo.get_all()==[nota,nota_other]
        repo.sterge_nota(99)
        assert repo.__len__()==1



    def teste_file_repo_probleme(self):
        self.clear_file("testare/test_file_repo_probleme.txt")
        repo=self.__file_repo_probleme("testare/test_file_repo_probleme.txt")
        assert repo.__len__()==0
        problema=Problema(1,1,1,"adunare",[1,2,3])
        repo.adauga_problema(problema)

        assert repo.cauta_problema_dupa_id(1)==problema
        problema = Problema(1, 1, 1, "scadere", [1, 2, 3])
        repo.modifica_problema(problema)
        problema=repo.cauta_problema_dupa_id(1)
        assert problema.get_descriere()=="scadere"
        problema_other=Problema(2,1,1,"adunare",[1,2,3])
        repo.adauga_problema(problema_other)
        assert repo.get_all()==[problema,problema_other]
        repo.sterge_problema_dupa_id(1)
        assert repo.__len__()==1




    def teste_file_repo_studenti(self):
        self.clear_file("testare/test_file_repo_studenti.txt")
        repo=self.__file_repo_studenti("testare/test_file_repo_studenti.txt")
        assert repo.__len__()==0
        student=self.__student(1,"andrei",22)
        repo.adauga_student(student)
        assert repo.cauta_student_dupa_id(1)==student
        student = self.__student(1, "dan", 22)
        repo.modifica_student(student)
        student=repo.cauta_student_dupa_id(1)
        assert student.get_nume()=="dan"
        student_other = self.__student(2, "andrei", 22)
        repo.adauga_student(student_other)
        assert repo.get_all()==[student,student_other]
        repo.sterge_student_dupa_id(1)
        assert repo.__len__()==1

    def clear_file(self,cale):
        with open(cale,"w") as f:
            pass

    def teste_problema(self):
        pb=self.__problema(124234,3242,3423,"fa_ceva",[21,10,2003])

        assert pb.get_id_problema()==124234
        assert pb.get_laborator()==3242
        assert pb.get_numar_problema()==3423
        assert pb.get_descriere()=="fa_ceva"
        assert pb.get_deadline()==[21,10,2003]
        pb.set_laborator(23423)
        pb.set_numar_problema(3242342)
        pb.set_descriere("nu face nimic")
        pb.set_deadline([2,2,2])
        assert pb.get_laborator() == 23423
        assert pb.get_numar_problema() == 3242342
        assert pb.get_descriere() == "nu face nimic"
        assert pb.get_deadline() == [2, 2, 2]




    def teste_student(self):
        st = self.__student(123,"Ion",2)

        assert st.get_id_student() == 123
        assert st.get_nume() == "Ion"
        assert st.get_grup() == 2
        st.set_nume("alex")
        assert st.get_nume() == "alex"
        st.set_grup(3)
        assert st.get_grup() == 3
        assert st.stare() == False
        st.sterge()
        assert st.stare() == True
    def teste_problema_validare(self):
        '''
        testeaza validarea unei note
        :return: -
        '''
        pb = self.__problema(124234, 3242, 3423, "fa_ceva", [21, 10, 2003])
        validator=self.validator_problema
        validator.valideaza(pb)
        pb_invalid=self.__problema(-124234, -3242, -3423, "", [-21, 10, 2003])
        try:
            validator.valideaza(pb_invalid)
            assert False
        except self.__valid_error:
            assert True
    def teste_student_validare(self):
        """
        testeaza validarea unui student

        """
        st = self.__student(1111,"Ion",2)
        validator = self.__validator_student
        validator.valideaza(st)
        st_invalid = self.__student(-2, "", -2)
        try:
            validator.valideaza(st_invalid)
            assert False
        except self.__valid_error:
            assert True
    def teste_repo_problema(self):
        dict=self.__repo_probleme
        pb = self.__problema(124234, 3242, 3423, "fa_ceva", [21, 10, 2003])
        assert dict.__len__()==0
        dict.adauga_problema(pb)
        try:
            dict.adauga_problema(pb)
            assert False
        except self.__repo_error:
            assert True
        assert dict.__len__()==1
        assert dict.cauta_problema_dupa_id(124234)==pb
        pb = self.__problema(124234, 322, 323, "nu_face", [1, 1, 203])
        dict.modifica_problema(pb)
        assert dict.cauta_problema_dupa_id(124234)==pb
        lista_problema=[]
        lista_problema.append(pb)
        assert lista_problema==dict.get_all()
        dict.sterge_problema_dupa_id(124234)
        assert dict.__len__()==0

    def teste_repo_student(self):
        dict = self.__repo_studenti
        st = self.__student(1111,"Ion",2)
        assert dict.__len__() == 0
        dict.adauga_student(st)
        try:
            dict.adauga_student(st)
            assert False
        except self.__repo_error:
            assert True
        assert dict.__len__() == 1
        dict.sterge_student_dupa_id(1111)
        assert dict.__len__() == 0
        st =self.__student(1268, "raul", 2)
        dict.adauga_student(st)
        assert dict.cauta_student_dupa_id(1268) == st
        lista_student = []
        lista_student.append(st)
        assert dict.get_all() == lista_student
        st_2 = self.__student(1268, "paul", 3)
        dict.modifica_student(st_2)
        st_2 = dict.cauta_student_dupa_id(1268)
        assert st_2.get_nume() != st.get_nume()
        assert dict.__len__() == 1
        dict.sterge_student_dupa_id(1268)

    def teste_nota(self):
        """
        testeaza crearea unei note

        """
        st = self.__student(99, "Ion", 2)
        nota = self.__nota(99, st, 2, 10)
        assert nota.get_sters() == False
        assert nota.get_id_nota() == 99
        assert (nota.get_nota()-10)<0.000001
        assert nota.get_id_student() == st
        nota.sterge()
        assert nota.get_sters() == True


    def teste_repo_nota(self):
        st = self.__student(9999, "Ion", 2)
        nota = self.__nota(9999, st, 2, 10)
        dict = self.__repo_note
        lista_note = []
        lista_note.append(nota)
        assert dict.__len__() == 0
        dict.adauga_nota(nota)
        assert dict.__len__() == 1
        assert dict.get_all() == lista_note
        assert dict.cauta_nota_dupa_id(9999) == nota
        nota1 = self.__nota(9999, st, 2, 5)
        dict.modifica_nota(nota1)
        nota1 = dict.cauta_nota_dupa_id(9999)
        assert nota1.get_nota() != nota.get_nota()
        dict.sterge_nota(9999)
        assert dict.__len__() == 0

    def teste_service_studenti(self):
        studenti = self.__service_studenti
        assert studenti.__len__() == 0
        st = self.__student(589, "Ion", 2)
        lista_studenti = []
        lista_studenti.append(st)
        studenti.adauga_student(589, "Ion", 2)
        assert studenti.__len__() == 1
        assert studenti.get_all_studenti() == lista_studenti
        assert studenti.cauta_student_dupa_id(589) == st
        studenti.modifica_student(589, "Raul", 2)
        st_2 = studenti.cauta_student_dupa_id(589)
        assert st_2.get_nume != st.get_nume()
        self.__service_note.sterge_student_si_notele_lui(589,0)
    def teste_service_probleme(self):
        probleme=self.__service_probleme
        assert probleme.__len__()==0
        probleme.adauga_problema(129, 3242, 3423, "fa_ceva", [21, 10, 2003])
        pb=self.__problema(129, 3242, 3423, "fa_ceva", [21, 10, 2003])
        assert probleme.__len__() == 1
        lista_problema=self.__repo_probleme
        assert probleme.cauta_problema_dupa_id(129)==pb
        assert probleme.get_all_probleme() == lista_problema.get_all()
        probleme.modifica_problema(129, 32, 33, "fa_nimic", [2, 1, 2003])
        pb_2=probleme.cauta_problema_dupa_id(129)
        assert pb_2.get_laborator!=pb.get_laborator
        self.__repo_probleme.sterge_problema_dupa_id(129)



    def teste_service_note(self):

        repo_note = self.__repo_note
        repo_studenti = self.__repo_studenti
        repo_probleme=self.__repo_probleme

        note = self.__service_note
        st = self.__student(5889, "andrei", 2)
        pb=self.__problema(129, 3242, 3423, "fa_ceva", [21, 10, 2003])

        repo_studenti.adauga_student(st)
        repo_probleme.adauga_problema(pb)
        note.adauga_nota(5889,5889,129,5.5)


        assert len(note.get_note_student(5889))==1
        assert note.__len__()==1
        note.sterge_student_si_notele_lui(5889,0)
        note.sterge_problema_si_notele_ei(129,0)
        assert repo_studenti.__len__() == 0
        assert repo_probleme.__len__()==0
        st = self.__student(2000, "andrei", 2)
        nota = self.__nota(2000, 2000, 129, 4)
        repo_studenti.adauga_student(st)
        repo_note.adauga_nota(nota)
        assert self.__service_note.get_note_student(2000)==[nota]



        st =self.__student(366, "razvan", 2)
        nota1 = self.__nota(366, 366, 129, 3)

        repo_studenti.adauga_student(st)

        repo_note.adauga_nota(nota1)
        st =self.__student(367, "daniel", 6)
        nota2 = self.__nota(367, 367, 129, 10)

        repo_studenti.adauga_student(st)
        repo_note.adauga_nota(nota2)
        repo_probleme.adauga_problema(pb)
        lista_note=note.get_note_problema(pb.get_id_problema(),2)

        assert lista_note[0].get_nume()=="razvan"
        assert lista_note[1].get_nume() == "andrei"
        assert lista_note[2].get_nume() == "daniel"
        lista_note = note.get_note_problema(pb.get_id_problema(), 1)

        assert lista_note[0].get_nume() == "andrei"
        assert lista_note[1].get_nume() == "daniel"
        assert lista_note[2].get_nume() == "razvan"
        assert note.get_premianti()==[['daniel',10.0]]
        assert note.get_restanti() == [['andrei', 4.0], ['razvan', 3.0]]
        self.__service_note.sterge_student_si_notele_lui(366,0)
        self.__service_note.sterge_student_si_notele_lui(2000,0)
        self.__service_note.sterge_student_si_notele_lui(367,0)
        note.sterge_problema_si_notele_ei(129,0)
    def teste_nota_validare(self):
        validator=self.__validator_nota
        st = self.__student(5889, "andrei", 2)
        pb = self.__problema(129, 3242, 3423, "fa_ceva", [21, 10, 2003])
        nota=self.__nota(1,5889,129,2)
        validator.valideaza(nota)
        note=self.__service_note
        pb_invalid = self.__problema(-124234, -3242, -3423, "", [-21, 10, 2003])
        st_invalid = self.__student(589, "andrei", 2)
        try:
            note.adauga_nota(5890, -33, pb_invalid, 6)
            assert False
        except self.__repo_error:
            assert True


    def run(self):
        self.teste_student()
        self.teste_problema()
        self.teste_nota()
        print("teste student,nota,problema trecute cu succes!")
        self.teste_student_validare()
        self.teste_problema_validare()
        self.teste_nota_validare()
        print("teste validator student,problema si nota trecute cu succes!")
        self.teste_repo_student()
        self.teste_repo_nota()
        self.teste_repo_problema()
        print("teste repo studenti,note,probleme trecute cu succes!")
        self.teste_service_probleme()
        self.teste_service_studenti()
        self.teste_service_note()
        print("teste service studenti si note trecute cu succes!")
        self.teste_file_repo_studenti()
        self.teste_file_repo_probleme()
        self.teste_file_repo_note()
        print("teste fisiere trecute cu succes!")


















