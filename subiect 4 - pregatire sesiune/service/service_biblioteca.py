from domeniu.domeniu_biblioteca import Biblioteca


class ServiceBiblioteca:
    def __init__(self,repo):
        self.__repo=repo

    def service_export_lista(self):
        lista=self.__repo.export_lista_biblioteca()
        return lista

    def service_adauga(self,carte):
        self.__repo.adauga_carte(carte)

    def fitrate_titlu_an(self,titlu,an_aparitie):
        lista=[]
        lista_biblioteca=self.__repo.export_lista_biblioteca()
        for carte in lista_biblioteca:
            if titlu in carte.titlu and carte.an_aparitie<an_aparitie:
                lista.append(carte)
        return lista

    def crt_undo(self,crt_undo,cif):
        lista=self.__repo.export_lista_biblioteca()
        lista=[el for el in lista if cif != el.id_carte]
        copy_list=[]
        for el in lista:
            copy_list.append(Biblioteca(el.id_carte,el.titlu,el.autor,el.an_aparitie))
        crt_undo.append(copy_list)

    def undo(self,crt_undo):
        errors=""
        if (len(crt_undo))==0:
            errors+="Nu se poate face undo!"
        else:
            for el in crt_undo[-1]:
                carte=Biblioteca(el.id_carte,el.titlu,el.autor,el.an_aparitie)
                self.__repo.adauga_carte(carte)

            crt_undo.pop(-1)

        if len(errors)>0:
            raise ValueError(errors)