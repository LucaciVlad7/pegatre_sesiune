from datetime import date

class ServiceEvenimente:
    def __init__(self,repo,validator):
        self.__repo=repo
        self.__validator=validator


    def adauga(self,eveniment):
        self.__validator.valideaza_evenimente(eveniment)
        self.__repo.adauga_eveniment(eveniment)

    def afiseaza_evenimentele_de_azi(self):#in service
        lista_evenimente=self.__repo.export_lista()
        data_azi=date.today()
        lista=[]
        for event in lista_evenimente:
            curent=event.get_data()
            parts=curent.split(".")
            zi=int(parts[0])
            luna=int(parts[1])
            an=int(parts[2])
            if data_azi.day==zi and luna == data_azi.month and an == data_azi.year:
                lista.append(event)

        lista.sort(key=lambda ob:(ob.get_ora(),ob.get_descriere()))
        return lista

    def afisare_evenimente_dupa_data(self,data):
        lista=[]
        lista_evenimente=self.__repo.export_lista()
        for eveniment in lista_evenimente:
            if eveniment.get_data()==data:
                lista.append(eveniment)
        return lista

    def export_lista_in_fisier(self,sir):
        lista=[]
        lista_evenimente=self.__repo.export_lista()
        for evenimente in lista_evenimente:
            if sir in evenimente.get_descriere():
                lista.append(evenimente)
        lista.sort(key=lambda ob:(ob.get_data(),ob.get_ora()))
        return lista