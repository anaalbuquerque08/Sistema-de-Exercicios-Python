import re
from collections import Counter

def processar_textos_juridicos():
    print("Questão 4:\n")
    contrato = input("Digite o texto completo do contrato:\n")
 
    contrato = re.sub(r'\s+', ' ', contrato)
   
    clausulas_valores = re.findall(r'(?i)(cláusula.*?)(?=\s*\n|\Z)', contrato)
    valores_monetarios = []
    
    for clausula in clausulas_valores:  
        encontrados = re.findall(r'R\$?\s*[\d.]+(?:,[\d]{2})?', clausula)
        valores_monetarios.extend(encontrados)

    print("\nValores monetários encontrados:")
    print(valores_monetarios)
  
    termos_legais = input("\nDigite os termos legais separados por vírgula:\n").split(',')
    termos_legais = [termo.strip() for termo in termos_legais]
    ocorrencias = Counter(re.findall(r'\b\w+\b', contrato.lower()))

    print("\nFrequência dos termos legais:")
    for termo in sorted(termos_legais, key=lambda x: ocorrencias[x.lower()], reverse=True):
        print(f"{termo}: {ocorrencias[termo.lower()]}")
