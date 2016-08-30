def verificaPalindrome(frase):
    removeWhiteSpaces = [] ### Array util para remover os espaços em brancos
    removeHypen = [] ### Array util para remover os hifen

    palindromo = str(frase).lower().strip() ### Remove os espaços em brancos no inicio e final e coloca toda a palavra em letra minuscula

    if (len(palindromo) == 1): ### Se o tamanho da palavra for 1, entao ele deve retornar verdadeiro
        return True

    ### BEGIN - Remover os espaços em branco no meio da frase - BEGIN ###
    removeWhiteSpaces = palindromo.split(' ')
    palindromo = str()
    for word in removeWhiteSpaces:
        palindromo = palindromo + word
    ### END - Remover os espaços em branco no meio da frase - END ###


    ### BEGIN - Remover hypen no meio da frase - BEGIN ###
    removeHypen = palindromo.split('-')
    palindromo = str()
    for word in removeHypen:
        palindromo = palindromo + word
    ### END - Remover hypen no meio da frase - END ###

    if(palindromo[0] == palindromo[-1]): ### Verifica se a primeira e ultima letra sao iguais
        return verificaPalindrome(palindromo[1:-1]) ### Remove a 1ª[1] e ultima[-1] letra da palavra

    return False

f = open('file.txt', 'r') ### abertura do arquivo genérico de entrada, substituia file.txt pelo nome de arquivo que quiser.

for line in f: ### le as linhas no arquivo genérico de entrada
    if (line == "fim"): ### Verifica se a linha esta escrito fim
        break ### termina o looping de leitura de linha
    elif(verificaPalindrome(line)):
        print("E palindromo")
    else:
        print("Nao e palindromo")

f.close() ### fecha o arquivo génerico de entrada

###### Lendo até o usuário escrever fim ######

while (True):
    frase = input() ### Pega o input do usuario
    if(frase == "fim"): ### Sai do loop se digitar fim
        break
    elif(verificaPalindrome(frase)):
        print("E palindromo")
    else:
        print("Nao e palindromo")
