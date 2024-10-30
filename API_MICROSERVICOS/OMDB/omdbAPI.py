import requests, pprint ,json

# film = input("type your name film \n")
# key = input("Type your api key \n")
# print(busca_nome(film, key)) 



def busca_id(film_id,api_Key):
  url = f"http://www.omdbapi.com/?i={film_id}&apikey={api_Key}"
  pedido = requests.get(url)
  dicionario_pedido = pedido.json()
  return dicionario_pedido

def busca_nome(film_name,api_Key):
  url = f"http://www.omdbapi.com/?s={film_name}&apikey={api_Key}"
  pedido = requests.get(url)
  dicionario_pedido = pedido.json()
  return print(f"O total de resultados para o filme {film_name} é {dicionario_pedido['totalResults']}")

def qnt_films(film_name,api_Key):
  url = f"http://www.omdbapi.com/?s={film_name}&type=movie&apikey={api_Key}"
  pedido = requests.get(url)
  dicionario_pedido = pedido.json()
  return print(f"O total de resultados para o filme {film_name} é {dicionario_pedido['totalResults']}")

def busca_qtd_jogos(film_name,api_Key):
    url = f"http://www.omdbapi.com/?s={film_name}&type=game&apikey={api_Key}"
    pedido = requests.get(url)
    transformarJson= pedido.json()
    return transformarJson['totalResults']

def nome_do_filme_por_id(film_name,api_Key):
    url = f"http://www.omdbapi.com/?s={film_name}&type=movie&apikey={api_Key}"
    pedido = requests.get(url)
    transformarJson = pedido.json()
    print(transformarJson['Search'][0]['imdbID'])
    x = 0
    for imdbID in transformarJson['Search']:
       print(f"nome: {transformarJson['Search'][x]['Title']} ano: {transformarJson['Search'][x]['Year']}, id do filme {transformarJson['Search'][x]['imdbID']}")
       x +=1

def ano_do_filme_por_id(id_filme,api_Key):
    url = f"http://www.omdbapi.com/?i={id_filme}&type=movie&apikey={api_Key}"
    pedido = requests.get(url)
    transformarJson = pedido.json()
    return transformarJson['Year']

def dicionario_do_filme_por_id(id_filme):
    url = f"http://www.omdbapi.com/?i={id_filme}&type=movie&apikey=333e85bd"
    pedido = requests.get(url)
    transformarJson = pedido.json()
    x = {
      'ano' : transformarJson['Year'],
      'nome': transformarJson['Title'],
      'diretor': transformarJson['Director'],
      'genero':transformarJson['Genre']
    }
    print(x)
    
dicionario_do_filme_por_id('tt0103776')