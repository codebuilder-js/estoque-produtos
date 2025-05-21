produtos = []

for i in range(3):
    nome = input("Produto: ")
    qtd = int(input("Quantidade atual: "))
    minimo = int(input("Estoque mínimo: "))

    produtos.append({"nome": nome, "qtd": qtd, "minimo": minimo})

print("\nVerificando necessidade de reposiçao:")

for produto in produtos:
    if produto["qtd"] < produto["minimo"]:
        print(f"{produto['nome']} - Estoque BAIXO: {produto['qtd']} unidades")

        for reposicao in range(produto["qtd"], produto["minimo"]):
            if reposicao - produto["qtd"] > 10:
                print("Reposição lenta... cancelando.")
                break
            else:
                print("Reposição completada.")
    else:
        print(f"{produto['nome']} - Estoque OK")
