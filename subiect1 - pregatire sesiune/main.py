from consola.consola_emisiuni import Consola
from repo.repo_emisiuni import RepoEmisiuni
from service.service_emisiuni import ServiceEmisiuni
from teste.teste_emisiuni import Teste


teste=Teste()
teste.ruleaza_toate_testele()
service=ServiceEmisiuni
#daca da eroare la lungime in repo da CTRL+Z in fisier ca sa fie iar 3
def main():
    consola=Consola(service)
    consola.run()

if __name__=="__main__":
    main()