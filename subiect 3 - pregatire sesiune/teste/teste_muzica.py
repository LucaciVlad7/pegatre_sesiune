from validator.validator_service import ValidatorMuzica
from service.service_muzica import ServiceMuzica
from repo.repo_muzica import RepoMuzica

class TesteMuzica:
    def __init__(self):
        self.__repo_muzica=RepoMuzica("muzica.txt")
        self.__service_muzica=ServiceMuzica(self.__repo_muzica,ValidatorMuzica())

    def ruleaza_toate_testele(self):
        self.teste_repo()
        self.teste_service()

    def teste_repo(self):
        lista=self.__repo_muzica.export_lista()
        assert len(lista)==4
        self.__repo_muzica.modifica_gen_si_durata("on me","lil baby","Pop",120)
        lista = self.__repo_muzica.export_lista()
        assert lista[0].durata == 120

        print("Repo merge")


    def teste_service(self):
        lista=self.__service_muzica.service_export_lista_muzica()
        assert len(lista)==4

        print("SERVICE merge")