def data_por_extenso(): 
    print("Questão 2:\n")
    unidades = {
        0: "", 1: "um", 2: "dois", 3: "três", 4: "quatro", 5: "cinco", 6: "seis", 7: "sete", 8: "oito", 9: "nove", 10: "dez",
        11: "onze", 12: "doze", 13: "treze", 14: "quatorze", 15: "quinze", 16: "dezesseis", 17: "dezessete", 18: "dezoito", 19: "dezenove"
    }
    dezenas = {
        2: "vinte", 3: "trinta", 4: "quarenta", 5: "cinquenta", 6: "sessenta", 7: "setenta", 8: "oitenta", 9: "noventa"
    }
    centenas = {
        1: "cento", 2: "duzentos", 3: "trezentos", 4: "quatrocentos", 5: "quinhentos", 6: "seiscentos", 7: "setecentos", 8: "oitocentos", 9: "novecentos"
    }
    meses = {
        1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril", 5: "maio", 6: "junho", 
        7: "julho", 8: "agosto", 9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"
    }

    while True:
        data = input('Digite uma data no formato (DD/MM/AAAA):\n') 
        try:
            dia, mes, ano = data.split('/')
            dia_num = int(dia)
            mes_num = int(mes)
            ano_num = int(ano) 

            if dia_num < 1 or dia_num > 31:
                raise ValueError("Dia deve estar entre 1 e 31.")
            if mes_num < 1 or mes_num > 12:
                raise ValueError("Mês deve estar entre 1 e 12.")
            if ano_num < 1000 or ano_num > 9999:
                raise ValueError("Ano deve estar entre 1000 e 9999.")
 
            if dia_num < 20:
                dia_extenso = unidades[dia_num]
            else:
                dia_extenso = dezenas[dia_num // 10] + (" e " + unidades[dia_num % 10] if dia_num % 10 != 0 else "")
             
            mes_extenso = meses[mes_num]
         
            milhar_digito = int(ano[0])   
            centena_digito = int(ano[1])   
            dezena_digito = int(ano[2])    
            unidade_digito = int(ano[3])  

            ano_extenso = f"{unidades[milhar_digito]} mil"
            if centena_digito > 0:
                ano_extenso += f" {centenas[centena_digito]}"
            if dezena_digito == 1:
                ano_extenso += f" e {unidades[dezena_digito * 10 + unidade_digito]}"
            else:
                if dezena_digito > 1:
                    ano_extenso += f" e {dezenas[dezena_digito]}"
                if unidade_digito > 0:
                    ano_extenso += f" e {unidades[unidade_digito]}"
             
            print(f"Dia {dia_extenso.capitalize()} de {mes_extenso} de {ano_extenso.strip()}.")
            break   

        except (ValueError, IndexError):
            print("Erro: O formato da data está incorreto. Por favor, digite no formato DD/MM/AAAA.")
 