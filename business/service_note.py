from domeniu.nota import Nota
from domeniu.note_problema_crescator import Note_problema_cresc
from domeniu.Note_problema_alfabetic import note_problema_alf





class ServiceNote:
    '''
    aceasta clasa gestioneaza notele
    '''


    def __init__(self,validator_nota,repo_note,repo_studenti,repo_probleme):

      self.__validator_nota=validator_nota
      self.__repo_note=repo_note
      self.__repo_studenti=repo_studenti
      self.__repo_probleme=repo_probleme
    def get_all(self):
        '''
        returneaza toate probleme
        :return: list
        '''
        return self.__repo_note.get_all()
    def adauga_nota(self,id_nota,id_student,id_problema,valoare):
        '''
        atribui o nota unui student la o anumita problema
        :param id_nota: int
        :param id_student: int
        :param id_problema: int
        :param valoare: float
        :return:
        '''
        nota=Nota(id_nota,id_student,id_problema,valoare)
        self.__repo_studenti.cauta_student_dupa_id(id_student)
        self.__repo_probleme.cauta_problema_dupa_id(id_problema)
        self.__validator_nota.valideaza(nota)
        self.__repo_note.adauga_nota(nota)
    def sterge_nota(self,id_nota):
        """
        sterge o nota atribuita unui student
        :return:
        """
        self.__repo_note.sterge_nota(id_nota)

    def sterge_problema_si_notele_ei(self, id_problema, indice):
        '''
        sterge o problema si notele la acea problema
        :param id_problema: int
        :param indice:int
        :return: int
        '''

        note = self.__repo_note.get_all()
        indice=indice+len(note)

        note_problema = []

        for x in note:
            if x.get_id_problema() == id_problema:
                note_problema.append(x)
                indice=indice+1
        for nota_problema in note_problema:
            self.__repo_note.sterge_nota(nota_problema.get_id_nota())
            indice=indice+1
        self.__repo_probleme.sterge_problema_dupa_id(id_problema)
        indice=indice+1
        return indice

    def sterge_problema_si_notele_ei2(self,id_problema,indice):
        """
        sterge o problema
        :param id_problema: int
        :param indice: int
        :return: -
        """
        note = self.__repo_note.get_all()

        if (len(note) == 0):
            self.__repo_probleme.sterge_problema_dupa_id(id_problema)
            return

        if note[indice].get_id_problema() == id_problema:
            self.__repo_note.sterge_nota(note[indice].get_id_nota())
            self.sterge_problema_si_notele_ei(id_problema, indice)
        elif indice == len(note) - 1:
            self.__repo_probleme.sterge_problema_dupa_id(id_problema)
            return
        else:
            self.sterge_problema_si_notele_ei(id_problema, indice + 1)

    def sterge_student_si_notele_lui(self, id_student,indice):
        '''
        sterge un student daca exista
        :param id_student: int
        :param indice:int
        :return: -
        '''

        note = self.__repo_note.get_all()


        if(len(note)==0):
            self.__repo_studenti.sterge_student_dupa_id(id_student)
            return

        if note[indice].get_id_student()==id_student:
            self.__repo_note.sterge_nota(note[indice].get_id_nota())
            self.sterge_student_si_notele_lui(id_student, indice )
        elif indice==len(note)-1:
            self.__repo_studenti.sterge_student_dupa_id(id_student)
            return
        else :
            self.sterge_student_si_notele_lui(id_student,indice+1)


    def get_restanti(self):
        """
        returneaza studenti care au media la laborator mai mica decat 5
        :return:list
        """
        info_studenti={}
        note=self.__repo_note.get_all()
        for nota in note:
            if nota.get_nota()!="lab_asignat":
                id_student_nota = nota.get_id_student()
                valoare_nota = nota.get_nota()
                if id_student_nota not in info_studenti:
                    info_studenti[id_student_nota] = []
                info_studenti[id_student_nota].append(valoare_nota)
        restanti = []


        for id_student in info_studenti:
            student=self.__repo_studenti.cauta_student_dupa_id(id_student)
            nume_student=student.get_nume()
            medie_student=sum(info_studenti[id_student])/len(info_studenti[id_student])
            if medie_student<5:
                restant=[nume_student,medie_student]
                restanti.append(restant)
        return restanti

    def get_premianti(self):
        '''
        returneaza studenti care au media 10
        :return:
        '''
        info_studenti = {}
        note = self.__repo_note.get_all()
        for nota in note:
            if nota.get_nota() != "lab_asignat":
                id_student_nota = nota.get_id_student()
                valoare_nota = nota.get_nota()
                if id_student_nota not in info_studenti:
                    info_studenti[id_student_nota] = []
                info_studenti[id_student_nota].append(valoare_nota)
        premianti = []

        for id_student in info_studenti:
            student = self.__repo_studenti.cauta_student_dupa_id(id_student)
            nume_student = student.get_nume()
            medie_student = sum(info_studenti[id_student]) / len(info_studenti[id_student])
            if medie_student == 10:
                premiant = [nume_student, medie_student]
                premianti.append(premiant)
        return premianti
    def __len__(self):
        """
        returneaza numarul de note din aplicatie
        :return: int
        """
        return self.__repo_note.__len__()
    def get_note_student(self,id_student):
        """
        returneaz o lista cu toate notele unui student
        :param id_student: student
        :return:list
        """
        student=self.__repo_studenti.cauta_student_dupa_id(id_student)
        lista_note_student=[]
        lista_note=self.__repo_note.get_all()

        for nota in lista_note:

            if nota.get_id_student()==student.get_id_student():
                lista_note_student.append(nota)
        return lista_note_student





    def get_note_problema(self,id_problema,caz):
        '''
        returneza notele la o problema in ordine alfabetica pentru caz=1 si in oridnea crescatoare a notelor pentru caz=2
        :param id_problema:int
        :param caz:int
        :return:list
        '''
        if (caz==2):
            note = self.__repo_note.get_all()
            note_problema = []

            for nota in note:
                if nota.get_id_problema() == id_problema:
                    student=self.__repo_studenti.cauta_student_dupa_id(nota.get_id_student())
                    nume=student.get_nume()
                    NOTA=nota.get_nota()
                    if(NOTA!="lab_asignat"):
                        x=Note_problema_cresc(nume,NOTA)
                        note_problema.append(x)
            'self.quicksort(note_problema,0,len(note_problema)-1, lambda x,y: x.get_nota()>y.get_nota() or (abs(x.get_nota()-y.get_nota())<0.00001 and x.get_nume()>y.get_nume()))'
            note_problema.sort(key=lambda x:(x.get_nota(),reversed(x.get_nume())))
            return note_problema
        if (caz == 1):
            note = self.__repo_note.get_all()
            note_problema = []

            for nota in note:
                if nota.get_id_problema() == id_problema:
                    student = self.__repo_studenti.cauta_student_dupa_id(nota.get_id_student())
                    nume = student.get_nume()
                    NOTA = nota.get_nota()

                    if (NOTA != "lab_asignat"):
                        x = note_problema_alf(nume, NOTA)
                        note_problema.append(x)
            self.quicksort(note_problema,0,len(note_problema)-1,lambda x,y:x.get_nume()>=y.get_nume())
            return note_problema



    def get_medie_studenti(self,litera):
        '''
        return   eaza media studentilor a caror nume incepe cu  litera litera
        daca in aplicatie nu exista studenti a caror nume nu incepe cu litera aleasa returneaza mesajul "nu exista elevi a caror nume sa inceapa cu litera litera"
        raise ValueError pt litera nu apartine de "zxcvbnmasdfghjklqwertyuiop"
        :param litera: string
        :return: float-daca exista studenti a caror nume incepe cu litera litera
                 mesajul: "nu exista studenti a caror nume incepe cu litera litera"
        '''
        if litera not in "zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP":
            raise ValueError("date de intrare invalide")
        info_studenti = {}
        note = self.__repo_note.get_all()
        for nota in note:
            if nota.get_nota() != "lab_asignat":
                id_student_nota = nota.get_id_student()
                valoare_nota = nota.get_nota()
                if id_student_nota not in info_studenti:
                    info_studenti[id_student_nota] = []
                info_studenti[id_student_nota].append(valoare_nota)

        suma_medi=0
        nr_medii=0
        for id_student in info_studenti:
            student = self.__repo_studenti.cauta_student_dupa_id(id_student)
            nume_student = student.get_nume()
            medie_student = sum(info_studenti[id_student]) / len(info_studenti[id_student])
            if nume_student[0] == litera:
                suma_medi+=medie_student
                nr_medii=nr_medii+1
        if nr_medii>0:
            return suma_medi/nr_medii
        return f"nu exista studenti a caror nume incepe cu litera {litera}"

    def partiti(self, array, start, end, compare_func):
        '''
        face parte din quicksort
        :param array: array
        :param start: int
        :param end: int
        :param compare_func: functie de comparare
        :return: int
        '''
        pivot=array[start]
        low=start+1
        high=end
        while True:
            while low<=high and compare_func(array[high],pivot):
                high=high-1
            while low<=high and not compare_func(array[low],pivot):
                low=low+1
            if low<=high:
                array[low],array[high]=array[high],array[low]
            else :
                break
        array[start],array[high]=array[high],array[start]
        return high



    def quicksort(self, array, start, end, compare_func):
        '''
        sorteaza un array
        :param array: array
        :param start: int
        :param end:int
        :param compare_func: functie de comparare
        :return: -
        '''
        if start >= end:
            return
        p = self.partiti(array, start, end, compare_func)
        self.quicksort(array, start, p - 1, compare_func)
        self.quicksort(array, p + 1, end, compare_func)
    def gnome_sort(self,array,compare_funct):
        '''
        gnome_sort
        :param array: array
        :param compare_funct: functie de comparare
        :return: -
        '''
        indice=0
        while indice<len(array):
            if indice==0 or compare_funct(array[indice],array[indice-1]):
                indice=indice+1
            else:
                array[indice],array[indice-1]=array[indice-1],array[indice]
                indice=indice-1



















