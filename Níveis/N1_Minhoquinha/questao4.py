def analise_frase():
    print("Questão 4:\n")
    frase = input('Digite uma frase:')
    caracteres = len(frase)
    palavras = len(frase.split())
    vazios = frase.count(' ')

    print('Na frase "{}" há: \n {} caracteres; \n {} palavras; \n {} espaços vazios.'.format(frase,caracteres, palavras,vazios))
 