peso = float(input("digite seu peso em quilograma: "))
altura = float(input("digite sua altura em metros: "))

imc = peso / altura ** 2

if imc < 18.5:
    print(f"seu IMC ({imc}) | Abaixo Do Peso")
elif imc >= 18.5 and imc < 24.9:
    print(f"seu IMC ({imc}) | Peso normal")
elif imc >= 25 and imc < 29.9:
    print(f"seu IMC ({imc}) | Sobrepeso")
else:
    print(f"seu IMC ({imc}) | Obesidade")