import random

class ServiceMuzica:
    def __int__(self,repo,validator):
        self.__repo_muzica=repo
        self.validator_muzica=validator

    def service_export_lista_muzica(self):
        lista=self.__repo_muzica.export_lista()
        return lista

    def service_modifica_gen_si_durata(self,titlu,artist,gen,durata):
        self.validator_muzica.validator_muzica(titlu, artist, gen, durata)
        self.__repo_muzica. modifica_gen_si_durata(titlu, artist, gen, durata)

    def generare_aleator_melodii(self,nr_melodii,string_titluri,string_artisti):
        lista_titluri=string_titluri.split(",")
        lista_artisti=string_artisti.split(",")
        lista_gen=["Rock","Pop","Jazz","Altele"]
        for i in range(nr_melodii):
            titlu=random.choice(lista_titluri)
            artist=random.choice(lista_artisti)
            gen=random.choice(lista_gen)
            durata=random.randint(60,360)
            self.__repo_muzica.append_fisier(titlu, artist, gen, durata)

    def expot_in_fisier_sortat(self,nume_fisier):
        lista = self.__repo_muzica.export_lista()
        lista.sort(key=lambda ob: (ob.titlu,ob.artist))
        with open(nume_fisier,"w") as f:
            for piesa in lista:
                f.write(f"{piesa.titlu},{piesa.artist},{piesa.gen},{piesa.durata}\n")