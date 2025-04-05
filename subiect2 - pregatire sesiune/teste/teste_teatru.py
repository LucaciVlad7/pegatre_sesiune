from service.service_teatru import ServiceTeatru
from repo.repo_teatru import RepoTeatru
from validator.validator_teatru import ValidatorTeatru
from domeniu.domeniu_teatru import Teatru

class TesteTeatru:
    def __init__(self):
        self.__repo=RepoTeatru("teatru.txt")
        self.__validator=ValidatorTeatru()
        self.__service=ServiceTeatru(self.__repo,self.__validator)

    def ruleaza_toate_testele(self):
        self.teste_repo()
        self.teste_service()

    def teste_repo(self):
        self.__repo.adaugare("Titlu","Regizor","Gen",1200)
        lista=self.__repo.export_lista()
        assert len(lista)==11

        print("Repo merge")

    def teste_service(self):
        self.__service.creare_piese_teatru(3)
        lista=self.__service.export_lista()
        assert len(lista)==14

        self.__service.export_lista_in_fisier("fisier_sortat.txt")


        print("Service merge")