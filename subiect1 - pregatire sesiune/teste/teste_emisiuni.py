from multiprocessing.context import assert_spawning

from repo.repo_emisiuni import RepoEmisiuni
from service.service_emisiuni import ServiceEmisiuni

class Teste:
    def __init__(self):
        self.__repo_emisiuni=RepoEmisiuni("emisiuni.txt")
        self.__service_emisiuni=ServiceEmisiuni(RepoEmisiuni("emisiuni.txt"))

    def ruleaza_toate_testele(self):
        self.teste_repo()
        self.teste_service()

    def teste_repo(self):
        lista_emisiuni=self.__repo_emisiuni.returneaza_lista()
        assert len(lista_emisiuni)==3
        self.__repo_emisiuni.stergere_emisiune("Jurnal","Stiri")
        lista_emisiuni = self.__repo_emisiuni.returneaza_lista()
        assert len(lista_emisiuni) == 2
        self.__repo_emisiuni.actualizare_durata_descriere("Reportaj","Informare",2,"Viata la oras")
        lista_emisiuni = self.__repo_emisiuni.returneaza_lista()
        for emisiune in lista_emisiuni:
            if emisiune.nume=="Reportaj" and emisiune.tip == "Informare":
                assert emisiune.durata==2
                assert emisiune.descriere=="Viata la oras"
        print("Repo merge")

    def teste_service(self):
        #lista_emisiuni=self.__service_emisiuni.service_returneaza_lista
        lista,var=self.__service_emisiuni.program_generat(10,15)
        assert var == True
        print("Service merge")

