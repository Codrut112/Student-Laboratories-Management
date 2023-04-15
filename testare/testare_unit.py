import unittest

from business.service_note import ServiceNote
from business.service_probleme import ServiceProbleme
from domeniu.Note_problema_alfabetic import note_problema_alf
from domeniu.nota import Nota
from domeniu.note_problema_crescator import Note_problema_cresc
from domeniu.problema import Problema
from domeniu.student import Student
from erori.validation_error import ValidError
from infrastructura.file_repo_note import FileRepoNote
from infrastructura.file_repo_probleme import FileRepoProbleme
from infrastructura.repo_note import RepoNote
from infrastructura.repo_probleme import RepoProbleme
from infrastructura.repo_studenti import RepoStudenti
from validare.validator_nota import ValidatorNota
from validare.validator_problema import ValidatorProblema
from validare.validator_student import ValidatorStudent
from business.service_studenti import ServiceStudenti
from infrastructura.file_repo_studenti import FileRepoStudenti

class TesteStudent(unittest.TestCase):




    def setUp(self) -> None:

        self.__id_student = 1
        self.__nume_student = "Razvan"
        self.__grup_student = 222
        self.__student = Student(1, "Razvan", 222)
        self.__nume_nou="Andrei"
        self.__grup_nou=2
        self.__student_acelasi_id = Student(self.__id_student, self.__nume_nou, self.__grup_nou)
        self.__repo = RepoStudenti()
        self.__validator=ValidatorStudent()
        self.__student_invalid=Student(-1,"",-33)
        self.__file_repo=FileRepoStudenti("testare/test_file_repo_studenti.txt")
        self.__service=ServiceStudenti(self.__validator,self.__file_repo)

    def test_create_student(self):
        self.assertEqual(self.__id_student, self.__student.get_id_student())
        self.assertEqual(self.__nume_student, self.__student.get_nume())
        self.assertEqual(self.__grup_student, self.__student.get_grup())
        self.assertEqual(self.__student, self.__student_acelasi_id)
    def teste_set_student(self):
        self.assertNotEqual(self.__nume_nou, self.__student.get_nume())
        self.__student.set_nume(self.__nume_nou)
        self.assertEqual(self.__nume_nou, self.__student.get_nume())
        self.assertNotEqual(self.__grup_nou, self.__student.get_grup())
        self.__student.set_grup(self.__grup_nou)
        self.assertEqual(self.__grup_nou, self.__student.get_grup())
    def teste_repo_studenti(self):
        self.assertEqual(self.__repo.__len__(),0)
        self.__repo.adauga_student(self.__student)
        self.assertEqual(self.__repo.__len__(),1)
        self.assertEqual(self.__repo.cauta_student_dupa_id(1),self.__student)
        self.assertEqual(self.__repo.get_all(),[self.__student])
        self.__repo.modifica_student(self.__student_acelasi_id)
        self.assertEqual(self.__repo.cauta_student_dupa_id(1).get_nume(),self.__student_acelasi_id.get_nume())
        self.__repo.sterge_student_dupa_id(1)
        self.assertEqual(self.__repo.__len__(), 0)
    def teste_validator_student(self):
        self.__validator.valideaza(self.__student)
        try:
            self.__validator.valideaza(self.__student_invalid)
            assert False
        except ValidError as ve:
           assert True
    def teste_file_repo_studenti(self):
        self.__file_repo.clear()
        self.assertEqual(self.__file_repo.__len__(), 0)
        self.__file_repo.adauga_student(self.__student)
        self.assertEqual(self.__file_repo.__len__(), 1)
        self.assertEqual(self.__file_repo.cauta_student_dupa_id(1), self.__student)
        self.assertEqual(self.__file_repo.get_all(), [self.__student])
        self.__file_repo.modifica_student(self.__student_acelasi_id)
        self.assertEqual(self.__file_repo.cauta_student_dupa_id(1).get_nume(), self.__student_acelasi_id.get_nume())
        self.__file_repo.sterge_student_dupa_id(1)
        self.assertEqual(self.__file_repo.__len__(), 0)
    def teste_service_studenti(self):
        self.assertEqual(self.__service.__len__(),0)
        self.__service.adauga_student(1,"Razvan",222)
        self.assertEqual(self.__service.__len__(),1)
        self.assertEqual(self.__service.cauta_student_dupa_id(1),self.__student)
        self.assertEqual(self.__service.get_all_studenti(),[self.__student])
        self.__service.modifica_student(1,"Andrei",222)
        self.assertEqual(self.__service.cauta_student_dupa_id(1).get_nume(),"Andrei")





