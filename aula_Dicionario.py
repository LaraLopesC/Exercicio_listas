# O dicionário se difere da lista devido a presença de chaves na iniciação do código.
#01
'''
aluno={
    'nome': 'Lucas',
    'matricula': 123455,
    'turma':'le',
    'notas': [7.5,8,5]
}
#Ele pode adicionar automaticamente se trocar alguma informação
aluno['nome'] ='Tiago',
aluno['senha'] = 36985,
print(aluno)
print("nome:",aluno['nome'])
print("notas:",aluno['notas'])
'''
#Exercicios Listas
'''
#1
notas=[7.5, 8.0, 6.0, 9.5, 5.0]
notas.append (8.5)
notas.remove(5.0)
notas.insert(4,6.5)
notas.sort()
print("Tamanho",len(notas))
print("notas:",notas)
#Maior e menor nota
print("Maior nota:", max(notas))
print("Menor nota:", min(notas))
'''
'''
#2
nomes=["Lara", "Wallyson","Ana", "Hérica" , "Laisa"]
for nome in nomes:
    print(nome)
for i, nome in enumerate (nomes):
    print(f' Aluno{i}:{nome}')

#Exercício 3:

numeros = [3, 17, 8, 42, 5, 100, 23, 66, 11, 99]
numeros.sort() #Eu coloquei para uma melhor visualização.

lista=[]
for numero in numeros:
    if numero%2==0:
        lista.append(numero)
print(f' Números pares dessa lista: {lista}')

nova_lista=[]
for numero in numeros:
    if numero>20:
        nova_lista.append(numero)
print(f' Números maiores que 20 nessa lista: {nova_lista}')
        
total = sum(numeros)
print(f' Total da soma dos números contido na lista principal: {total}')
'''

#Exercício 4:
'''
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros[:4])
print(numeros[7:])
print(numeros[1:11:2])

print(num)
'''
#5
turma = [
    ['Ana', 8.5],
    ['Lara', 8.5],
    ['Beto', 7.0],
    ['Luisa', 6.9]
]

for aluno in turma:
    nome = aluno[0]
    nota = aluno[1]
    print(f"{nome} tirou {nota}")

for i, aluno in enumerate(turma):
    print(f"{i}: {aluno}")
