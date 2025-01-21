from erori.erori_emisiuni import EroareDeBlocare, EroareDeNeexistanta


class Consola:
    def __init__(self,_service_emisiune):
        self.__service_emisiune=_service_emisiune
        self.__comenzi ={
            "afisare":self.__ui_afisare,
        }

    def __ui_afisare(self):
        lista=self.__service_emisiune.service_returneaza_lista()
        contor=1
        for emisiune in lista:
            print(f"Emisiunea {contor}: {emisiune.nume}, {emisiune.tip}, {emisiune.descriere}, {emisiune.durata}")

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
                except EroareDeBlocare as eb:
                    print(f"eroare de blocare: {eb}")
                except EroareDeNeexistanta as en:
                    print(f"erorare de neexistenta:{en}")
            else:
                print("comanda invalida!")