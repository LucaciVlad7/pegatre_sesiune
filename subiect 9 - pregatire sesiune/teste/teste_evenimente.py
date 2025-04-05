from repo.repo_evenimente import RepoEvenimente
from service.service_repo import ServiceEvenimente
from validator.valideaza_evenimente import ValidatorEvenimente
from domeniu.domeniu_evenimente import Eveniment
class TesteEvenimente():
    def __init__(self):
        self.__validator=ValidatorEvenimente
        self.__repo=RepoEvenimente("evenimente.txt")
        self.__service=ServiceEvenimente(self.__repo,self.__validator)

    def ruleaza_tot(self):
        self.repo_teste()
        self.service_teste()

    def repo_teste(self):
        eveniment=Eveniment("25.01.2025","11:11","Aunta")
        self.__repo.adauga_eveniment(eveniment)
        lista=self.__repo.export_lista()
        assert len(lista)==1
        eveniment = Eveniment("11.11.2025", "13:11", "Bunta")
        self.__repo.adauga_eveniment(eveniment)
        eveniment = Eveniment("25.01.2025", "14:11", "Cunta")
        self.__repo.adauga_eveniment(eveniment)
        eveniment = Eveniment("41.11.2025", "15:11", "Dunta")
        self.__repo.adauga_eveniment(eveniment)
        lista = self.__repo.export_lista()
        assert len(lista) == 4

    def service_teste(self):
        lista=self.__service.afiseaza_evenimentele_de_azi()
        assert len(lista)==2
        assert lista[0].get_ora()=="11:11"

        lista=self.__service.afisare_evenimente_dupa_data("11.11.2025")
        assert len(lista)==1

        lista=self.__service.export_lista_in_fisier("un")
        assert len(lista)==4
        assert lista[0].get_data()=="11.11.2025"
        assert lista[2].get_descriere()=="Cunta"