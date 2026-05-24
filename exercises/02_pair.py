def count_char(frase : str):
    dict = {}

    for i in frase:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)


def ativo():
    usuarios = [
        {"nome":"Pedro","ativo": True},
        {"nome":"Lucas","ativo": False},
        {"nome":"Yago","ativo": True},
    ]

    usuarios_filtrados = []

    for i in usuarios:
        if i["ativo"] == True:
            usuarios_filtrados.append(i)
    

    print(usuarios_filtrados)


def more_expensive():
    produtos = [
        {"nome":"mouse","preco":50},
        {"nome":"teclado","preco":120},
        {"nome":"monitor","preco":500},
    ]
    maior_preco = 0
    maior = {}
    for i in produtos:
        if i["preco"] > maior_preco:
            maior_preco = i["preco"]
            
    for i in produtos:
        if i["preco"] == maior_preco : maior.update(i)

    print(maior)

if __name__ == "__main__":
    #count_char("programacao")
    #ativo()
    more_expensive()