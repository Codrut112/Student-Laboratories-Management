from erori.repo_error import RepoError
from erori.validation_error import ValidError
from prezentare.comenzi import comenzi
import random


class UI():
    def __init__(self,service_studenti,service_probleme,service_note):
        self.__service_studenti=service_studenti
        self.__service_probleme=service_probleme
        self.__service_note=service_note
        self.__comenzi={
            "adauga_student":self.__ui_adauga_student,
            "print_studenti":self.__ui_print_studenti,
            "sterge_student":self.__ui_sterge_student_si_note,
            "restanti":self.__ui_restanti,
            "modifica_student":self.__ui_modifica_student,
            "cauta_student_dupa_id":self.__ui_cauta_student_dupa_id,
            "adauga_nota":self.__ui_adauga_nota,
            "adauga_problema":self.__ui_adauga_problema,
            "print_probleme":self.__ui_print_probleme,
            "cauta_problema":self.__ui_cauta_problema_dupa_id,
            "sterge_problema":self.__ui_sterge_problema_dupa_id,
            "modifica_problema":self.__ui_modifica_problema_dupa_id,
            "adauga_student_random":self.__ui_adauga_student_random,
            "adauga_problema_random":self.__ui_adauga_problema_random,
            "print_note_student":self.__ui_print_note_student,
            "atribuie_laborator_student":self.__ui_atribuire_laborator,
            "note_problema_alfabetic":self.__ui_note_problema_alfabetic,
            "note_problema_crescator": self.__ui_note_problema_crescator,
            "premianti":self.__ui_premianti,
            "medie_student":self.__ui_medie_student









        }

    def __ui_note_problema_crescator(self):
        '''
        afiseaza studenti notele atribuite unei probleme in ordinea crescatoare a notelor
        :return:-
        '''
        if len(self.__params) != 1:
            print("numar parametri invalid!")
            return
        id_problema = int(self.__params[0])
        note = self.__service_note.get_note_problema(id_problema, 2)
        for nota in note:
            print(nota)
    def __ui_note_problema_alfabetic(self):
        '''
        afiseaza studenti notele atribuite unei probleme in ordinea alfabetica a numelor
        :return: -
        '''
        if len(self.__params)!=1:
            print("numar parametri invalid!")
            return
        id_problema=int(self.__params[0])
        note=self.__service_note.get_note_problema(id_problema,1)
        for nota in note:
            print(nota)

    def __ui_modifica_problema_dupa_id(self):
        '''
               modifica o problema
               :return: -
               '''
        if len(self.__params) != 7:
            print("numar parametri invalid")
            return
        id_problema = int(self.__params[0])
        laborator = int(self.__params[1])
        numar_problema = int(self.__params[2])
        descriere = self.__params[3]
        zi = int(self.__params[4])
        luna = int(self.__params[5])
        an = int(self.__params[6])
        data = [zi, luna, an]
        self.__service_probleme.modifica_problema(id_problema,laborator,numar_problema,descriere,data)
        print(f"problema cu idul {id_problema} a fost modificata cu succes")

    def __ui_sterge_problema_dupa_id(self):
        '''
        sterge o problema
        :return: -
        '''
        if len(self.__params)!=1:
            print("numar parametri invalid")
            return
        id_problema = int(self.__params[0])

        indice=self.__service_note.sterge_problema_si_notele_ei(id_problema,0)
        print(f"problema cu idul {id_problema} a fost stearsa cu succes")
        print(f"s-au  executat {indice} instructiuni")

    def __ui_cauta_problema_dupa_id(self):
        '''
        afiseaza o problema dupa id
        :return: -
        '''
        if len(self.__params)!=1:
            print("numar parametri invalid")
            return
        id_problema=int(self.__params[0])
        print(self.__service_probleme.cauta_problema_dupa_id(id_problema))
    def __ui_adauga_problema(self):
        '''
        adauga o problema
        :return: -
        '''
        if len(self.__params)!=7:
            print("numar parametri invalid")
            return
        id_problema=int(self.__params[0])
        laborator=int(self.__params[1])
        numar_problema=int(self.__params[2])
        descriere=self.__params[3]
        zi=int(self.__params[4])
        luna=int(self.__params[5])
        an=int(self.__params[6])
        data=[zi,luna,an]
        self.__service_probleme.adauga_problema(id_problema,laborator,numar_problema,descriere,data)
        print("problema adaugata cu succes!")
    def __ui_print_probleme(self):
        if(len(self.__params)!=0):
            print("numar parametri invalid!")
            return
        probleme = self.__service_probleme.get_all_probleme()
        if len(probleme) == 0:
            print("nu exista probleme in aplicatie!")
            return
        for problema in probleme:
            print(problema)




    def __ui_adauga_nota(self):
        """
        atribuie o nota unui elev
        :return:
        """
        if(len(self.__params)!=4):
            print("numar parametri invalid")
            return
        id_nota=int(self.__params[0])
        id_student=int(self.__params[1])
        id_problema=int(self.__params[2])
        nota=float(self.__params[3])

        self.__service_note.adauga_nota(id_nota,id_student,id_problema,nota)
        print("nota a fost atribuita cu succes")
    def __ui_atribuire_laborator(self):
        '''
        atribuie o problema de laborator unui student
        :return: -
        '''
        if (len(self.__params) != 3):
            print("numar parametri invalid")
            return
        id_nota = int(self.__params[0])
        id_student = int(self.__params[1])
        id_problema = int(self.__params[2])

        self.__service_note.adauga_nota(id_nota, id_student, id_problema, "lab_asignat")
        print("problema atribuita cu succes")

    def __ui_print_note_student(self):
        """
        afiseaza notele unui student
        :return:
        """
        if (len(self.__params)!=1):
            print("numar paramteri invalid")
            return
        id=int(self.__params[0])
        note=self.__service_note.get_note_student(id)
        for nota in note :
            print (nota)








    def __ui_cauta_student_dupa_id(self):
        """
        afiseaza studentul cu un anume id
        :return:
        """
        if len(self.__params)!=1:
            print("numar parametri invalid")
            return
        id_student = int(self.__params[0])
        print(self.__service_studenti.cauta_student_dupa_id(id_student))

    def __ui_modifica_student(self):
        '''
        modifica datele unui student
        :return: -
        '''
        if len(self.__params)!=3:
            print("numar parametri invalid")
            return
        id_student = int(self.__params[0])
        nume = self.__params[1]
        grup = int(self.__params[2])
        self.__service_studenti.modifica_student(id_student,nume,grup)
        print(f"studentul cu idul {id_student} a fost modificat cu succes!")

    def __ui_restanti(self):
        '''
        afiseaza toti studentii restanti la o materie
        :return: -
        '''
        if len(self.__params)!=0:
            print("numar parametri invalid!")
            return
        restanti=self.__service_note.get_restanti()
        for restant in restanti:
            print(restant)
        if len(restanti)==0:
            print("nici un student nu este restant")
    def __ui_premianti(self):
        """
        afiseaza studentii cu media 10
        :return:
        """
        if len(self.__params) != 0:
            print("numar parametri invalid!")
            return
        premianti = self.__service_note.get_premianti()
        for premiant in premianti:
            print(premiant)
        if len(premianti) == 0:
            print("nici un student nu este premiant")


    def __ui_print_studenti(self):
        """
        afiseaza toti studentii
        :return:
        """

        if len(self.__params)!=0:
            print("numar parametri invalid!")
            return
        studenti=self.__service_studenti.get_all_studenti()
        if len(studenti)==0:
            print("nu exista studenti in aplicatie!")
            return
        for student in studenti:
            print(student)
    def __ui_adauga_student(self):
        '''
        adauga un student in aplicatie
        :return: -
        '''
        if len(self.__params)!=3:
            print("numar parametri invalid!")
            return
        id_student=int(self.__params[0])
        nume=self.__params[1]
        grup=int(self.__params[2])
        self.__service_studenti.adauga_student(id_student,nume,grup)
        print("student adaugat cu succes!")
    def __ui_adauga_student_random(self):
        if(len(self.__params)!=1):
            print("numar parametri invalid!")
            return
        numar=int(self.__params[0])
        for i in range(numar):
            id=self.__service_studenti.create_random_id()
            nume=self.__service_studenti.generate_nume(random.randint(5, 15))
            grup=self.__service_studenti.create_random_id()
            self.__params=[id,nume,grup]
            self.__ui_adauga_student()
    def __ui_adauga_problema_random(self):
        if(len(self.__params)!=1):
            print("numar parametri invalid!")
            return
        numar = int(self.__params[0])
        for i in range(numar):
            id=self.__service_studenti.create_random_id()
            laborator= self.__service_studenti.create_random_id()
            numar_problema = self.__service_studenti.create_random_id()
            descriere=self.__service_studenti.generate_nume(random.randint(10,20))
            self.__params=[id, laborator, numar_problema, descriere, random.randint(1,28),random.randint(1,12),random.randint(0,20000000)]
            self.__ui_adauga_problema()
    def __ui_sterge_student_si_note(self):
        '''
        sterge studentul si notele atribuite studentului din aplicatie
        :return: -
        '''
        if len(self.__params)!=1:
            print("numar parametri invalid!")
            return
        id_student=int(self.__params[0])
        self.__service_note.sterge_student_si_notele_lui(id_student,0)
        print(f"studentul cu idul {id_student} si notele lui au fost sterse cu succes")
    def __ui_medie_student(self):
        if(len(self.__params)!=1):
            print("numar parametri invalid")
            return
        litera=self.__params[0]
        media=self.__service_note.get_medie_studenti(litera)
        if type(media)==str:
            print(f"nu sunt studenti a caror nume sa inceapa cu litera {litera}")
            return
        print(f"media studentilor a caror nume incepre cu litera {litera} este {media} ")

    def run(self):
        while True:
            comanda=input(">>>")
            comanda=comanda.strip()
            if comanda=="":
                continue
            if comanda=="exit":
                return
            if comanda=="help":
                comenzi()
                continue
            parti=comanda.split()
            nume_comanda=parti[0]
            self.__params=parti[1:]
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda]()
                except ValueError:
                    print("eroare UI:tip numeric invalid!")
                except ValidError as ve:
                    print(f"Valid Error:{ve}")
                except RepoError as re:
                    print(f"Repo Error:{re}")
            else:
                print("comanda invalida")
