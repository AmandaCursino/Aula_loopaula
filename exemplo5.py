#armazena um numero pequeno
maior_numero = -99999999

#entra com o primeiro numero
number = int(input('Entre com um numero ou digite -1 para parar: '))

#Se o numero nao for igual a -1 continua
while number != -1:
    #o numero é maior que o maior_numero
    if number > maior_numero:
    #sim, atualiza maior_numero
        maior_numero = number
    #entre com o proximo numero
    number = int(input('Entre com um numero ou digite -1 para para: '))
    
#Imprime o maior numero
print('O maior numero é', maior_numero)
