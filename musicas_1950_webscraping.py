import requests
from bs4 import BeautifulSoup
from codigo_html import pagina_html_musicas
import numpy as np # type: ignore


soup = BeautifulSoup(pagina_html_musicas, 'html.parser')

# encontra todas as tags <p>
all_paragraphs = soup.find_all('p')

# Filtra as tags para encontrar somente as musicas. Filtro: comecar com '19' or '20'
target_paragraphs = []
for paragraph in all_paragraphs:
  paragraph_text = paragraph.text.strip()
  if paragraph_text.startswith('19') or paragraph_text.startswith('20'):
    target_paragraphs.append(paragraph)

# Imprime e armazena somente a parte texto das musicas
musicas_somente_text = []
for paragraph in target_paragraphs:
    musicas_somente_text.append(paragraph.text)  
    #print(paragraph.text)
    
print("....")

#divide a informacao em colunas ano, titulo e autor
def divide_text(text):
    # Divide o texto pelo caractere "-"
    partes = text.split(" – ")

    # Extrai as informações das três colunas
    ano = partes[0]
    titulo = partes[1].split(" by ")[0]
    autor = partes[1].split(" by ")[1]

    return ano, titulo, autor

# Texto de exemplo
#texto = "1952 – Singin’ In The Rain by Gene Kelly"

# ano_musica = []
# titulo_musica = []
# autor_musica = []
# for musica in musicas_somente_text:
# # Chama a função para dividir o texto
#     ano, titulo, autor = divide_text(musica)
#     ano_musica.append(ano)
#     titulo_musica.append(titulo)
#     autor_musica.append(autor)
# # Imprime as informações
#     print(f"Ano: {ano}")
#     print(f"Título: {titulo}")
#     print(f"Autor: {autor}")

# Funcao pra criar o link das paginas Wikipedia
urls_wikipedia = []
ano_musica = []
titulo_musica = []
autor_musica = []
lista_musicas_1 = np.empty((0, 4), dtype=object)
for musica in musicas_somente_text:
# Chama a função para dividir o texto
    ano, titulo, autor = divide_text(musica)
    #formatacao do titulo da musica _
    titulo_formatado_espaco = titulo.replace(" ", "_")
    titulo_formatado = titulo_formatado_espaco.replace("’", "%27")
    url_wikipedia = f"https://en.wikipedia.org/wiki/{titulo_formatado}"
    urls_wikipedia.append(url_wikipedia)
    ano_musica.append(ano)
    titulo_musica.append(titulo)
    autor_musica.append(autor)
    #lista_musicas_1 = np.array([urls_wikipedia, ano_musica, titulo_musica, autor_musica])
    
lista_musicas_1 = []
lista_musicas_1 = list(zip(urls_wikipedia, ano_musica, titulo_musica, autor_musica))        

print("lista_musicas_1:")
print(lista_musicas_1[0])
print(lista_musicas_1[1])
print(lista_musicas_1[2])
print(lista_musicas_1[3])
print("....")  
    
# funcao para fazer a solicitacao http pro site wikipedia e colher mais informacao das musicas
# def fazer_requisicoes_http(urls_wikipedia): 

#   informacoes_urls = {}
#   print("Entrou aqui....")  
#   for url in urls_wikipedia:
#     try:
#       #print("Primeiro link do array....")
#       print(urls_wikipedia)
#       response = requests.get(urls_wikipedia)
#       #response = requests.get(url)
#       #informacoes_urls[url] = {
#       informacoes_urls[urls_wikipedia] = {
#         "status_code": response.status_code,
#         "texto_pagina": response.text,
#         # Adicione outras informações desejadas aqui
#       }
#     except requests.exceptions.RequestException as e:
#       informacoes_urls[url] = {
#         "status_code": "Erro",
#         "texto_pagina": f"Erro ao acessar a URL: {e}",
#       }
#   return informacoes_urls 

# Exemplo de uso
# urls_exemplo = ["https://www.example.com", "https://www.google.com", "https://www.youtube.com/"]
# informacoes_coletadas = fazer_requisicoes_http(urls_exemplo)
# print(informacoes_coletadas)

#----------Fazer a requisicao http e extrair o genero musical de cada musica--------------------------------------

def extrair_genero_musical(url, tag_alvo, classe_alvo, atributo_titulo):

  try:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Encontrar a tag com a classe e tag alvo especificadas
    tag_com_link = soup.find(tag_alvo, class_=classe_alvo)

    # Se a tag for encontrada
    if tag_com_link:
      # Encontrar o link dentro da tag
      link = tag_com_link.find("a")

      # Se o link for encontrado
      if link:
        # Extrair o texto do título do link do atributo especificado
        titulo_link = link.get(atributo_titulo)

        # Retornar o título do link
        return titulo_link
      else:
        texto_classe = classe_alvo.text.strip()
        return texto_classe
    else:
      return "Tag com classe e tag alvo não encontrada"

  except requests.exceptions.RequestException:
    return "Erro ao acessar a URL"
  
def extrair_tempo_musica(url, classe_alvo):
  try:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Encontrar a tag com a classe especificada
    tag_classe_alvo = soup.find("span", class_=classe_alvo)

    # Se a tag for encontrada
    if tag_classe_alvo:
      # Extrair o texto da tag
      texto_classe = tag_classe_alvo.text.strip()

      # Retornar o texto da classe
      return texto_classe
    else:
      return "Classe não encontrada"

  except requests.exceptions.RequestException:
    return "Erro ao acessar a URL"  
  
# Genero musical

# Duracao da musica

# Exemplo pra pegar o genero musical
url_exemplo = "https://en.wikipedia.org/wiki/As_It_Was"
tag_alvo = "td"
classe_alvo = "infobox-data category hlist"
atributo_titulo = "title"
titulo_link_encontrado = extrair_genero_musical(url_exemplo, tag_alvo, classe_alvo, atributo_titulo)
print("Print genero musical aqui....")  
print(titulo_link_encontrado) 

# Exemplo pra pegar o duracao da musica
url_exemplo = "https://en.wikipedia.org/wiki/Head_&_Heart"
classe_alvo = "duration"  # Substitua pelo nome real da classe
texto_tempo_musica = extrair_tempo_musica(url_exemplo, classe_alvo)
print(texto_tempo_musica)       

