import re 

def calculadora():
    print("Questão 1:\n")
    expressao = input('Digite uma expressão matemática apenas utilizando números e operadores (+), (-), (*), (/): ')
    expressao = expressao.replace(" ", "")
 
    if re.match(r'^[0-9+\-*/.()]+$', expressao):
        try: 
            resultado = eval(expressao)
            print(f'O resultado da expressão é = {resultado}')
        except Exception as e:
            print("Erro ao calcular a expressão:", e)
    else:
        print("Expressão inválida. Por favor, use apenas números e os operadores +, -, * e /.")
   