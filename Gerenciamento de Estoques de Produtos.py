import e07modulo
from time import sleep

while True:
    resposta = e07modulo.menu(['Adcionar um produto', 'Remover produto',
                              'Atualizar a quantidade do produto', 'Exibir estoque', 'Sair do Sistema'])

    if resposta == 1:
        e07modulo.cabecalho('CADASTRANDO PRODUTO')
        e07modulo.adcionar_estoque()

    elif resposta == 2:
        e07modulo.cabecalho('REMOVENDO PRODUTO')
        e07modulo.remover_produto()

    elif resposta == 3:
        e07modulo.cabecalho('ATUALIZANDO PRODUTO')
        e07modulo.atualizar_quantidade()

    elif resposta == 4:
        e07modulo.cabecalho('EXIBIR ESTOQUE')
        e07modulo.exibir_estoque()

    elif resposta == 5:
        e07modulo.cabecalho('SAINDO DO PROGRAMA')
        break

    else:
        print('Opção inválida!')
    sleep(2)
