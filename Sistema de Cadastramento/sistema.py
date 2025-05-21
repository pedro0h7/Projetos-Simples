from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'pedrinho.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #opção de listar o conteúdo de um arquivo
        lerarquivo(arq)
    elif resposta == 2:
        #Opcao de cadastrar nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        #Opçao de sair do sistema
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        #Digitou um número errado no menu
        print('\033[0;31mERRO! Digite uma opção válida\033[m')
    sleep(2)

