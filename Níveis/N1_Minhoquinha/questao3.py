import string

def palavra_longa():
     print("Questão 3:\n")
     frase = input("Digite uma frase: ")
     frase_sem_pontuacao = frase.translate(str.maketrans('', '', string.punctuation))
     palavras = frase_sem_pontuacao.split()
     maior_palavra = max(palavras, key=len) if palavras else ""
     print("A palavra mais longa é:", maior_palavra)
 