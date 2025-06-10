#venv\Scripts\activate
import pandas as pd
from faker import Faker # pip intall faker
import random



fake = Faker('en_US')
#faker = Faker('pt_BR')

#função para gerar o dataframe
def gerar_dados_brutos(num_registros):
    dados_brutos=[]
    lista_cidades = set()

    while len(dados_brutos) < num_registros:
        nome_cidade = fake.city()
        if nome_cidade not in lista_cidades:
            lista_cidades.add(nome_cidade)
            #gerar população aleatoria entre 10k e 5mi
            populacao = fake.random_int(min=10000, max=5000000)
            #gerar taxa de homicidios entre 1.0 e 15.0 arredondado e com uma casa decimal
            taxa_homicidios = round(random.uniform(1.0, 15.0), 1)
            dados_brutos.append({"cidade": nome_cidade,
                                 "populacao": populacao,
                                 "taxa taxa_homicidios": taxa_homicidios
                                 
            })
    return pd.DataFrame(dados_brutos)

num_registros=10
df= gerar_dados_brutos(num_registros)
#Exibir o data frame
print(df)

output_csv_file = "taxa_homicidios.csv"
df.to_csv(output_csv_file, index=False)

