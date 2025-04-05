from erori.erori_muzica import ValidationError

class Consola:

    def __init__(self,_service_muzica):
        self.__service_muzica=_service_muzica
        self.__comenzi ={
                "lista_noua":self.__ui_export_fisier_sortat
        }

    def __ui_export_fisier_sortat(self):
        nume_fisier=input("Numele fisierului dorit: ")
        self.__service_muzica.xpot_in_fisier_sortat(nume_fisier)



    def run(self):
        while True:
            nume_comanda = input(">>>")
            nume_comanda = nume_comanda.lower()
            nume_comanda = nume_comanda.strip()
            if nume_comanda == "":
                continue
            if nume_comanda == "exit":
                break
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda]()
                except ValidationError as ve:
                    print(f"eroare de validare:{ve}")
            else:
                print("comanda invalida!")