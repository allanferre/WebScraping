import json

def corrigir_apostrofo(dados_json):

  if isinstance(dados_json, dict):
    for chave, valor in dados_json.items():
      if isinstance(valor, str) and "\u2019" in valor:
        dados_json[chave] = valor.replace(u"\u2019", "’")
      corrigir_apostrofo(valor)  # Recursivamente corrigir em valores aninhados
  elif isinstance(dados_json, list):
    for item in dados_json:
      corrigir_apostrofo(item)  # Recursivamente corrigir em cada item da lista

  return dados_json

# Carregue o JSON
with open('musicas.json') as f:
  dados_json = json.load(f)

# Corrija os apóstrofos
dados_json_corrigido = corrigir_apostrofo(dados_json)

# Salve o JSON corrigido (opcional)
with open('arquivo_corrigido.json', 'w') as f:
  json.dump(dados_json_corrigido, f, indent=4)
