m1 = int(input("digite o valor de consumo do mês passado: "))
m2 = int(input("digite o valor de consumo deste mês: "))

if m2 <= 20:
    valorDeConsumo = m2 * 2
if m2 > 20 and m2 <= 35:
    valorDeConsumo = m2 * 3.50
if m2 > 35 and m2 <= 50:
    valorDeConsumo = m2 * 5.50
if m2 > 50:
    valorDeConsumo = m2 * 7

if m1 < m2:
    multa = valorDeConsumo * 0.10
    valorTotal = valorDeConsumo + multa
    print(f"valor por consumo deste mês: {valorDeConsumo}")
    print(f"multa por ter gasto mais este mês: {multa}")
    print(f"valor final de sua conta: {valorTotal}")
else:
    desconto = valorDeConsumo * 0.15
    valorTotal = valorDeConsumo - desconto
    print(f"valor por consumo deste mês: {valorDeConsumo}")
    print(f"desconto por ter gasto menos do que o mês anterior: {desconto}")
    print(f"valor final da conta: {valorTotal}")
