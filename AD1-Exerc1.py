def convert(numDecimal, base):
    numConvertido = "" ### Número final que retornará, inicializado como string para concatenar os restos da divisões
    numInvertido = [] ### Array feito para armazenar de forma invertida os restos da divisão

    if(numDecimal < base): ### Caso o numero seja menor que a propria base é só retornar o próprio número
        return numDecimal

    while (numDecimal > 0): ### Vamos fazendo multiplas divisões até o nosso número seja igual a zero
        numQuociente = numDecimal//base ### Divisão onde só pegamos a parte inteira, ou seja, o numero antes da virgula 3 / 2 = 1.5 -> retorna apenas o 1
        numResto = numDecimal%base ### Divisão modular, retorna o resto da divisão
        numInvertido.append(numResto) ### Adiciona no Array o resto da divisão
        numDecimal = numQuociente ### o Nosso novo numero para divisão se torna o quociente da antiga divisão

    for num in reversed(numInvertido): ### Inverte o Array para sair o número de forma correta
        numConvertido = numConvertido + str(num) ### Concatenação para formar o número na base desejada

    int (numConvertido) ### Faz retornar um numero inteiro (type-cast)

    return numConvertido

###### Lendo de um arquivo genérico ######

f = open('file.txt', 'r') ### abertura do arquivo genérico de entrada, substituia file.txt pelo nome de arquivo que quiser.

for line in f: ### le as linhas no arquivo genérico de entrada
    num = int(line.rstrip('\n')) ### retira a quebra de linha e converta de str para int
    if (num == -1): ### Verifica se o número é -1
        break; ### termina o looping de leitura de linha
    else:
        for i in range(2, 10): ### se não for -1, imprime todos os valores nas bases de 2 a 9
            if(i == 9): ### Verifica se é a ultima base para pode colocar a quebra de linha corretamente
                print(convert(num, i))
            else:
                print(convert(num, i), end=' ') ### coloca as saidas das bases lado a lado.

f.close() ### fecha o arquivo génerico de entrada

###### Lendo até o usuário colocar -1 ######

while (True):
    num = int(input('Entre com o número: ')) ### Input com um texto para melhor indicar o que deve ser feito. (Mas acho que no exercicio tem apagar o "Entre com o numero: ") 
    if(num == -1): ### Sai do loop se digitar -1
        break
    for i in range(2, 10): ### se não for -1, imprime todos os valores nas bases de 2 a 9
        if(i == 9): ### Verifica se é a ultima base para pode colocar a quebra de linha corretamente
            print(convert(num, i))
        else:
            print(convert(num, i), end=' ') ### coloca as saidas das bases lado a lado.
