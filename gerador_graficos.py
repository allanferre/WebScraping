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

  # Inicializar dicionário para armazenar durações médias
  duracao_media_por_musica = defaultdict(list)

  # Extrair dados e calcular durações médias
  for musica in dados:
    nome_musica = musica['nome']
    duracao = musica['duracao']  # Assumindo que 'duracao' é um valor numérico
    duracao_media_por_musica[nome_musica].append(duracao)

  # Calcular durações médias
  duracoes_medias = {nome_musica: sum(duracoes) / len(duracoes) for nome_musica, duracoes in duracao_media_por_musica.items()}

  # Gerar gráfico de barras tipo "dot bar"
  plt.figure(figsize=(12, 8))
  plt.bar(duracoes_medias.keys(), duracoes_medias.values(), color='skyblue', alpha=0.7)
  plt.xlabel("Nome da Música")
  plt.xticks(rotation=45, ha='right', fontsize=8, tight_layout=True)
  plt.ylabel("Duração Média (em minutos)")
  plt.title("Duração Média das Músicas")
  plt.tight_layout()

  # Exibir o gráfico no VS Code
  plt.show()
         
          



# Artistas mais citados
arquivo_json = 'musicas.json'  # Substitua pelo caminho real do seu arquivo
gerar_grafico_artistas_mais_citados(arquivo_json)

