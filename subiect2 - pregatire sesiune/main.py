from teste.teste_teatru import TesteTeatru
from consola.consola_teatru import Consola
from repo.repo_teatru import RepoTeatru
from service.service_teatru import ServiceTeatru
from validator.validator_teatru import ValidatorTeatru
teste=TesteTeatru()
teste.ruleaza_toate_testele()
repo=RepoTeatru("teatru.txt")
validator=ValidatorTeatru
service=ServiceTeatru(repo,validator)
consola=Consola(service)
consola.run()
