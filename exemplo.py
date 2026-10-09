produto = "Mouse gamer wifi"
valores = [20,71,100,30]

if produto == "mouse":
    if "mouse".lower() in produto.lower():
        print("produto encontrado")
    else:
        print("Produto nao encontrado")

def dobrar (valor):
    resultado = valor * 2
    return resultado

valores_novos = []
for valor in valores:
    valores_novos.append (dobrar(valor))

print(valores_novos)

alunos = ["Ana", "hugo", "Mariana", "Pedro", "Ana Paula"]

aluno_procurado = input("Digite um nome: ")

alunos_encontrados = []

for alunos.lower() in alunos.lower():
    alunos_encontrados.append(alunos)

print(alunos_encontrados)