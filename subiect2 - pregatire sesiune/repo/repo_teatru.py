from domeniu.domeniu_teatru import Teatru

class RepoTeatru:
    def __init__(self,cale_fisier):
        self.__cale_fisier=cale_fisier
        self.lista_teatru=[]
        self.__citeste_tot_din_fisier()


    def adaugare(self,titlu,regizor,gen,durata):
        piesa = Teatru(titlu, regizor, gen, durata)
        self.lista_teatru.append(piesa)
        self.append_fisier(titlu,regizor,gen,durata)

    def export_lista(self):
        return self.lista_teatru

    def append_fisier(self,titlu,regizor,gen,durata):
        with open(self.__cale_fisier,"a") as f:
            f.write(f"{titlu},{regizor},{gen},{durata}\n")

    def __citeste_tot_din_fisier(self):
        with open(self.__cale_fisier,"r") as f:
            self.lista_teatru.clear()
            lines=f.readlines()
            for line in lines:
                if line != "":
                    parts=line.split(",")
                    titlu=parts[0]
                    regizor=parts[1]
                    gen=parts[2]
                    durata=int(parts[3])
                    piesa=Teatru(titlu,regizor,gen,durata)
                    self.lista_teatru.append(piesa)