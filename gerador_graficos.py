import collections
import json
import matplotlib.pyplot as plt
import numpy as np

def gerar_grafico_artistas_mais_citados(arquivo_json):

  # Carregar dados do JSON
  with open(arquivo_json ) as f:
    dados = json.load(f)
    
    autores = []
    for index, i in dados.items():
        autores.append(i['artista'])

  contagem_artistas = collections.Counter(autores)
  
  artista = []
  citacoes = []
  for word, count in contagem_artistas.items():
      if count >= 2:
        artista.append(word)
        citacoes.append(count)
        # print(".....")
        # print(f"{word}: {count}")

  # Gerar gráfico de barras
  plt.figure(figsize=(10, 6))
  plt.bar(artista, citacoes, color='skyblue')
  plt.xlabel("Artista")
  plt.ylabel("Contagem")
  plt.title("Artistas Mais Citados")
  plt.xticks(rotation=45, ha='right')
  plt.tight_layout()

  plt.show() 

def gerar_grafico_duracao_media_por_musica(arquivo_json):

  # Carregar dados do JSON
  with open(arquivo_json, 'r') as f:
    dados = json.load(f)

 # Extrair dados e filtrar as musicas que nao consta tempo
  nome = []
  duracao = []
  nome_sem_tempo = []
  duracao_sem_tempo = []
  for index, i in dados.items():
    sem_duracao = i['duracao']
    if sem_duracao != "Nao consta tempo":
        nome.append(i['nome'])
        duracao.append(i['duracao'])
    else:
            nome_sem_tempo.append(i['nome'])
            duracao_sem_tempo.append(i['duracao']) 
        
   
  # ordenacao pela duracao da musica     
  dados = list(zip(nome, duracao))
  dados_ordenados = sorted(dados, key=lambda x: x[1])   
  nome_ordenado, duracao_ordenada = zip(*dados_ordenados)     

  # Gerar o gráfico
  plt.figure(figsize=(14, 8))
  plt.bar(nome_ordenado, duracao_ordenada, color='skyblue')
  plt.xlabel("Nome da Música")
  plt.xticks(rotation=30, ha='right', fontsize=8)
  plt.ylabel("Duração (em minutos)")
  plt.title("Duração das Músicas")
  plt.tight_layout()
  plt.show()
  
def gerar_grafico_generos_mais_citados(arquivo_json):

  # Carregar dados do JSON
  with open(arquivo_json ) as f:
    dados = json.load(f)
    
    generos = []
    for index, i in dados.items():
        generos.append(i['genero'])

  contagem_generos = collections.Counter(generos)
  
  generos1 = []
  citacoes = []
  for word, count in contagem_generos.items():
      nao_consta_genero = word
      if count >= 2 and nao_consta_genero !="Nao consta genero":
        generos1.append(word)
        citacoes.append(count)

  # Gerar gráfico
  plt.figure(figsize=(10, 6))
  plt.bar(generos1, citacoes, color='skyblue')
  plt.xlabel("Genero")
  plt.ylabel("Contagem")
  plt.title("Generos Mais Citados")
  plt.xticks(rotation=45, ha='right')
  plt.tight_layout()
  plt.show()   

# Gerando os graficos
arquivo_json = 'musicas.json' 
gerar_grafico_artistas_mais_citados(arquivo_json)
gerar_grafico_duracao_media_por_musica(arquivo_json)
gerar_grafico_generos_mais_citados(arquivo_json)

