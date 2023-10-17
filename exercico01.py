from random import randint

Q = []
for numero in range(20):
     Q.append(randint(1, 100))

maior = -1
menor = 101

for item_lista in Q:
     if maior < item_lista:
          maior = item_lista

     if menor > item_lista:
          menor = item_lista

print('lista de números:')
print(Q)
print(f'O maior valor é: {maior}')
print(f'O numero da lista menor é: {menor}')

#from random import randint

lista = []
resultado_soma = 0

for n in range(10):
     lista.append(randint(1, 30))

for i in lista:
     if (i % 2) == 0:
          resultado_soma = resultado_soma + i

print(f'O resultado da soma é: {resultado_soma}')
print(lista)