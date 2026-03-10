nome = input("Digite seu nome: ")
estado = input("Digite seu estado: ")

def saudacao(nome, estado):
    print(f"Olá {nome}, seja bem-vindo! Muito legal ver alguém do {estado}\n")

saudacao(nome, estado)


a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
def soma(a, b):
    return a + b

# def potencia(a, b):
#    return a ** b

resultado = soma(a, b)
print(f"O resultado da soma de {a} com {b} é de: {resultado}")

#resultado = potencia(a, b)
#print(f"O resultado da potência de {a} com {b} é de: {resultado}")