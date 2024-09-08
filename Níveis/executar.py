from N1_Minhoquinha.questao1 import nomeCompleto
from N1_Minhoquinha.questao2 import substituir_palavra
from N1_Minhoquinha.questao3 import palavra_longa
from N1_Minhoquinha.questao4 import analise_frase
from N1_Minhoquinha.questao5 import string_de_numeros
from N2_Cobrinha.questao1 import calculadora
from N2_Cobrinha.questao2 import data_por_extenso
from N3_Python.questao1 import cadastrar_usuario
from N3_Python.questao2 import coletar_transacoes, vendas_por_produto,exibir_resultados,converter_moeda
from N3_Python.questao3 import sistema_gerenciamento_senhas

# Menu Principal

while True:
    print("Escolha um nível:")
    print("1 - Nível Minhoquinha")
    print("2 - Nível Cobrinha")
    print("3 - Nível Phython")
    print("4 - Sair do Sistema\n")

    nivel = input("Digite o número do nível: ")

    if nivel == "1":
        while True:
            print("\nNível Minhoquinha\n")
            print("Escolha qual questão deseja executar: ")
            print("1 - Questão 1 (Nome Completo)")
            print("2 - Questão 2 (Substituir Palavras)")
            print("3 - Questão 3 (Palavra mais longa)")
            print("4 - Questão 4 (Análise da frase)")
            print("5 - Questão 5 (String de números)")
            print("6 - Sair do Nível Minhoquinha\n")

            questao = input("Digite o número da questão ou aperte para sair (6):\n") 
            if questao == "1":
                nomeCompleto()
            elif questao == "2":
                substituir_palavra()
            elif questao == "3":
                palavra_longa()
            elif questao == "4":
                analise_frase()
            elif questao == "5":
                string_de_numeros()
            elif questao == "6":
                break 
            else:
                print("Opção inválida. Tente novamente.\n")


    elif nivel == "2":
        while True:
            print("\nNível Cobrinha\n")
            print("Escolha qual questão deseja executar: ")
            print("1 - Questão 1 (Calculadora)")
            print("2 - Questão 2 (Data por Extenso)")
            print("3 - Sair do Nível Cobrinha")

            questao = input("Digite o número da questão ou aperte para sair (3):\n")

            if questao == "1":
                calculadora()
            elif questao == "2":
                data_por_extenso() 
            elif questao == "3":
                break
            else:
                print("Opção inválida. Tente novamente.\n")

    elif nivel == "3":
        while True: 
            print("\nNível Phython\n")
            print("Escolha qual questão deseja executar: ")
            print("1 - Questão 1 (cadastrar Usuário)")
            print("2 - Questão 2 (Análise de Vendas)")
            print("3 - Questão 3 (Gerenciamento de Senhas)")
            print("3 - Questão 4 (x)")
            print("5 - Sair do Nível Phython")

            questao = input("Digite o número da questão ou aperte para sair (5):\n") 

            if questao == "1":
                cadastrar_usuario()
            elif questao == "2":
                 transacoes = coletar_transacoes()
                 vendas, quantidades = vendas_por_produto(transacoes)
                 exibir_resultados(vendas, quantidades)
                 converter_moeda(vendas)
            elif questao == "3":
                sistema_gerenciamento_senhas()
            elif questao == "4": 
                sistema_gerenciamento_senhas()
            elif questao == "5":
                break
            else:
                print("Opção inválida. Tente novamente.\n")

    elif nivel == "4":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.\n")