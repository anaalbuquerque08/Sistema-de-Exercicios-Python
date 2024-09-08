def coletar_transacoes():
    transacoes = []
    while True:
        print("Questão 2:\n")
        print('Informações do produto:')
        id_produto = input("  1-Digite o ID do Produto: ")
        nome_produto = input("  2-Digite o Nome do Produto: ")
 
        while True:
            try:
                quantidade = int(input("  3-Digite a Quantidade vendida: "))
                if quantidade < 0:
                    raise ValueError
                break
            except ValueError:
                print("Quantidade inválida. Por favor, insira um número inteiro positivo.")
 
        while True:
            try:
                valor_produto = float(input("  4-Digite o valor do produto: "))
                if valor_produto < 0:
                    raise ValueError
                break
            except ValueError:
                print("Valor inválido. Por favor, insira um número positivo.")

        transacao = f"{id_produto},{nome_produto},{quantidade},{valor_produto}"
        transacoes.append(transacao)

        continuar = input("Deseja adicionar outra transação? (s/n): ").lower()
        if continuar != 's':
            break

    return transacoes


def vendas_por_produto(transacoes):
    vendas_por_produto = {}
    quantidade_por_produto = {}

    for transacao in transacoes:
        id_produto, nome_produto, quantidade, valor_total = transacao.split(',')

        quantidade = int(quantidade)
        valor_total = float(valor_total) * quantidade   

        if nome_produto in vendas_por_produto:
            vendas_por_produto[nome_produto] += valor_total
            quantidade_por_produto[nome_produto] += quantidade
        else:
            vendas_por_produto[nome_produto] = valor_total
            quantidade_por_produto[nome_produto] = quantidade

    return vendas_por_produto, quantidade_por_produto


def produtos_mais_vendidos(quantidade_por_produto):
    max_quantidade = max(quantidade_por_produto.values())
    produtos = [produto for produto, quantidade in quantidade_por_produto.items() if quantidade == max_quantidade]
    return produtos


def produtos_maior_receita(vendas_por_produto):
    max_receita = max(vendas_por_produto.values())
    produtos = [produto for produto, valor in vendas_por_produto.items() if valor == max_receita]
    return produtos


def converter_moeda(vendas_por_produto):
    fator_conversao = float(input("\nDigite o fator de conversão para a moeda desejada: "))
    valores_convertidos = {}
    for produto, valor in vendas_por_produto.items():
        valor_convertido = valor * fator_conversao
        valores_convertidos[produto] = valor_convertido
        print(f"R$ {valor:.2f} para o produto '{produto}' fica no total de '{valor_convertido:.2f}' na moeda escolhida;")
    return valores_convertidos


def exibir_resultados(vendas, quantidades):
    for produto, valor in vendas.items():
        print(f"\nO valor total de vendas para {produto} foi: R$ {valor:.2f}")

    produtos_mais_vendidos_nome = produtos_mais_vendidos(quantidades)
    produtos_maior_receita_nome = produtos_maior_receita(vendas)

    print(f"\nOs produtos mais vendidos foram: {', '.join(produtos_mais_vendidos_nome)}")
    print(f"Os produtos que geraram a maior receita foram: {', '.join(produtos_maior_receita_nome)}")


 