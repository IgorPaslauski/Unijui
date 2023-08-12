# itera i na sequencia de 0 a 4
for i in range(5):
    print(i)

print("------------------")

# itera i na sequencia de 1 a 5
for i in range(2, 5):
    print(i)

print("------------------")

# itera i na sequencia de 10 a 2, decrementando de 2 em 2
for i in range(10, 2, -2):
    print(i)

print("------------------")

# acessando os elementos de uma lista
lista = ["a", "b", "c", "d", "e"]
for i in range(len(lista)):
    print(lista[i])

print("------------------")

# iterando sobre os elementos de uma lista
for i in lista:
    print(i)

print("------------------")

lista = ["mercurio", "venus", "terra", "marte", "jupiter", "saturno", "urano", "netuno"]

# iterando e alterando os elementos de uma lista
for i in range(len(lista)):
    lista[i] = lista[i].capitalize()

print(lista)

# iterando e alterando os elementos de uma lista enumerable
for i, planeta in enumerate(lista):
    lista[i] = planeta.capitalize() + "-"

print(lista)

# iterando e alterando os elementos de uma lista forma errada
for i in lista:
    i = i + " planeta"

print(lista)

lista1 = ["pão", "queijo"]
lista2 = ["pão", "queijo", "maionese"]

lista3 = lista1 + lista2

print(lista3)

# concatena removendo os elementos duplicados
lista3 = list(set(lista3))

print(lista3)

# concatena e ordena
lista3 = sorted(lista3)

print(lista3)
print("------------------")

# exemplo while
i = 0
while i < 10:
    print(i)
    i += 1

print("------------------")

# exemplo while
i = 0
while True:
    print(i)
    i += 1
    if i == 10:
        break

print("------------------")

# exemplo while
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

print("------------------")

# funcoes
def calculaMedia(nota1, nota2):
    return (nota1 + nota2) / 2


print(calculaMedia(10, 8))

print("------------------")


# media 3 notas
def calculaMedia(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3


print(calculaMedia(7, 10, 4))

print("------------------")

#maior e menor
def maiorMenor(lista):
    maior = lista[0]
    menor = lista[0]
    for i in lista:
        if i > maior:
            maior = i
        if i < menor:
            menor = i
    return maior, menor, lista

print(maiorMenor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print("------------------")

#dicionario

dicionario = {"nome": "joao", "idade": 20, "cidade": "sao paulo"}

print(dicionario)

print(dicionario["nome"])

print(dicionario["idade"])

print(dicionario["cidade"])

print(dicionario.keys())

print(dicionario.values())

print(dicionario.items())

print("------------------")
