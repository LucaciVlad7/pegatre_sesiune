from teste.teste_evenimente import TesteEvenimente
from ui.ui_evenimente import Consola
from validator.valideaza_evenimente import ValidatorEvenimente
from service.service_repo import ServiceEvenimente
from repo.repo_evenimente import RepoEvenimente
#teste=TesteEvenimente()
#teste.ruleaza_tot()

repo=RepoEvenimente("evenimente.txt")
valid=ValidatorEvenimente()
service=ServiceEvenimente(repo,valid)
consola=Consola(service)

consola.run()