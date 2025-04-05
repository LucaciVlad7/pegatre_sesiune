from teste.teste_muzica import TesteMuzica
from consola.consola_muzica import Consola
from service.service_muzica import ServiceMuzica
from validator.validator_service import ValidatorMuzica
from repo.repo_muzica import RepoMuzica


validator=ValidatorMuzica()
repo=RepoMuzica("muzica.txt")
service=ServiceMuzica(repo,validator)
teste=TesteMuzica()
teste.ruleaza_toate_testele()

consola=Consola(service)
consola.run()