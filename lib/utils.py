import csv
import os

def criar_arquivos():
    arquivos = {
        'database/produtos.csv':
            ['id', 'nome', 'preco', 'categoria'],
        
        'database/pedidos.csv':
            ['id_pedido', 'mesa', 'produto', 'quantidade', 'total'],
    
        'database/mesas.csv':
            ['mesa', 'status'],

        'database/fechamento.csv':
            ['mesa', 'total', 'data']
    }

    for caminho, colunas in arquivos.items():
        if not os.path.exists(caminho):
            with open(caminho, 'w', newline='', encoding='utf-8') as arquivo:
                writer = csv.writer(arquivo)
                writer.writerow(colunas)
                print('Arquivos CSV criados com sucesso')