dic = {
    "linguagens" : [
        {"nome": "javaScript", "criacao" : 1980 ,
         "paradigma" : ["eventos", "funcional"]},
         {"nome": "python", "criacao" : 1678 ,
         "paradigma" : ["orientada a objetos", "estruturada"]},
         {"nome": "haskell", "criacao" : 1990 ,
         "paradigma" : ["funcional"]}
    ]
}

def maisVelha (dicionario):
    lista_linguagem = dic["linguagens"]
    x = 0
    for key in lista_linguagem:
        if x == 0:
            x = key["criacao"]
        elif key["criacao"] < x:
            x = key["criacao"]
    return x

print(maisVelha(dic))

def noRepeatLanguages (dicionario):
    lista_linguagem = dic["linguagens"]
    nlist = []
    for paradigmas in lista_linguagem:
        for x in paradigmas["paradigma"]:
            if x not in nlist:
                nlist.append(x)
    return nlist


print(noRepeatLanguages(dic))