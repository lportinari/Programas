import random

print('-=' * 11)
print('SIMULADOR DA MEGASENA')
print('-=' * 11)
print()
print('''Este programa irá fazer uma simulação de um sorteio da megasena.
O programa só irá parar quando o usuário acertar os 6 números sorteados.
No final mostraremos quantos jogos foram necessários para acertar os 6 números e
calcularemos quanto foi gasto, levando em conta que cada jogo custa R$3.50.

''')

mega = list(range(1, 61))
my_game = []
cont = 0
for n in range(1, 7):
    while True:
        choice = int(input(f'Escolha {n}. Digite um número entre 1 e 60: '))
        if choice < 1 or choice > 61:
            print('ERRO! Digite um número entre 1 e 60.')
        else:
            my_game.append(choice)
            break
my_game.sort()

print('Este processo pode demorar, dependendo da sua "sorte".')

while True:
    sorteio = []
    copia_mega = mega.copy()
    cont += 1
    
    for j in range(6):
        n_sorteado = random.choice(copia_mega)
        sorteio.append(n_sorteado)
        copia_mega.remove(n_sorteado)

    sorteio.sort()
    if sorteio == my_game:
        break

debito = cont * 3.5

print(f'Parabéns! Você venceu na {cont} tentativa!')
print(f'Você gastou R${debito}.')

input()

        
        
    
