#Dicionarios e listas de Dados

escola = [
  {
    "nome": "Julia",
    "sobrenome": "Silva",
    "idade": 20,
    "curso": "Engenharia de Software",
    "status": True 
  },
  {
    "nome": "Pedro",
    "sobrenome": "Raphaele",
    "idade": 20,
    "curso": "Python",
    "status": True 
  },
  {
    "nome": "Rita",
    "sobrenome": "Sandra",
    "idade": 20,
    "curso": "Dados",
    "status": False 
  },
  {
    "nome": "Mia",
    "sobrenome": "Fernandes",
    "idade": 20,
    "curso": "C#",
    "status": True 
  }
]
print(escola)

for aluna in escola:
  print(aluna)

for aluna in escola:
  print(f"nome:{aluna['nome']}")
  print(f"curso:{aluna['curso']}")
  print("#" * 20)

for aluna in escola:
  if aluna["nome"] == "Rita":
    print(f"nome:{aluna['nome']}")
    print(f"curso:{aluna['curso']}")
    print("#" * 20) 



aluna = {
  "nome": "Julia",
  "sobrenome": "Silva",
  "idade": 20,
  "curso": "Engenharia de Software",
  "status": True
} 
print(aluna["nome"])
print(aluna["curso"])
print(aluna["status"])

aluna["sobrenome"] = "Santos"
aluna["cidade"] = "Belém"

print(aluna)

aluna.pop("idade")
print(aluna)