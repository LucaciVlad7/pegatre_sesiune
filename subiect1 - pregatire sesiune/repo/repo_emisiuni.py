from domeniu.domeniu_emisiuni import Emisiuni
from erori.erori_emisiuni import EroareDeNeexistanta, EroareDeBlocare


class RepoEmisiuni:
    def __init__(self,cale_fisier):
        self.__cale_fisier=cale_fisier
        self.lista_emisiuni=[]
        self.__citeste_tot_din_fisier()

    def blocare(self,tip):
        for emisiune in self.lista_emisiuni:
            if emisiune.tip == tip:
                emisiune.blocat=True


    def stergere_emisiune(self,nume,tip):
        """
        Sterge emisiunea cu numele si tipul dat sau afiseaza
        "Emisiunea nu exista" daca emisiunea nu exista
        :param nume: numele emisiunii dorite
        :param tip: tipul emisiunii dorite
        """
        lungime=len(self.lista_emisiuni)
        self.lista_emisiuni=[emisiune for emisiune in self.lista_emisiuni if (emisiune.nume!=nume or emisiune.tip!=tip) and emisiune.blocat==False]
        if lungime==len(self.lista_emisiuni):
            raise EroareDeNeexistanta("Evenimentul nu exista")
        self.scrie_tot_in_fisier()
        return self.lista_emisiuni

    def actualizare_durata_descriere(self,nume,tip,durata,descriere):
        """
        Inlocuieste durata si descrierea pt emisiunea cu nume si tip dat
        :param nume: Numele emisiunii
        :param tip: Tipul emisiunii
        :param durata: Durata care va fi inlocuita
        :param descriere: Descrierea care va fi inlocuita
        """
        schimbare=False
        blocat=False
        for emisiune in self.lista_emisiuni:
            if emisiune.nume==nume and emisiune.tip == tip:
                if emisiune.blocat==True:
                    raise EroareDeBlocare("Evenimentul este Blocat")
                    blocat=True
                else:
                    emisiune.durata=durata
                    emisiune.descriere=descriere
                    schimbare=True
        if blocat==True:
            raise EroareDeBlocare("Evenimentul este Blocat")
        elif schimbare==False:
            raise EroareDeNeexistanta("Evenimentul nu exista")
        return self.lista_emisiuni


    def returneaza_lista(self):
        """
        returneaza lista de emisiuni
        """
        return self.lista_emisiuni

    def __citeste_tot_din_fisier(self):
        """
        Citeste emisiunile din fisier si le introduce in lista
        """
        with open(self.__cale_fisier,"r") as f:
            self.lista_emisiuni.clear()
            lines=f.readlines()
            for line in lines:
                if line!="":
                    parts=line.split(",")
                    nume=parts[0]
                    tip=parts[1]
                    durata=int(parts[2])
                    descriere=parts[3]
                    emisiune=Emisiuni(nume,tip,durata,descriere,False)
                    self.lista_emisiuni.append(emisiune)

    def scrie_tot_in_fisier(self):
        """
        Scrie lista in fisier
        """
        with open(self.__cale_fisier,"w") as f:
            for emisiune in self.lista_emisiuni:
                f.write(f"{emisiune.nume},{emisiune.tip},{emisiune.durata},{emisiune.descriere}")

