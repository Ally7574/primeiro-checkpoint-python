valorTotal = 0

print("Cliente comum | 1")
print("Cliente VIP | 2")
print("Cliente Premium | 3")
fidelidade = int(input("digite o tipo de fidelidade: "))

valorFinal = valorTotal

while True:
    produto = float(input("digite o preço do produto: "))

    if produto == 0:
        break

    valorTotal += produto


if fidelidade == 1:
    print("não recebe desconto nos produtos")
    valorFinal = valorTotal

elif fidelidade == 2 and valorTotal > 100:
    desconto = valorTotal * 0.05
    valorFinal = valorTotal - desconto
    print("desconto de 5%")
elif fidelidade == 2:
    valorFinal = valorTotal

elif fidelidade == 3 and valorTotal > 500:
    desconto = valorTotal * 0.15
    valorFinal = valorTotal - desconto
    print("desconto de 15%")
elif fidelidade == 3:
    valorFinal = valorTotal

if valorFinal < 200:
    frete = valorFinal + 25
    print(f"preço original da compra: {valorTotal}")
    print(f"preço da compra com desconto {valorFinal}")
    print(f"valor final com frete: {frete}")
elif valorFinal >= 200:
    print(f"preço original da compra: {valorTotal}")
    print(f"preço da compra com desconto {valorFinal}")
    print(f"Frete grátis")