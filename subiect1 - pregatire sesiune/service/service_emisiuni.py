import random
from domeniu.domeniu_linie_tabel import LinieTabel

from domeniu.domeniu_emisiuni_cu_indici import EmisiuniIndici

class ServiceEmisiuni:
    def __init__(self,repo):
        self.__repo_emisiuni=repo

    def service_blocare(self,tip):
        self.__repo_emisiuni.blocare(tip)


    def service_stergere_emisiune(self,nume,tip):
        """
        Sterge emisiunea cu numele si tipul dat sau afiseaza
        "Emisiunea nu exista" daca emisiunea nu exista folosind functia din repo
        :param nume: numele emisiunii dorite
        :param tip: tipul emisiunii dorite
        """
        lista_emisiuni=self.__repo_emisiuni.stergere_emisiune(nume,tip)
        return lista_emisiuni

    def service_actualizare_durata_descriere(self,nume,tip,durata,descriere):
        """
        Inlocuieste durata si descrierea pt emisiunea cu nume si tip dat,
        folosind functia din repo
        :param nume: Numele emisiunii
        :param tip: Tipul emisiunii
        :param durata: Durata care va fi inlocuita
        :param descriere: Descrierea care va fi inlocuita
        """
        lista_emisiuni=self.__repo_emisiuni.actualizare_durata_descriere(nume,tip,durata,descriere)
        return lista_emisiuni

    def service_returneaza_lista(self):
        """
          returneaza lista de emisiuni,folosind repo
        """
        lista_emisiuni=self.__repo_emisiuni.returneaza_lista
        return lista_emisiuni

    def creare_lista_indici(self,lista_emisiune):
        indice=-1
        lista_emisiune_cu_indici=[]
        for emisiune in lista_emisiune:
            indice+=1
            emisiune_ind=EmisiuniIndici(indice,emisiune.nume,emisiune.tip,emisiune.durata,emisiune.descriere)
            lista_emisiune_cu_indici.append(emisiune_ind)
        return lista_emisiune_cu_indici

    def posibilitate(self,ora_inceput,ora_final,lista_emisiune):
        exista=False
        for emisiune in lista_emisiune:
            if ora_inceput+emisiune.durata<=ora_final:
                exista=True
        return exista

    def program_generat(self,ora_inceput,ora_final):
        lista_tabel=[]
        if ora_final<ora_inceput:
            ora_final=24+ora_final
        lista_emisiune=self.__repo_emisiuni.returneaza_lista()
        lista_emisiune_cu_indici=self.creare_lista_indici(lista_emisiune)
        while ora_inceput<ora_final:
            if self.posibilitate==False:
                return None,None
            indice=random.randint(0,len(lista_emisiune_cu_indici)-1)
            if ora_inceput+lista_emisiune_cu_indici[indice].durata<=ora_final:
                linie_tabel=LinieTabel(ora_inceput,lista_emisiune_cu_indici[indice].nume,lista_emisiune_cu_indici[indice].tip,lista_emisiune_cu_indici[indice].descriere)
                if lista_emisiune_cu_indici[0].descriere[len(lista_emisiune_cu_indici[0].descriere)-1]!='*':
                    lista_emisiune_cu_indici[0].descriere+="****"
                    linie_tabel.descriere+="****"
                ora_inceput+=lista_emisiune_cu_indici[indice].durata
                lista_tabel.append(linie_tabel)
        return lista_tabel,True