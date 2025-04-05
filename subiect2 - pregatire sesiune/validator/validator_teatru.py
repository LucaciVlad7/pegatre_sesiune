from exceptii.erori import ValidationError

class ValidatorTeatru:

    def valideaza_teatru(self,titlu,regizor,gen,durata):
        erori=""
        if titlu=="" or titlu[0].islower():
            erori+=f"Titlu invalid \n"
        if regizor=="" or regizor[0].islower():
            erori+=f"Regizor invalid \n"
        if gen!="Comedie" and gen!="Drama" and gen!="Satira" and gen!="Altele":
            erori+=f"Gen invalid \n"
        if durata<=0:
            erori+=f"Durata invalida \n"
        if len(erori)>0:
            raise ValidationError(erori)