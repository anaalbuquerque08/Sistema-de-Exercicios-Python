import random
import string

def sistema_gerenciamento_senhas():
    while True:
        print("\nSistema de Gerenciamento de senha:")
        print("1 - Gerar nova senha")
        print("2 - Verificar senha existente")
        print("3 - Criptografar senhas")
        print("4 - Descriptografar senhas")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        # Definindo todos os caracteres no início
        letras_maiusculas = string.ascii_uppercase
        letras_minusculas = string.ascii_lowercase
        numeros = string.digits
        caracteres_especiais = string.punctuation
        todos_caracteres = letras_maiusculas + letras_minusculas + numeros + caracteres_especiais

        if opcao == '1':
            tamanho = 8
            senha = [
                random.choice(letras_maiusculas),
                random.choice(letras_minusculas),
                random.choice(numeros),
                random.choice(caracteres_especiais),
            ]
            senha += random.choices(todos_caracteres, k=tamanho - 4)
            random.shuffle(senha)
            senha_final = ''.join(senha)
            print(f"Senha gerada: {senha_final}")
            continue

        elif opcao == '2':
            senha = input("Digite a senha para verificar: ")
            if (len(senha) >= 8 and
                    any(c.islower() for c in senha) and
                    any(c.isupper() for c in senha) and
                    any(c.isdigit() for c in senha) and
                    any(c in string.punctuation for c in senha)):
                print("A senha atende aos critérios de segurança.")
            else:
                print("A senha não atende aos critérios. Gerando nova senha segura...")
                senha_nova = ''.join(random.choices(todos_caracteres, k=8))
                print(f"Nova senha sugerida: {senha_nova}")
            continue

        elif opcao == '3':
            senha_para_criptografar = input("Digite a senha para criptografar: ")
            deslocamento = 3
            senha_criptografada = ''.join([chr((ord(c) + deslocamento) % 256) for c in senha_para_criptografar])
            print(f"Senha criptografada: {senha_criptografada}")
            continue

        elif opcao == '4':
            senha_para_descriptografar = input("Digite a senha criptografada: ")
            deslocamento = 3
            senha_descriptografada = ''.join([chr((ord(c) - deslocamento) % 256) for c in senha_para_descriptografar])
            print(f"Senha descriptografada: {senha_descriptografada}")
            continue

        elif opcao == '5':
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")
 