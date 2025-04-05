from domeniu.domeniu_evenimente import Eveniment

class RepoEvenimente:
    def __init__(self,cale_fisire):
        self.__cale_fisier=cale_fisire
        self.lista_evenimente=[]
        self.citeste_tot_din_fisier()

    def export_lista(self):
        return self.lista_evenimente

    def citeste_tot_din_fisier(self):
        with open(self.__cale_fisier,"r") as f:
            self.lista_evenimente.clear()
            lines=f.readlines()
            for line in lines:
                if line !="":
                    parts=line.split(",")
                    data=parts[0]
                    ora=parts[1]
                    descriere=parts[2]
                    event=Eveniment(data,ora,descriere)
                    self.lista_evenimente.append(event)

    def adauga_eveniment(self,eveniment):
        self.lista_evenimente.append(eveniment)
        self.append_fisier(eveniment)

    def append_fisier(self,eveniment):
        with open(self.__cale_fisier,"a") as f:
            f.write(f"{eveniment.get_data()},{eveniment.get_ora()},{eveniment.get_descriere()}\n")

