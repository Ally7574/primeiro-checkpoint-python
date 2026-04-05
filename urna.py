ca = 0
cb = 0
nulo = 0
branco = 0

print("Candidato A: 1")
print("Candidato B: 2")
print("Voto Nulo: 3")
print("Voto em Branco: 4")

while True:
    voto = int(input("digite uma das opções a cima para votar (digite 0 para finalizar)"))
    if voto == 1:
        ca = ca + 1
        print("voto no candidato A")
    elif voto == 2:
        cb = cb + 1
        print("voto no candidato B")
    elif voto == 3:
        nulo = nulo + 1
        print("Voto nulo")
    elif voto == 4:
        branco = branco + 1
        print("voto em branco")
    elif voto == 0:
        break
    else:
        print("voto invalido")

print(f"Candidato A: {ca}")
print(f"Candidato B: {cb}")
print(f"voto nulo: {nulo}")
print(f"voto em branco: {branco}")
