
import os
arquivo = "alunas.txt"
alunas = []



############ CRIAÇÃO DE ARQUIVOS
arquivo = "alunas.txt"
with open(arquivo, mode ="w", encoding = "utf-8") as f:
  f.write("Ana\n")
  f.write("Geizi\n")
  f.write("Pedro\n")
  f.write("Ana Paula\n")

with open(arquivo, mode = "r", encoding = "utf-8") as j:
  conteudo = j.read()

print(conteudo)




############ ACESSANDO E LENDO OS ARQUIVOS
#with open(arquivo, mode = "r", encoding = "utf-8") as h:
 # for linha in h:
 #   print(linha.strip())
    
#with open(arquivo, mode = "r", encoding = "utf-8") as h:
  #linhas = h.readlines()
  #for linha in h.readlines():
    #alunas.append(linha.strip())

#print(alunas)




########### ATUALIZANDO ARQUIVOS
#with open(arquivo, mode = "r", encoding = "utf-8") as h:
  #alunas = h.readlines()

#alunas_atualizadas = []

#for aluna in alunas:
 # nome = aluna.strip()

  #if nome != "Pedro":
    #alunas_atualizadas.append(nome)

#with open(arquivo, mode = "w", encoding = "utf-8") as h:
  #for aluna in alunas_atualizadas:
  #  h.write(aluna + "\n")


#with open(arquivo, mode = "a", encoding = "utf-8") as h:
 # h.write("Dani\n")

#with open(arquivo, mode = "a", encoding = "utf-8") as h:
  #h.write("Rita\n")



############# DELETANDO ARQUIVOS
#if os.path.exists(arquivo):
  #os.remove(arquivo)
  #print("Arquivo removido com sucesso!")

#else:
  #("Arquivo não encontrado!")