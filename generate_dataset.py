# Gerar os dados aleatorios do poliglota idiomas

# Importing the libraries
import numpy as np
import pandas as pd
import random
import names

# Caso de teste
#id = np.array([1, 2])
#Unidade = np.array(["Butantã", "Paulista"])
#Nome_Cliente = np.array(["José Alpargadas", "Janice Souza"])
#Nome_Instituto = np.array(["POLI", "Nenhum"])
#Idioma = np.array(["Alemão", "Inglês"])
#Nível = np.array(["Básico", "Avançado"])
#Opção_Curso = np.array(["Extensivo", "Intensivo"])
#Periodicidade = np.array(["Semanal", "Sábado"])
#Preço = np.array([785, 1020])
#Data = np.array(["11/02/2014", "11/02/2014"])

# iniciaiza as numpy arrays
id = np.array([])
Unidade = np.array([])
Nome_Cliente = np.array([])
Nome_Instituto = np.array([])
Idioma = np.array([])
Nível = np.array([])
Opção_Curso = np.array([])
Periodicidade = np.array([])
Preço = np.array([])
Data = np.array([])

# Variáveis iniciais
n = 5000

# Todos os valores possíveis
totalUnidade = np.array(["Butantã", "Paulista"])
totalNome_InstitutoButantã = np.array(["POLI", "USP", "Nenhum"])
totalNome_InstitutoPaulista = np.array(["FMUSP", "USP", "Nenhum"])

totalIdioma = np.array(["Alemão", "Inglês", "Português", "Espanhol", "Francês", "Italiano"])
totalNível = np.array(["Básico", "Intermediário", "Avançado"])
totalOpção_Curso = np.array(["Intensivo", "Semi-Intensivo", "Extensivo", "Conversação"])
totalPeriodicidade = np.array(["Semanal", "Sábado"])
# Data será gerado pelo pandas

# Valores atuais inicializados em vazio
atualUnidade = []
atualNome_Instituto = []
atualIdioma = []
atualNível = []
atualOpção_Curso = []
atualPeriodicidade = []

# Funções de Auxílio

# Verifica as opções de curso dependendo da unidade
def Unidade_Instituto(atualUnidade, totalUnidade):
    if atualUnidade == totalUnidade[0]:
        return totalNome_InstitutoButantã
    else:
        return totalNome_InstitutoPaulista
    
# Define periodicidade dado a opção de curso
def Opção_Curso_Periodicidade(atualOpção_Curso, totalOpção_Curso):
    if atualOpção_Curso == "Extensivo":
        return random.choice(totalPeriodicidade)
    else:
        return "Semanal"
    
# Retorna o preço seguindo as condições do site do poliglota
def definePreço(atualNome_Instituto, atualOpção_Curso, atualPeriodicidade):
    # Define um aux para facilitar a categorização do preço por instituto
    aux = 0
    if atualNome_Instituto == "POLI" or atualNome_Instituto == "FMUSP":
        aux = 1
    
    # Verifica se extensivo
    if atualOpção_Curso == "Extensivo":
        # Extensivo de sábado
        if atualPeriodicidade == "Sábado":
            if aux == 1:
                return 830
            elif atualNome_Instituto == "USP":
                return 940
            elif atualNome_Instituto == "Nenhum":
                return 1020
        # Extensivo de semana
        else:
            if aux == 1:
                return 785
            elif atualNome_Instituto == "USP":
                return 900
            elif atualNome_Instituto == "Nenhum":
                return 965
            
    # Verifica se conversação
    elif atualOpção_Curso == "Conversação":
        if aux == 1:
            return 400
        elif atualNome_Instituto == "USP":
            return 450
        elif atualNome_Instituto == "Nenhum":
            return 485
        
    # Verifica se intensivo ou semi-intensivo mesmo preço    
    else:
        if aux == 1:
            return 785
        elif atualNome_Instituto == "USP":
            return 900
        elif atualNome_Instituto == "Nenhum":
            return 965

# Loop de geração de dados
for i in range(n):
    # Gera id
    id = np.append(id, i+1)
    
    # Gera Nome de clientes
    Nome_Cliente = np.append(Nome_Cliente, names.get_full_name())
    
    # Gera Unidade
    atualUnidade = random.choice(totalUnidade)
    Unidade = np.append(Unidade, atualUnidade)
    
    # Gera Instituto
    atualNome_Instituto = random.choice(Unidade_Instituto(atualUnidade, totalUnidade))
    Nome_Instituto = np.append(Nome_Instituto, atualNome_Instituto)
    
    # Gera Idioma
    atualIdioma = random.choice(totalIdioma)
    Idioma = np.append(Idioma, atualIdioma)
    
    # Gera Nível
    atualNível = random.choice(totalNível)
    Nível = np.append(Nível, atualNível)
    
    # Gera Opção_Curso
    atualOpção_Curso = random.choice(totalOpção_Curso)
    Opção_Curso = np.append(Opção_Curso, atualOpção_Curso)
    
    # Gera Periodicidade
    atualPeriodicidade = Opção_Curso_Periodicidade(atualOpção_Curso, totalOpção_Curso)
    Periodicidade = np.append(Periodicidade, atualPeriodicidade)
    
    # Gera Preço
    Preço = np.append(Preço, definePreço(atualNome_Instituto, atualOpção_Curso, atualPeriodicidade))
    
    # Gera Data
    ano = random.randint(2014, 2016)
    mês = random.randint(1, 12)
    dia = random.randint(1, 28)
    Data = np.append(Data, str(dia) + "/" + str(mês) + "/" + str(ano))
    
    
# Gera o dataframe resultante dos arrays
DataFrame = pd.DataFrame.from_items([
        ('id', id),
        ('Unidade', Unidade),
        ('Nome_Cliente', Nome_Cliente),
        ('Nome_Instituto', Nome_Instituto),
        ('Idioma', Idioma),
        ('Nível', Nível),
        ('Opção_Curso', Opção_Curso),
        ('Periodicidade', Periodicidade),
        ('Preço', Preço),
        ('Data', Data)
])

# Passo final, escreve todos os dados em excel
writer = pd.ExcelWriter('Dados_Poliglota_Idiomas_5.xlsx', engine='xlsxwriter')
DataFrame.to_excel(writer, sheet_name='Sheet1')
writer.save()