login = input("digite o login: ")
senha = input("digite a senha: ")

if login == "walt" and senha == "disney":
    print("autenticado com sucesso")
elif login == "scott" and senha == "tiger":
    print("autenticado com sucesso")
elif login == "spock" and senha == "ncc1701":
    print("autenticado com sucesso")
else:
    print("usuário ou senha invalidos")