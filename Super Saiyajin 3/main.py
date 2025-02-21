print("Esta é uma hora decisiva para a humanidade! Rápido, ajude Goku a derrotar Majin Boo e salvar a Terra!")

vidaGoku: int = 3
vidaMajinBoo: int = 3
ataqueGoku: int = 2
ataqueMajinBoo: int = 9
ss3: int = 0
turno: int = 1
resposta: int
print(f"Vida de Goku: {vidaGoku}")
print(f"Vida de Majin Boo: {vidaMajinBoo}")

while True:
    print()
    print(f"Turno {turno}")
    print("O que Goku deve fazer?")
    print("1 - Atacar")
    print("2 - Carregar ki")
    print("3 - Transformar em Super Saiyajin 3")
    print("4 - Desistir")
    resposta = int(input())

    if resposta == 1:
        if ataqueGoku > ataqueMajinBoo:
            vidaMajinBoo -= 1
            print("Ataque bem sucedido!")
            print(f"Vida de Majin Boo: {vidaMajinBoo}")
        else:
            print("Ataque falhou!")
            vidaGoku -= 1
            print(f"Vida de Goku: {vidaGoku}")
            print(f"Vida de Majin Boo: {vidaMajinBoo}")

    elif resposta == 2:
        ataqueGoku += 2
        print("Ki carregado!")
        print(f"Novo ataque de Goku: {ataqueGoku}")
        print("Entretanto Majin boo aproveita para contra-atacar!")
        vidaGoku -= 1
        print(f"Vida de Goku: {vidaGoku}")
    elif resposta == 3:
        if (ss3 == 0):
            ss3 = 1
            ataqueGoku = ataqueGoku * 3
            print("Goku: E este é o Super Saiyajin 3!")
            print(f"Novo ataque de Goku: {ataqueGoku}")
            print("Majin Boo se aproveita da transformação para atacar!")
            vidaGoku -= 1
            print(f"Vida de Goku: {vidaGoku}")
        else:
            print("Goku: Eu já estou transformado!")
    elif resposta == 4:
        print("DERROTA!")
        break
    else:
        print("Comando inválido!")

    if vidaGoku == 0:
        print("DERROTA!")
        break

    if vidaMajinBoo == 0:
        print("VITÓRIA!")
        break

    turno += 1
