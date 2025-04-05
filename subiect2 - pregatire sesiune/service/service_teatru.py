import random
from domeniu.domeniu_teatru import Teatru

class ServiceTeatru:
    def __init__(self,repo,validator):
        self.__repo=repo
        self.__validator=validator

    def adaugare_service(self,titlu,regizor,gen,durata):
        self.__validator. valideaza_teatru(titlu,regizor,gen,durata)
        self.__repo.adaugare(titlu,regizor,gen,durata)

    def export_lista(self):
        lista=self.__repo.export_lista()
        return lista

    def generare_titlu_sau_regizor(self):
        lungime=random.randint(8,12)
        vocale = ['a', 'e', 'i', 'o', 'u']
        consoane = [
            'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
            'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'
                    ]
        nume=""
        prima=random.randint(1,2)
        if prima==1:
            for i in range(lungime):
                if i % 2 == 0:
                    index=random.randint(0,len(vocale)-1)
                    nume+=vocale[index]
                else:
                    index = random.randint(0, len(consoane)-1)
                    nume += consoane[index]
            spatiu=random.randint(1,lungime)
            nume=nume[:spatiu]+ " " + nume[spatiu+1:]
        else:
            for i in range(lungime):
                if i % 2 == 1:
                    index=random.randint(0,len(vocale)-1)
                    nume+=vocale[index]
                else:
                    index = random.randint(0, len(consoane)-1)
                    nume += consoane[index]
            spatiu=random.randint(1,lungime)
            nume=nume[:spatiu]+ " " + nume[spatiu+1:]
        nume=nume.capitalize()
        return nume

    def creare_piese_teatru(self,numar_piese):
        lista_generate=[]
        lista_gen=["Comedie","Drama","Satira","Altele"]
        for i in range(numar_piese):
            titlu=self.generare_titlu_sau_regizor()
            regizor=self.generare_titlu_sau_regizor()
            gen=random.choice(lista_gen)
            durata=random.randint(60,3600)
            self.__repo.adaugare(titlu,regizor,gen,durata)
            piesa=Teatru(titlu,regizor,gen,durata)
            lista_generate.append(piesa)

    def export_lista_in_fisier(self,nume_fisier):
        lista=self.__repo.export_lista()
        lista.sort(key=lambda ob: (ob.titlu,ob.regizor))
        with open(nume_fisier,"w") as f:
            for piesa in lista:
                f.write(f"{piesa.titlu},{piesa.regizor},{piesa.gen},{piesa.durata}\n")