class TesteProblema(unittest.TestCase):
    def setUp(self) -> None:
        self.__id_problema=1
        self.__laborator=2
        self.__numar_problema=3
        self.__descriere="adunare"
        self.__deadline=[1,2,3]
        self.__laborator_nou=3
        self.__numar_problema_nou=3
        self.__descriere_nou="scadere"
        self.__deadline_nou=[1,2,2023]
        self.__problema=Problema(self.__id_problema,self.__laborator,self.__numar_problema,self.__descriere,self.__deadline)
        self.__problema_acelasi_id=Problema(1,1,1,"scadere",[1,1,1])
        self.__repo=RepoProbleme()
        self.__validator=ValidatorProblema()
        self.__problema_invalida=Problema(0,0,0,"",[0,0,0])
        self.__file_repo=FileRepoProbleme("test_file_repo_probleme.txt")
        self.__service=ServiceProbleme(self.__validator,self.__file_repo)

    def teste_create_problema(self):
        self.assertEqual(self.__id_problema,self.__problema.get_id_problema())
        self.assertEqual(self.__laborator,self.__problema.get_laborator())
        self.assertEqual(self.__numar_problema,self.__problema.get_numar_problema())
        self.assertEqual(self.__descriere,self.__problema.get_descriere())
        self.assertEqual(self.__deadline,self.__problema.get_deadline())
        self.assertEqual(self.__problema,self.__problema_acelasi_id)
    def teste_set_problema(self):
        self.assertNotEqual(self.__laborator_nou, self.__problema.get_laborator())
        self.__problema.set_numar_problema(self.__numar_problema_nou)
        self.assertEqual(self.__numar_problema_nou,self.__problema.get_numar_problema())
        self.assertNotEqual(self.__laborator_nou,self.__problema.get_laborator())
        self.__problema.set_laborator(self.__laborator_nou)
        self.assertEqual(self.__laborator_nou,self.__problema.get_laborator())
        self.assertNotEqual(self.__descriere_nou,self.__problema.get_descriere())
        self.__problema.set_descriere(self.__descriere_nou)
        self.assertEqual(self.__descriere_nou,self.__problema.get_descriere())
        self.assertNotEqual(self.__deadline_nou,self.__problema.get_descriere())
        self.__problema.set_deadline(self.__deadline_nou)
        self.assertEqual(self.__deadline_nou,self.__problema.get_deadline())
    def teste_repo_problema(self):
        self.assertEqual(self.__repo.__len__(), 0)
        self.__repo.adauga_problema(self.__problema)
        self.assertEqual(self.__repo.__len__(), 1)
        self.assertEqual(self.__repo.cauta_problema_dupa_id(1), self.__problema)
        self.assertEqual(self.__repo.get_all(), [self.__problema])
        self.__repo.modifica_problema(self.__problema_acelasi_id)
        self.assertEqual(self.__repo.cauta_problema_dupa_id(1).get_descriere(), self.__problema_acelasi_id.get_descriere())
        self.__repo.sterge_problema_dupa_id(1)
        self.assertEqual(self.__repo.__len__(), 0)
    def teste_validator_problema(self):

            self.__validator.valideaza(self.__problema)
            try:
                self.__validator.valideaza(self.__problema_invalida)
                assert False
            except ValidError as ve:
                assert True
    def teste_file_repo_probleme(self):
        self.__file_repo.clear()
        self.assertEqual(self.__file_repo.__len__(), 0)
        self.__file_repo.adauga_problema(self.__problema)
        self.assertEqual(self.__file_repo.__len__(), 1)
        self.assertEqual(self.__file_repo.cauta_problema_dupa_id(1), self.__problema)
        self.assertEqual(self.__file_repo.get_all(), [self.__problema])
        self.__file_repo.modifica_problema(self.__problema_acelasi_id)
        self.assertEqual(self.__file_repo.cauta_problema_dupa_id(1).get_descriere(), self.__problema_acelasi_id.get_descriere())
        self.__file_repo.sterge_problema_dupa_id(1)
        self.assertEqual(self.__file_repo.__len__(), 0)
    def teste_service_probleme(self):
        self.assertEqual(self.__service.__len__(),0)
        self.__service.adauga_problema(self.__id_problema,self.__laborator,self.__numar_problema,self.__descriere,self.__deadline)
        self.assertEqual(self.__service.__len__(),1)
        self.assertEqual(self.__service.cauta_problema_dupa_id(1),self.__problema)
        self.assertEqual(self.__service.get_all_probleme(),[self.__problema])
        self.__service.modifica_problema(self.__id_problema,self.__laborator,self.__numar_problema,self.__descriere_nou,self.__deadline)
        self.assertEqual(self.__service.cauta_problema_dupa_id(1).get_descriere(),self.__descriere_nou)



