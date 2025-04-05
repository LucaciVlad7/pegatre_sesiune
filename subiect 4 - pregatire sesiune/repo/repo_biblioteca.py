from domeniu.domeniu_biblioteca import Biblioteca
from erori.erori_biblioteca import RepoError

class RepoBiblioteca:
    def __init__(self,nume_fisier):
        self.__cale_fisier=nume_fisier
        self.lista_bibiloateca=[]
        self.lista_undo=[]

    def export_lista_biblioteca(self):
        return self.lista_bibiloateca

    def adauga_carte(self,carte):
        self.lista_undo=self.export_lista_biblioteca()
        if carte.id_carte in self.lista_bibiloateca:
            raise RepoError("Id-ul exista deja")
        else:
            self.lista_bibiloateca.append(carte)
            self.append_in_fisier(carte)

    def sterge_carte(self,cifra):
        self.lista_undo = self.export_lista_biblioteca()
        self.lista_bibiloateca=[carte for carte in self.lista_bibiloateca if str(cifra) not in str(carte.id_carte)]
        self.scrie_tot_in_fisier()

    def scrie_tot_in_fisier(self):
        with open(self.__cale_fisier,"w") as f:
            for carte in self.lista_bibiloateca:
                f.write(f"{carte.id_carte},{carte.titlu},{carte.autor},{carte.an_aparitie}\n")

    def append_in_fisier(self,carte):
        with open(self.__cale_fisier,"a") as f:
            f.write(f"{carte.id_carte},{carte.titlu},{carte.autor},{carte.an_aparitie}\n")