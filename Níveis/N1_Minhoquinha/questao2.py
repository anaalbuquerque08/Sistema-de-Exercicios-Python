def substituir_palavra(): 
    print("Questão 2:\n")
    texto = "Eu me chamo nome, tenho XX anos e sou estudante de Curso."
    print(texto)
    print("\nEsse é o texto principal. Você pode substituir várias palavras e, ao final, digite 'sair' para ver o texto final.\n")
    
    while True:
        palavra_substituida = input("Qual palavra deseja substituir (ou digite 'sair' para encerrar)? ")
         
        if palavra_substituida.lower() == "sair":
            break   
        
        palavra_nova = input("Digite a nova palavra: ")
         
        texto = texto.replace(palavra_substituida, palavra_nova)
     
    print("\nNovo texto final:\n")
    print(texto)
 