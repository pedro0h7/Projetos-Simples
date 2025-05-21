estoque = dict()

def adcionar_estoque():
    nome = str(input('Nome do produto: '))
    quantidade = int(input('Quantidade: '))
    preco = float(input('Preço: R$'))
    
    if nome in estoque:
        print(f'O produto {nome} já está cadastrado, atualizando quantidade')
        estoque[nome]['quantidade'] += quantidade
        estoque[nome]['preço'] = preco
    else:
        estoque[nome] = {'quantidade': quantidade, 'preço': preco}
    print(f'O produto {nome} foi atualizado/cadastrado com sucesso!')

def atualizar_quantidade():
    nome = str(input('Nome do produto: '))
    if nome in estoque:
        nova_quantidade = int(input('Quantidade nova: '))
        estoque[nome]['quantidade'] = nova_quantidade
        print(f'A quantidade do produto {nome} atualizado para {nova_quantidade}')
    else:
        print('Produto não achado!')

def remover_produto():
    nome = str(input('Nome do produto: '))
    if nome in estoque:
        del estoque[nome]
        print(f'O produto {nome} foi removido com sucesso!')
    else:
        print(f'O produto {nome} não encontrado no estoque!')

def exibir_estoque():
    if not estoque:
        print('O estoque está vazio!')
    else:
        for nome, detalhes in estoque.items():
            print(f"Produto: {nome}, Quantidade: {detalhes['quantidade']}, Preço: R${detalhes['preço']:.2f}")

#menu principal
def linha(tam=40):
    return '-'* tam

def cabecalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for items in lista:
        print(f'{c} - {items}')
        c += 1
    print(linha())
    opc = int(input('Sua opção: '))
    return opc
