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
        print(".....")
        print(f"{word}: {count}")
  

  
#   rotulos = list(contagem_artistas.keys())
#   valores = list(contagem_artistas.values())
#   print(".....")
#   print(f"{artista}: {citacoes}")

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

 # Extrair dados
#   nomes_musicas = [musica['nome'] for musica in dados]
#   duracoes_musicas = [musica['duracao'] for musica in dados]  # Assumindo 'duracao' como valor numérico
  
  nome = []
  duracao = []
  for index, i in dados.items():
        nome.append(i['nome'])
        duracao.append(i['duracao'])

  # Gerar gráfico de barras tipo "dot bar"
  plt.figure(figsize=(14, 8))
  plt.bar(nome, duracao, color='skyblue', alpha=0.7)
  plt.xlabel("Nome da Música")
  plt.xticks(rotation=30, ha='right', fontsize=8)
  plt.ylabel("Duração (em minutos)")
  plt.title("Nome e Duração das Músicas")
  plt.tight_layout()

  # Exibir o gráfico no VS Code
  plt.show()

         
          



# Artistas mais citados
arquivo_json = 'musicas.json'  # Substitua pelo caminho real do seu arquivo
gerar_grafico_duracao_media_por_musica(arquivo_json)

