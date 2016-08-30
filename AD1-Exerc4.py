import random
import math
#import sys -> Usar se rodar na versão menor que a 3.5

def verificaMaiorMenor(vector):
    vmin = int(math.inf) ### Maior número inteiro possivel, logo qualquer número é menor que ele; sys.maxsize -> Usar se rodar na versão menor que a 3.5
    vmax = int(-math.inf) ### Menor número inteiro possivel, logo qualquer número é maior que ele; -sys.maxsize -> Usar se rodar na versão menor que a 3.5

    max_repet = False ### Booleano para verificar a unicidade do Maior
    min_repet = False ### Booleano para verificar a unicidade do Menor

    if(len(vector) == 1): ### Se o vetor só tiver um elemento dentro, retornar esse elemento como maior e menor
        vmin = vector[0]
        vmax = vector[0]
        return (vmin, vmax)

    for num in vector: ### Varre o vetor comaparando os valores maiores e menores
        if(vmin > num):
            vmin = num
        elif(vmin == num): ### Se encontrar um valor repetido ao menor troca a variavel min_repet para verdadeiro
            min_repet = True

        if(vmax < num):
            vmax = num
        elif(vmax == num): ### Se encontrar um valor repetido ao maior troca a variavel max_repet para verdadeiro
            max_repet = True

    if(min_repet): ### Caso exista valor repetido vmin = None
        vmin = None
    if(max_repet): ### Caso exista valor repetido vmax = None
        vmax = None

    return (vmin, vmax)


vecInt = []

L = int (input("Informe o valor inteiro minimo da faixa: "))
H = int (input("Informe o valor inteiro maximo da faixa: "))
numElementos = int (input("Informe a quantidade de valores a serem sortiados: "))

for i in range(0, numElementos):
    vecInt.append(random.randint(L, H)) ### random.randint fornece pseudos-numeros aleatorios dentro de uma faixa de números

print (vecInt)
print (verificaMaiorMenor(vecInt))
