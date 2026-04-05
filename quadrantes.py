x = float(input("digite o numero na posição X: "))
y = float(input("digite o numero na posição Y: "))

if x == 0 and y == 0:
    print("posição em ponto de origem")
elif y == 0:
    print("posição no eixo X") 
elif x == 0:
    print("posição no eixo Y")

if x > 0 and y > 0:
    print("quadrante 1")
elif x < 0 and y > 0:
    print("quadrante 2")
elif x < 0 and y < 0:
    print("quadrante 3")
elif x > 0 and y < 0:
    print("quadrante 4")