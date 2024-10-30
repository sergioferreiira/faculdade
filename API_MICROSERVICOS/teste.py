engine = create_engine('sqlite:///imoveis.db')

class Imovel:
    def __init__(self, id, logradouro, numero, cep):
        # ...

def converte_dict_para_imovel(linha):
    d = dict(linha)
    return Imovel(**d)
    # Você viu esta sintaxe ** em LP2, né?
    # Se você viu esta sintaxe, ela vai pegar o dicionário e transformá-lo
    # em uma lista de parâmetros. Se as chaves do dicionário forem as mesmas
    # que estão nos parâmetros do construtor, isso dará certo. Mas se forem
    # diferentes ou se houverem chaves a mais ou a menos, não vai dar certo.

def pesquisar(nome_rua):
    with engine.connect() as con:
        lista = []
        sql = ### lacuna1 ###
        rs = ### lacuna 2 ###
        ### lacuna 3 ###
        lista.append(converte_dict_para_imovel(linha))
    return lista


OBSERVAÇÃO IMPORTANTE: O banco de dados contém uma tabela 
"imoveis" com as colunas id, logradouro, numero, cep, cidade e estado.