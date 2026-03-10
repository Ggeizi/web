cursos = ["Python", "GIT", "Design Web", "Curriculo Lattes"]

print(cursos)

#printar posição especifica
print(cursos[1])

#modificar item da lista
cursos[1] = "GIT e GitHub"
print(cursos)

#adicionar item na lista
cursos.append("SQL")
print(cursos)

#remover item da lista
cursos.remove("Design Web")
cursos.pop(0)
print(cursos)

