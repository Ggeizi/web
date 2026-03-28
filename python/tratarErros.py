""" try:
  numero = int(input("Digite um número: "))
  resultado = 10 / numero
  
except ZeroDivisionError:
  print("Erro 404")
except ValueError:
  print("Digite somente numeros")
  
else:
  print(f"Resulatado é {resultado}") """


try:
  arquivo = open("dados.txt", mode = "r")
  conteudo = arquivo.read()

except FileNotFoundError:
  print("Arquivo não encontrado!\n")

finally:
  print("Operação finalizada!")