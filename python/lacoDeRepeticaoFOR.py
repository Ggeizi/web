indice = 0

for item in range(5):
  indice += item
  print("numero atual:", indice, "\n")
  
print("####################################################################################################")
contador = 0

while contador < 10:
  #contador += 1
  contador = contador + 1
  print(contador, "\n")

print("####################################################################################################")
tentativas = 8

while tentativas > 0:
  print("você ainda pode tentar ", tentativas, " vezes")
  tentativas -= 1
