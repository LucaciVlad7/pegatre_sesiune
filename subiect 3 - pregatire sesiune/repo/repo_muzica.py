from domeniu.domeniu_muzica import Muzica

class RepoMuzica:
    def __init__(self,cale_fisier):
        self.__cale_fisier=cale_fisier
        self.lista_muzica=[]
        self.citeste_tot_din_fisier()

    def export_lista(self):
        return self.lista_muzica

    def modifica_gen_si_durata(self,titlu,artist,gen,durata):
        for piesa in self.lista_muzica:
            if piesa.titlu== titlu and piesa.artist==artist:
                piesa.gen=gen
                piesa.durata=durata
        self.scrie_tot_in_fisier()

    def append_fisier(self,titlu,artist,gen,durata):
        with open(self.__cale_fisier,"a") as f:
            f.write(f"{titlu},{artist},{gen},{durata}")

    def citeste_tot_din_fisier(self):
        with open(self.__cale_fisier,"r") as f:
            self.lista_muzica.clear()
            lines=f.readlines()
            for line in lines:
                if line!="":
                    line.strip()
                    parts=line.split(",")
                    titlu=parts[0]
                    artist=parts[1]
                    gen=parts[2]
                    durata=int(parts[3])
                    piesa=Muzica(titlu,artist,gen,durata)
                    self.lista_muzica.append(piesa)

    def scrie_tot_in_fisier(self):
        with open(self.__cale_fisier,"w") as f:
            for piesa in self.lista_muzica:
                f.write(f"{piesa.titlu},{piesa.artist},{piesa.gen},{piesa.durata}\n")