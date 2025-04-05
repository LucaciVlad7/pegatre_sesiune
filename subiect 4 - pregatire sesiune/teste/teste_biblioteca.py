from repo.repo_biblioteca import RepoBiblioteca
from domeniu.domeniu_biblioteca import Biblioteca
from service.service_biblioteca import ServiceBiblioteca


class Teste:
    def __init__(self):
        self.__repo_bibilioteca=RepoBiblioteca("biblioteca.txt")
        self.__service_biblioteca=ServiceBiblioteca(self.__repo_bibilioteca)
    def ruleaza_teste(self):
        self.repo_teste()
        self.teste_service()

    def repo_teste(self):
        carte=Biblioteca(0,"Carte Test","Vlad",2025)
        self.__repo_bibilioteca.adauga_carte(carte)
        lista=self.__repo_bibilioteca.export_lista_biblioteca()
        assert len(lista)==1
        self.__repo_bibilioteca.sterge_carte(0)
        lista = self.__repo_bibilioteca.export_lista_biblioteca()
        assert len(lista) == 0
        print("Merge repo")

    def teste_service(self):
        crt_undo=[]

        carte=Biblioteca(0,"Carte Test","Vlad",2025)
        self.__service_biblioteca.service_adauga(carte)
        lista=self.__service_biblioteca.service_export_lista()
        assert len(lista)==1
        carte = Biblioteca(1, "Carte Test1", "Vlad", 2020)
        self.__service_biblioteca.service_adauga(carte)
        carte = Biblioteca(2, "Carte Test2", "Vlad", 2021)
        self.__service_biblioteca.service_adauga(carte)
        carte = Biblioteca(3, "Carte Test3", "Vlad", 2022)
        self.__service_biblioteca.service_adauga(carte)
        lista = self.__service_biblioteca.service_export_lista()
        assert len(lista) == 4
        lst=self.__service_biblioteca.fitrate_titlu_an("art",2023)
        assert len(lst) ==3
        self.__service_biblioteca.crt_undo(crt_undo,0)
        assert len(crt_undo)==1
        self.__repo_bibilioteca.sterge_carte(0)
        self.__repo_bibilioteca.sterge_carte(1)
        self.__repo_bibilioteca.sterge_carte(2)
        self.__repo_bibilioteca.sterge_carte(3)
        lista = self.__repo_bibilioteca.export_lista_biblioteca()
        assert len(lista)==0
        carte = Biblioteca(0, "Carte Test", "Vlad", 2025)
        self.__service_biblioteca.service_adauga(carte)
        lista = self.__service_biblioteca.service_export_lista()
        assert len(lista) == 1
        self.__service_biblioteca.undo(crt_undo)
        lista = self.__service_biblioteca.service_export_lista()

        print("Service repo")