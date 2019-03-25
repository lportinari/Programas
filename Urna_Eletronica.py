from time import sleep
import random


def menu1():
    """
    Responsável por criar o primeiro menu.
    O usuário deverá escolher a opção de votação ou o acesso restrito
    """
    print('-=' * 30)
    while True:
        escolha = int(input('''Digite 1 para votar ou 2 para entrar no modo administrador:

[ 1 ] - Votar
[ 2 ] - Acesso restrito

Digite sua opção: '''))
        if escolha == 2 or escolha == 1:
            break
        print('Opção invalida.')
    if escolha == 1:
        menu2()
    else:
        menu3()


def menu2():
    global haddad, bolsonaro, branco
    print('-=' * 20)
    print('''Favor, digitar o número do candidato ou uma das opções abaixo:

[ 1 ] VOTAR EM BRANCO
[ 2 ] MOSTRAR CANDIDATOS
''')
    while True:
        voto = int(input('Número do candidato: '))
        if voto == 1 or voto == 2 or voto == 13 or voto == 17:
            break
        print('ERRO! Digite uma opção valida')

    if voto == 1:
        while True:
            confirm = str(input('Tem certeza que deseja declarar seu voto em BRANCO? [S/N]: ')).upper().strip()[0]
            if confirm in 'S':
                branco += 1
                break
            elif confirm in 'N':
                menu2()
                break
            print('ERRO! Digite S para SIM ou N para NÃO!')

    elif voto == 2:
        mostraCandidatos()

    elif voto == 13:
        while True:
            confirm = \
            str(input('Tem certeza que deseja declarar seu voto para FERNANDO HADADD? [S/N]: ')).upper().strip()[0]
            if confirm in 'S':
                haddad += 1
                break
            elif confirm in 'N':
                menu2()
                break
            print('ERRO! Digite S para SIM ou N para NÃO!')

    elif voto == 17:
        while True:
            confirm = \
            str(input('Tem certeza que deseja declarar seu voto para JAIR BOLSONARO? [S/N]: ')).upper().strip()[0]
            if confirm in 'S':
                bolsonaro += 1
                break
            elif confirm in 'N':
                menu2()
                break
            print('ERRO! Digite S para SIM ou N para NÃO!')


def menu3():
    password = ''
    print('-=' * 20)
    print('Bem vindo ao modo administrador.')

    while password != 'swordfish':
        password = input('Digite a sua senha: ').lower()
        if password != 'swordfish':
            print('Senha incorreta! Digite uma senha valida.')
            back = str(input('Deseja voltar para o menu anterior? [S/N]: ')).upper()[0]


    print('''Acesso concedido!

Aguarde enquanto computamos os votos da urna.
    ''')
    print('Buscando informações...')

    sleep(1.7)

    print('-=' * 20)
    print('Votos em branco:', branco)
    print('Votos de Fernando Haddad:', haddad)
    print('Votos de Jair Bolsonaro:', bolsonaro)
    print()
    if haddad > bolsonaro:
        print('Fernando Hadadd lidera nas votações.')
    elif bolsonaro > haddad:
        print('Jair Bolsonaro lidera nas votações.')
    else:
        print('Empate técnico.')


    print('-=' * 20)
    print('''Escolha uma opção:
[ 1 ] - Modo simulação
[ 2 ] - Voltar ao menu anterior''')

    back = int(input('Escolha uma opção: '))
    if back == 1:
        simulator(candidatos)
    elif back == 2:
        menu2()


def mostraCandidatos():
    global candidatos
    print('-' * 20)
    for i in candidatos:
        print(i)
    print('-' * 20)
    menu2()
    

def simulator(candidatos):
    global bolsonaro, haddad
    
    for i in range(1000):
        choice = random.choice(candidatos)
        
        if choice == candidatos[0]:
            haddad += 1
            
        elif choice == candidatos[1]:
            bolsonaro += 1
        


# Programa principal
haddad = bolsonaro = branco = 0
candidatos = ['Fernando Haddad - 13', 'Jair Bolsonaro - 17']
simulador = list()

print('-=' * 7)
print('ELEIÇÕES 2018')
print('-=' * 7)
print()

print('''Bem vindo ao simulador de urna eletrônica.
Nossos candidatos e números para votação serão:

[ 13 ] Fernando Haddad
[ 17 ] Jair Bolsonaro

Tendo a lista de candidatos, continuaremos com o simulador.
''')

# Chamada da função menu1
menu1()

while True:
    loop = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if loop in 'S':
        menu1()
    elif loop in 'N':
        break

print('Obrigado! Encerrando...')
sleep(1)

