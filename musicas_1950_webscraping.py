import requests
from bs4 import BeautifulSoup
from codigo_html import pagina_html_musicas
import json
import numpy as np # type: ignore


soup = BeautifulSoup(pagina_html_musicas, 'html.parser')

# encontra todas as tags <p>
all_paragraphs = soup.find_all('p')

# Filtra as tags para encontrar somente as musicas
# Filtro: comecar com '19' or '20'
target_paragraphs = []
for paragraph in all_paragraphs:
  paragraph_text = paragraph.text.strip()
  if paragraph_text.startswith('19') or paragraph_text.startswith('20'):
    target_paragraphs.append(paragraph)

# Armazena somente a parte texto das musicas
musicas_somente_text = []
for paragraph in target_paragraphs:
    musicas_somente_text.append(paragraph.text)  
print("....")

#divide a informacao nas colunas ano, titulo e autor
def divide_text(text):
    partes = text.split(" – ")
    ano = partes[0]
    titulo = partes[1].split(" by ")[0]
    autor = partes[1].split(" by ")[1]
    return ano, titulo, autor

# Funcao pra criar o link das paginas Wikipedia
urls_wikipedia = []
ano_musica = []
titulo_musica = []
autor_musica = []
for musica in musicas_somente_text:
    ano, titulo, autor = divide_text(musica)
    titulo_formatado_espaco = titulo.replace(" ", "_")
    titulo_formatado = titulo_formatado_espaco.replace("’", "%27")
    url_wikipedia = f"https://en.wikipedia.org/wiki/{titulo_formatado}"
    urls_wikipedia.append(url_wikipedia)
    ano_musica.append(ano)
    titulo_musica.append(titulo)
    autor_musica.append(autor)

# Primeira lista de musicas    
lista_musicas_1 = []
lista_musicas_1 = list(zip(urls_wikipedia, ano_musica, titulo_musica, autor_musica))        
print("....")  

# Funcao para fazer a requisicao http e extrair o genero
def extrair_genero_musical(url, tag_alvo, classe_alvo, atributo_titulo):

  try:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    tag_com_link = soup.find(tag_alvo, class_=classe_alvo)

    if tag_com_link:
      link = tag_com_link.find("a")
      if link:
        titulo_link = link.get(atributo_titulo)

        return titulo_link
      else:
        texto_classe = classe_alvo.text.strip()
        return texto_classe
    else:
      texto_classe = "Nao consta genero"
      return texto_classe

  except requests.exceptions.RequestException:
    return "Erro ao acessar a URL"

# Funcao para fazer a requisicao http e extrair a duracao de cada musica  
def extrair_tempo_musica(url, classe_alvo):
  try:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    tag_classe_alvo = soup.find("span", class_=classe_alvo)

    if tag_classe_alvo:
      texto_classe = tag_classe_alvo.text.strip()
      return texto_classe
    else:
      texto_classe = "Nao consta tempo"
      return texto_classe

  except requests.exceptions.RequestException:
    return "Erro ao acessar a URL"  
  
# Colher o Genero musical e a Duracao da musica
genero_musical = []
duracao_musica = []
for url in urls_wikipedia:
    # extrai o genero musical
    tag_alvo = "td"
    classe_alvo = "infobox-data category hlist"
    atributo_titulo = "title"
    genero_musical_texto = extrair_genero_musical(url, tag_alvo, classe_alvo, atributo_titulo)
    genero_musical.append(genero_musical_texto)
    # extrai a duracao da musica
    classe_alvo = "duration"
    texto_tempo_musica = extrair_tempo_musica(url, classe_alvo)
    duracao_musica.append(texto_tempo_musica)
print("....")

# Listas de musicas finais (juncao dos arrays)
lista_musicas_final = []
lista_musicas_final = list(zip(urls_wikipedia, ano_musica, titulo_musica, autor_musica, duracao_musica, genero_musical))
print("....")

# Funcao pra criar o arquivo json
def criar_arquivo_json_musicas(lista_musicas_final, nome_arquivo):
  
  dados_musicas = {}
  for musica in lista_musicas_final:
    url = musica[0]
    ano = musica[1]
    nome = musica[2]
    artista = musica[3]
    duracao = musica[4]
    genero = musica[5]

    dados_musica = {
      "url": url,
      "ano": ano,
      "nome": nome,
      "artista": artista,
      "duracao": duracao,
      "genero": genero
    }

    dados_musicas[nome] = dados_musica

  # Converte o dicionário em uma string JSON
  dados_json = json.dumps(dados_musicas, indent=4)

  # Abre e popula o arquivo JSON
  with open(nome_arquivo, 'w') as arquivo:
    arquivo.write(dados_json)

nome_arquivo = "musicas.json"

criar_arquivo_json_musicas(lista_musicas_final, nome_arquivo)