from exceptii.erori import ValidationError

class Consola:

    def __init__(self,_service_teatru):
        self.__service_teatru=_service_teatru
        self.__comenzi ={

        }


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