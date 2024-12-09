import random
playerin = True
dealerin = True

baralho = [2, 3, 4, 5, 6, 7, 8, 9, 10, 
           2, 3, 4, 5, 6, 7, 8, 9, 10,
           2, 3, 4, 5, 6, 7, 8, 9, 10,
           2, 3, 4, 5, 6, 7, 8, 9, 10,
           'A', 'K', 'J', 'Q', 
           'A', 'K', 'J', 'Q',
           'A', 'K', 'J', 'Q',
           'A', 'K', 'J', 'Q',       ] # baralho quadruplicado para representar os naipes

maodojogador = []
banca = []

def cartabanca(turn):
    carta = random.choice(baralho)
    turn.append(carta)
    baralho.remove(carta)


def total(turn):
    total = 0
    face = [ 'K', 'J', 'Q']
    for carta in turn:
        if carta in range(1, 11):
            total += carta
        elif carta in face:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total = 11
    return total

def revelarbanca():
    if len(banca) == 2:
        return banca[0]
    elif len(banca) > 2:
        return banca[0], banca[1]


for _ in range(2):
    cartabanca(banca)
    cartabanca(maodojogador)


while playerin or dealerin:
    print(f"Banca tem {revelarbanca()} e X")
    print(f"Você tem {maodojogador} e um total de {total(maodojogador)}")
    if playerin:
        stay0rHit = input("1:ficar\n2:comprar\n")
    if total(banca) > 16:
        dealerin = False
    else:
        cartabanca(banca)
    if stay0rHit == '1':
        playerin = False
    else:
        cartabanca(maodojogador)
    if total(maodojogador) >=21:
        break
    elif total(banca) >= 21:
        break

if total(maodojogador) == 21:
    print(f"\nVocê tem {maodojogador} para um total de 21 e a banca tem {banca} para um total de {total(banca)}")
    print("BlackJack! Você venceu")
elif total(banca) == 21:
        print(f"\nVocê tem {maodojogador} para um total de 21 e a banca tem {banca} para um total de {total(banca)}")
        print("BlackJack! A banca venceu")
elif total(maodojogador) > 21:
        print(f"\nVocê tem {maodojogador} para um total de 21 e a banca tem {banca} para um total de {total(banca)}")
        print("Você quebrou! a banca venceu")
elif total(banca) > 21:
        print(f"\nVocê tem {maodojogador} para um total de 21 e a banca tem {banca} para um total de {total(banca)}")
        print("A banca quebrou! Você venceu")
elif 21 - total(banca) > 21 - total(maodojogador):
        print(f"\nVocê tem {maodojogador} para um total de 21 e a banca tem {banca} para um total de {total(banca)}")
        print("Você venceu!")
elif 21 - total(banca) < 21 - total(maodojogador):
    print(f"\nVocê tem {maodojogador} para um total de 21 e a banca tem {banca} para um total de {total(banca)}")
    print("A banca venceu")

        