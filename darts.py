import sys

# jatekosok
players = [501, 501]
rounds = -1
count180 = [0,0]
count140p = [0,0]
count100p = [0,0]


current_player = 0

while True:
    if current_player == 0:
        rounds += 1
    print("Pontszamok:")
    for i in range(0, len(players)):
        print(str(i + 1) + ". jatekos: " + str(players[i]))

    try:
        thrown = input("Mennyit dobott a(z) {} jatekos? ".format(current_player + 1))
        thrown = int(thrown)
    except:
        print("Kerem szamot adjon meg!")
        continue

    if thrown < 0 or thrown > 180:
        print("Hibas ertek! Adjon meg egy 0 es 180 kozotti szamot!")
        continue

    if players[current_player] - thrown < 0:
        print("Nem nyert, ez a jatekos tul sokat dobott.")
        continue

    if thrown == 180:
        count180[current_player] += 1
    elif thrown > 139:
        count140p[current_player] += 1
    elif thrown > 99:
        count100p[current_player] += 1

    if players[current_player] - thrown == 0:
        last_round_darts = None
        while last_round_darts is None:
            try:
                last_round_darts = int(input("Hany nyillal dobta meg a kiszallot? "))
                if last_round_darts > 3 or last_round_darts < 1:
                    last_round_darts = None
                    print("1 es 3 kozotti szamot adjon meg")
            except:
                print("Kerem szamot adjon meg!")

        print(str(current_player + 1) + " szamu jatekos nyert " + str(rounds * 3 + last_round_darts) + " dobasbol!")
        print("A dobasonkenti atlag az {}.".format(1503 / (rounds * 3 + last_round_darts)))
        for i in range(0,2):
            print("{}. jatekos 180-as dobasok szama: {}".format(i+1, count180[i]))
            print("{}. jatekos 140+ dobasok szama: {}".format(i+1, count140p[i]))
            print("{}. jatekos 100+ dobasok szama: {}".format(i+1, count100p[i]))
        break

    players[current_player] = players[current_player] - thrown

    current_player = (current_player + 1) % len(players)