class TesteNota(unittest.TestCase):
    def setUp(self) -> None:
        self.__id_nota=1
        self.__id_student=2
        self.__id_problema=3
        self.__valoare_nota=4
        self.__nota=Nota(1,2,3,4)
        self.__nota2=Nota(2,2,1,10)
        self.__nota3=Nota(3,1,1,3)
        self.__validator_nota=ValidatorNota()
        self.__valoare_nota_noua=10
        self.__nota_acelasi_id=Nota(1,10,10,10)
        self.__nota_invalida=Nota(0,0,0,0)
        self.__repo=RepoNote()
        self.__problema = Problema(1, 1, 1, "scadere", [1, 1, 1])
        self.__problema2=Problema(2,2,2,"adunare",[10,12,2022])
        self.__student1=Student(1, "andrei", 22)
        self.__student2 = Student(2, "daniel", 22)
        self.__file_repo_note=FileRepoNote("testare/test_file_repo_note.txt")
        self.__file_repo_studenti=FileRepoStudenti("testare/test_file_repo_studenti.txt")
        self.__file_repo_probleme=FileRepoProbleme("testare/test_file_repo_probleme.txt")
        self.__service=ServiceNote(self.__validator_nota,self.__file_repo_note,self.__file_repo_studenti,self.__file_repo_probleme)
        self.__lista1=[note_problema_alf("andrei",4),note_problema_alf("andrei",3),note_problema_alf("daniel",10)]
        self.__lista2=[Note_problema_cresc("andrei",3),Note_problema_cresc("andrei",4),Note_problema_cresc("daniel",10)]
        self.__lista_3 = [note_problema_alf("daniel", 10), note_problema_alf("andrei", 4), note_problema_alf("andrei", 3)]
    def teste_create_nota(self):
        self.assertEqual(self.__id_nota,self.__nota.get_id_nota())
        self.assertEqual(self.__id_student,self.__nota.get_id_student())
        self.assertEqual(self.__id_problema,self.__nota.get_id_problema())
        self.assertEqual(self.__nota_acelasi_id,self.__nota)
    def teste_repo_nota(self):
        self.assertEqual(self.__repo.__len__(),0)
        self.__repo.adauga_nota(self.__nota)
        self.assertEqual(self.__repo.get_all(),[self.__nota])
        self.assertEqual( self.__repo.cauta_nota_dupa_id(1),self.__nota)
        self.__repo.modifica_nota(self.__nota_acelasi_id)
        self.assertEqual(self.__repo.cauta_nota_dupa_id(1).get_nota(),self.__valoare_nota_noua)
        self.__repo.sterge_nota(1)
        self.assertEqual(self.__repo.__len__(),0)
    def teste_validator_nota(self):
        self.__validator_nota.valideaza(self.__nota)
        try:
            self.__validator_nota.valideaza(self.__nota_invalida)
            assert False
        except ValidError:
            assert True
    def teste_file_repo_note(self):
        self.__file_repo_note.clear()
        self.assertEqual(self.__file_repo_note.__len__(),0)
        self.__file_repo_note.adauga_nota(self.__nota)
        self.assertEqual(self.__file_repo_note.get_all(),[self.__nota])
        self.assertEqual(self.__file_repo_note.cauta_nota_dupa_id(1),self.__nota)
        self.__file_repo_note.modifica_nota(self.__nota_acelasi_id)
        self.assertEqual(self.__file_repo_note.cauta_nota_dupa_id(1).get_nota(),self.__nota_acelasi_id.get_nota())
        self.__file_repo_note.sterge_nota(1)
        self.assertEqual(self.__file_repo_note.__len__(),0)
    def teste_service_note(self):
        self.assertEqual(self.__service.__len__(),0)
        self.__file_repo_studenti.clear()
        self.__file_repo_probleme.clear()
        self.__file_repo_studenti.adauga_student(self.__student1)
        self.__file_repo_studenti.adauga_student(self.__student2)
        self.__file_repo_probleme.adauga_problema(self.__problema)

        self.__service.adauga_nota(1,1,1,4)
        self.__service.adauga_nota(3,1,1,3)
        self.__service.adauga_nota(2,2,1,10)

        'black box texting'
        self.assertEqual(self.__service.get_medie_studenti("a"),3.5)
        self.assertEqual(self.__service.get_medie_studenti("b"),"nu exista studenti a caror nume incepe cu litera b")
        try:
            self.__service.get_medie_studenti("1")
            assert False
        except ValueError:
            assert True

        self.assertEqual(self.__service.get_note_problema(1,1),self.__lista1)
        self.assertEqual(self.__service.get_note_problema(1,2),self.__lista2)
        self.__service.gnome_sort(self.__lista_3,lambda x,y:x.get_nume()>=y.get_nume())
        self.assertEqual(self.__lista_3,self.__lista1)
        self.assertEqual(self.__service.get_note_student(1),[self.__nota,self.__nota3])
        self.assertEqual(self.__service.get_restanti(),[["andrei",3.5]])
        self.assertEqual(self.__service.get_medie_studenti("a"),3.5)
        self.assertEqual(self.__service.get_premianti(),[["daniel",10]])
        self.assertEqual(self.__service.__len__(),3)
        self.__service.sterge_nota(1)
        self.assertEqual(self.__service.__len__(),2)
        self.__service.sterge_problema_si_notele_ei(1,0)
        self.assertEqual(self.__file_repo_probleme.__len__(),0)
        self.__service.sterge_student_si_notele_lui(1,0)
        self.assertEqual(self.__file_repo_studenti.__len__(),1)










