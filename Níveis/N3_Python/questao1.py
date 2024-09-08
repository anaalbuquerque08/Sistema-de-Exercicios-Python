import re

def validar_cpf(cpf): 
    cpf = cpf.replace('.', '').replace('-', '')   
    if len(cpf) != 11 or not cpf.isdigit():
        return "CPF inválido. Deve conter 11 dígitos."
    
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"   

def validar_email(email): 
    email = email.lower()   
    padrao = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(padrao, email):
        return "E-mail inválido. O formato deve ser 'login@dominio.com'."
    
    return email   

def validar_telefone(telefone):
    telefone = re.sub(r'\D', '', telefone)   
    if len(telefone) < 10 or len(telefone) > 11:
        return "Número de telefone inválido. Deve conter o DDD e o número."
    if len(telefone) == 11:  
        return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    else:   
        return f"({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}"


def cadastrar_usuario(): 
    print("Por favor, digite os dados a seguir:")
    
    cpf = input("CPF: ")
    cpf_formatado = validar_cpf(cpf)
    if "inválido" in cpf_formatado:
        print(cpf_formatado)
        return

    email = input("E-mail: ")
    email_normalizado = validar_email(email)
    if "inválido" in email_normalizado:
        print(email_normalizado)
        return

    telefone = input("Telefone: ")
    telefone_formatado = validar_telefone(telefone)
    if "inválido" in telefone_formatado:
        print(telefone_formatado)
        return

    print("\nDados válidos Cadastrados:")
    print(f"CPF: {cpf_formatado}")
    print(f"E-mail: {email_normalizado}")
    print(f"Telefone: {telefone_formatado}")

  