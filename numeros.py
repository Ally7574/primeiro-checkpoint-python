quantidade = int(input("digite a quantidade de numeros na sequencia que deseja: "))

pares = 0
impares = 0

for i in range(quantidade):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("Par")
        pares += 1
    else:
        print("Ímpar")
        impares += 1




print("Total de pares:", pares)
print("Total de ímpares:", impares)
