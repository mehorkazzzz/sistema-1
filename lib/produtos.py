import csv

def cadastrar_produtos():
    while True:
        nome = input('Nome do produto: ').strip()
        if nome == '':
            print('O nome não pode ficar vazio!')
        else:
            break
    while True:
        try:
            preco = float(input('Preço do produto: '))
            if preco <= 0:
                print('O preço deve ser maior que zero!')
            else:
                break
        except ValueError:
            print('Digite um número válido!')
    while True:
        categoria = input('Categoria do produto: ').strip()
        if categoria == '':
            print('A categoria não pode ficar vazia!')
        else:
            break
    id_produto = 1
    with open('database/produtos.csv', 'r', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo)
        next(reader)
        for linha in reader:
            id_produto = int(linha[0]) + 1

    with open('database/produtos.csv', 'a', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([
            id_produto,
            nome,
            preco,
            categoria
        ])
    print('Produto cadastrado com sucesso!')

def listar_produtos():
    print('Entrou na função listar')
    with open('database/produtos.csv', 'r', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo)
        next(reader)
        print('\n--- PRODUTOS CADASTRADOS ---\n')
        for linha in reader:
            print(
                f'ID: {linha[0]} | '
                f'Nome: {linha[1]} | '
                f'Preço: {linha[2]} | '
                f'Categoria: {linha[3]}'
            )

def remover_produtos():
    listar_produtos()
    id_remover = input('Digite o ID do produto que deseja remover: ').strip()
    produtos = []
    with open('database/produtos.csv', 'r', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo)
        cabecalho = next(reader)
        for linha in reader:
            if linha[0] != id_remover:
                produtos.append(linha)
    with open('database/produtos.csv', 'w', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(cabecalho)
        writer.writerows(produtos)
        print('\nProduto removido com sucesso!')