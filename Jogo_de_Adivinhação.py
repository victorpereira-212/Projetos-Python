import random

numero = random.randint(1, 100)
acertou = False
contador = 0

print('*--------Jogo de Adivinhação--------*')
print('Eu estou pensando em um número entre 1 e 100, tente adivinhar e eu direi se é maior ou menor.')
while acertou == False:
        tentativa = int(input(f'Digite um número!\n'))
        contador += 1
        if tentativa == numero:
             print('*--------Parabéns, você acertou!--------*')
             print(f'*----Foram necessárias {contador} tentativas-----*')
             acertou = True
        else:
            if tentativa > numero:
                print('O número que estou pensando é menor')
            else:
                print('O número que estou pensando é maior')
