arquivo = "alunas.txt"
alunas = []

#with open(arquivo, mode ="w", encoding = "utf-8") as f:
  #f.write("Ana\n")
  #f.write("Geizi\n")
  #f.write("Pedro\n")
  #f.write("Ana Paula\n")

#with open(arquivo, mode = "r", encoding = "utf-8") as j:
  #conteudo = j.read()

#print(conteudo)


with open(arquivo, mode = "r", encoding = "utf-8") as h:
  for linha in h:
    print(linha.strip())
    
with open(arquivo, mode = "r", encoding = "utf-8") as h:
  #linhas = h.readlines()
  for linha in h.readlines():
    alunas.append(linha.strip())

print(alunas)