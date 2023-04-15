from domeniu.problema import Problema
from testare.teste import  Teste
from validare.validator_student import ValidatorStudent
from validare.validator_problema import ValidatorProblema
from validare.validator_nota import ValidatorNota
from infrastructura.repo_note import RepoNote
from infrastructura.repo_probleme import RepoProbleme
from infrastructura.repo_studenti import RepoStudenti
from business.service_note import ServiceNote
from business.service_probleme import ServiceProbleme
from business.service_studenti import ServiceStudenti
from prezentare.consola import UI
from domeniu.student import Student
from domeniu.nota import Nota
from erori.repo_error import RepoError
from erori.validation_error import ValidError
from infrastructura.file_repo_studenti import FileRepoStudenti
from infrastructura.file_repo_probleme import FileRepoProbleme
from infrastructura.file_repo_note import FileRepoNote


validator_student=ValidatorStudent()
validator_problema=ValidatorProblema()
validator_nota=ValidatorNota()
repo_studenti=RepoStudenti()
repo_note=RepoNote()
repo_probleme=RepoProbleme()
service_note=ServiceNote(validator_nota,repo_note,repo_studenti,repo_probleme)
service_probleme=ServiceProbleme(validator_problema,repo_probleme)
service_studenti=ServiceStudenti(validator_student,repo_studenti)

teste=Teste(service_studenti,service_probleme,service_note,Student,validator_student,repo_studenti,repo_note,Nota,RepoError,ValidError,Problema,validator_problema,repo_probleme,validator_nota)
teste.run()
validator_student=ValidatorStudent()
validator_problema=ValidatorProblema()
validator_nota=ValidatorNota()
repo_studenti=FileRepoStudenti("studenti.txt")
repo_note=FileRepoNote("note.txt")
repo_probleme=FileRepoProbleme("probleme.txt")
service_note=ServiceNote(validator_nota,repo_note,repo_studenti,repo_probleme)
service_probleme=ServiceProbleme(validator_problema,repo_probleme)
service_studenti=ServiceStudenti(validator_student,repo_studenti)
consola=UI(service_studenti,service_probleme,service_note)
consola.run()