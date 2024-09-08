def string_de_numeros():
    print("Questão 5:\n")
    string_numero = input('Digite uma string de número para realizar a soma de cada um deles (Exemplo: 1234):\n')
    
    if string_numero.isdigit(): 
        lista_digitos = [int(digito) for digito in string_numero]
        soma = sum(lista_digitos)
 
        print(f'A soma dos dígitos da string {lista_digitos} é igual a {soma};')
    else:
        print("A string contém caracteres não numéricos. Por favor, insira apenas números.")
 