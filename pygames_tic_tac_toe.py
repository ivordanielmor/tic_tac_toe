# 1. Pygame ablak nyitása, rács kirajzolása
# Elindítjuk a Pygame-et, létrehozunk egy 600x600-as ablakot, és berajzoljuk a 3x3 rácsot.

# import pygame

# pygame.init()

# M = 200
# ablak = pygame.display.set_mode((3*M, 3*M)) # függvény megnyit egy ablakot, amelybe rajzolhatsz
# pygame.display.set_caption("Tic Tac Toe") # ez a sor az ablak címsorában megjelenő szöveget állítja be

# FEHER = (255, 255, 255)
# FEKETE = (0, 0, 0)

# ablak.fill(FEHER)

# for i in range(1, 3):
#     pygame.draw.line(ablak, FEKETE, (i*M, 0), (i*M, 3*M), 5)  # függőleges
#     pygame.draw.line(ablak, FEKETE, (0, i*M), (3*M, i*M), 5)  # vízszintes

# pygame.display.flip() # a képernyő tartalmát frissíti

# fut = True
# while fut:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             fut = False

# pygame.quit()

# 2. Tábla tárolása, X/O rajzolása
# Egy 3x3-as listában (tabla), minden elem “X”, “O” vagy üres (“ ”). A rajzol_tabla függvény
# a mezőkbe helyezi az X/O-t.

# import pygame

# pygame.init()

# M = 200
# ablak = pygame.display.set_mode((3*M, 3*M))
# pygame.display.set_caption("Tic Tac Toe")

# FEHER = (255, 255, 255)
# FEKETE = (0, 0, 0)

# tabla = [
#     ["X", "O", "X"],
#     [" ", "X", "O"],
#     ["O", " ", " "]
# ]

# betu = pygame.font.SysFont(None, 120)  # Alapértelmezett betűtípus, 120-as méret

# def rajzol_tabla():
#     for sor in range(3):
#         for oszlop in range(3):
#             mezo = tabla[sor][oszlop]
#             if mezo != " ":
#                 szoveg = betu.render(mezo, True, FEKETE) # Ez létrehoz egy új képet (egy Surface objektumot), amin a "mezo" karakter (pl. "X" vagy "O") van kirajzolva szövegként a megadott színnel
#                 x = oszlop * M + M // 2 - szoveg.get_width() // 2 # Ez számítja ki a szöveg vízszintes pozícióját (azaz az X koordinátát)
#                 y = sor * M + M // 2 - szoveg.get_height() // 2 # Ez ugyanazt csinálja függőlegesen
#                 ablak.blit(szoveg, (x, y)) # kirajzolja a szöveget az ablakra a kiszámított (x, y) pozícióba

# ablak.fill(FEHER)
# for i in range(1, 3):
#     pygame.draw.line(ablak, FEKETE, (i*M, 0), (i*M, 3*M), 5)  # függőleges
#     pygame.draw.line(ablak, FEKETE, (0, i*M), (3*M, i*M), 5)  # vízszintes

# rajzol_tabla()
# pygame.display.flip()

# fut = True
# while fut:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             fut = False

# pygame.quit()

# 3. Egérkattintásból sor/oszlop meghatározása
# A kattintás pixel-koordinátájából kiszámoljuk, melyik sor/oszlop. Ha az egér 330, 420-ra
# kattint: oszlop = 330//200 = 1, sor = 420//200 = 2.

# import pygame

# pygame.init()

# M = 200
# ablak = pygame.display.set_mode((3*M, 3*M)) # függvény megnyit egy ablakot, amelybe rajzolhatsz
# pygame.display.set_caption("Tic Tac Toe") # ez a sor az ablak címsorában megjelenő szöveget állítja be

# FEHER = (255, 255, 255)
# FEKETE = (0, 0, 0)

# tabla = [
#     [" ", " ", " "],
#     [" ", " ", " "],
#     [" ", " ", " "]
# ]

# betu = pygame.font.SysFont(None, 120)  # Alapértelmezett betűtípus, 120-as méret

# def rajzol_tabla():
#     for sor in range(3):
#         for oszlop in range(3):
#             mezo = tabla[sor][oszlop]
#             if mezo != " ":
#                 szoveg = betu.render(mezo, True, FEKETE) # Ez létrehoz egy új képet (egy Surface objektumot), amin a "mezo" karakter (pl. "X" vagy "O") van kirajzolva szövegként a megadott színnel
#                 x = oszlop * M + M // 2 - szoveg.get_width() // 2 # Ez számítja ki a szöveg vízszintes pozícióját (azaz az X koordinátát)
#                 y = sor * M + M // 2 - szoveg.get_height() // 2 # Ez ugyanazt csinálja függőlegesen
#                 ablak.blit(szoveg, (x, y)) # kirajzolja a szöveget az ablakra a kiszámított (x, y) pozícióba

# ablak.fill(FEHER)
# for i in range(1, 3):
#     pygame.draw.line(ablak, FEKETE, (i*M, 0), (i*M, 3*M), 5)  # függőleges
#     pygame.draw.line(ablak, FEKETE, (0, i*M), (3*M, i*M), 5)  # vízszintes

# rajzol_tabla()
# pygame.display.flip()

# jelenlegi_jatekos = "X"

# fut = True
# while fut:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             fut = False

#         if event.type == pygame.MOUSEBUTTONDOWN:
#             x, y = pygame.mouse.get_pos()
#             sor = y // M
#             oszlop = x // M

#             if tabla[sor][oszlop] == " ":
#                 tabla[sor][oszlop] = jelenlegi_jatekos
#                 jelenlegi_jatekos = "O" if jelenlegi_jatekos == "X" else "X"

#                 ablak.fill(FEHER)
#                 for i in range(1, 3):
#                     pygame.draw.line(ablak, FEKETE, (i*M, 0), (i*M, 3*M), 5)
#                     pygame.draw.line(ablak, FEKETE, (0, i*M), (3*M, i*M), 5)

#                 rajzol_tabla()
#                 pygame.display.flip()

# pygame.quit()

# 4. Nyerés/döntetlen felismerése
# Egyszerű ellenőrző függvény:

# import pygame

# pygame.init()

# M = 200
# ablak = pygame.display.set_mode((3*M, 3*M)) # függvény megnyit egy ablakot, amelybe rajzolhatsz
# pygame.display.set_caption("Tic Tac Toe") # ez a sor az ablak címsorában megjelenő szöveget állítja be

# FEHER = (255, 255, 255)
# FEKETE = (0, 0, 0)

# tabla = [
#     [" ", " ", " "],
#     [" ", " ", " "],
#     [" ", " ", " "]
# ]

# betu = pygame.font.SysFont(None, 120)  # Alapértelmezett betűtípus, 120-as méret
# uzenet_betu = pygame.font.SysFont(None, 60)  # Üzenetekhez kisebb betű

# def rajzol_tabla():
#     for sor in range(3):
#         for oszlop in range(3):
#             mezo = tabla[sor][oszlop]
#             if mezo != " ":
#                 szoveg = betu.render(mezo, True, FEKETE) # Ez létrehoz egy új képet (egy Surface objektumot), amin a "mezo" karakter (pl. "X" vagy "O") van kirajzolva szövegként a megadott színnel
#                 x = oszlop * M + M // 2 - szoveg.get_width() // 2 # Ez számítja ki a szöveg vízszintes pozícióját (azaz az X koordinátát)
#                 y = sor * M + M // 2 - szoveg.get_height() // 2 # Ez ugyanazt csinálja függőlegesen
#                 ablak.blit(szoveg, (x, y)) # kirajzolja a szöveget az ablakra a kiszámított (x, y) pozícióba

# def ellenor(tabla):
#     # sorok
#     for sor in tabla:
#         if sor[0] == sor[1] == sor[2] != " ":
#             return sor[0]

#     # oszlopok
#     for i in range(3):
#         if tabla[0][i] == tabla[1][i] == tabla[2][i] != " ":
#             return tabla[0][i]

#     # átlók
#     if tabla[0][0] == tabla[1][1] == tabla[2][2] != " ":
#         return tabla[0][0]
#     if tabla[0][2] == tabla[1][1] == tabla[2][0] != " ":
#         return tabla[0][2]
#     return None

# def uzenet_rajzol(uzenet):
#     ablak.fill(FEHER)
#     szoveg = uzenet_betu.render(uzenet, True, FEKETE)  # az üzenet szövegének létrehozása a kisebb betűmérettel
#     x = (3*M)//2 - szoveg.get_width()//2  # vízszintes középre igazítás
#     y = (3*M)//2 - szoveg.get_height()//2  # függőleges középre igazítás
#     ablak.blit(szoveg, (x, y))  # az üzenet kirajzolása az ablakra
#     pygame.display.flip()  # frissíti a képernyőt, hogy az üzenet megjelenjen

# ablak.fill(FEHER)

# for i in range(1, 3):
#     pygame.draw.line(ablak, FEKETE, (i*M, 0), (i*M, 3*M), 5)  # függőleges vonalak
#     pygame.draw.line(ablak, FEKETE, (0, i*M), (3*M, i*M), 5)  # vízszintes vonalak

# rajzol_tabla()
# pygame.display.flip()

# jelenlegi_jatekos = "X"

# fut = True
# while fut:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             fut = False

#         if event.type == pygame.MOUSEBUTTONDOWN:
#             x, y = pygame.mouse.get_pos()
#             sor = y // M
#             oszlop = x // M

#             if tabla[sor][oszlop] == " ":
#                 tabla[sor][oszlop] = jelenlegi_jatekos
#                 nyertes = ellenor(tabla)

#                 if nyertes is not None:
#                     print(f"Nyertes: {nyertes}")
#                     uzenet_rajzol(f"Nyertes: {nyertes}")
#                     fut = False
#                 else:
#                     ures_mezo = any(" " in sor for sor in tabla) # az any egy beépített Python függvény, ami azt vizsgálja, hogy a kapott iterálható (pl. lista, tuple) tartalmaz-e legalább egy igaz értéket
#                     if not ures_mezo:
#                         print("Döntetlen!")
#                         uzenet_rajzol("Döntetlen!")
#                         fut = False
#                     else:
#                         jelenlegi_jatekos = "O" if jelenlegi_jatekos == "X" else "X"

#                 if fut:  # csak ha nem ért véget a játék
#                     ablak.fill(FEHER)
#                     for i in range(1, 3):
#                         pygame.draw.line(ablak, FEKETE, (i*M, 0), (i*M, 3*M), 5)
#                         pygame.draw.line(ablak, FEKETE, (0, i*M), (3*M, i*M), 5)

#                     rajzol_tabla()
#                     pygame.display.flip()

# pygame.quit()

# 5. Főciklus: játék logika, állapotjelző

# A ciklus minden körben újrarajzolja a teljes képernyőt: először a rácsot, majd a tábla
# X/O-jeleit, végül a játék aktuális állapotát (ki következik, vagy ki nyert/döntetlen).

import pygame

pygame.init()

M = 200
ablak = pygame.display.set_mode((3*M, 3*M + 50))  # plusz hely az állapotjelzőnek
pygame.display.set_caption("Tic Tac Toe") # ez a sor az ablak címsorában megjelenő szöveget állítja be

FEHER = (255, 255, 255)
FEKETE = (0, 0, 0)

tabla = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

betu = pygame.font.SysFont(None, 120)  # Alapértelmezett betűtípus, 120-as méret
uzenet_betu = pygame.font.SysFont(None, 40)  # Üzenetekhez kisebb betű

def rajzol_tabla():
    for sor in range(3):
        for oszlop in range(3):
            mezo = tabla[sor][oszlop]
            if mezo != " ":
                szoveg = betu.render(mezo, True, FEKETE) # Ez létrehoz egy új képet (egy Surface objektumot), amin a "mezo" karakter (pl. "X" vagy "O") van kirajzolva szövegként a megadott színnel
                x = oszlop * M + M // 2 - szoveg.get_width() // 2 # Ez számítja ki a szöveg vízszintes pozícióját (azaz az X koordinátát)
                y = sor * M + M // 2 - szoveg.get_height() // 2 # Ez ugyanazt csinálja függőlegesen
                ablak.blit(szoveg, (x, y)) # kirajzolja a szöveget az ablakra a kiszámított (x, y) pozícióba

def ellenor(tabla):
    # sorok
    for sor in tabla:
        if sor[0] == sor[1] == sor[2] != " ":
            return sor[0]

    # oszlopok
    for i in range(3):
        if tabla[0][i] == tabla[1][i] == tabla[2][i] != " ":
            return tabla[0][i]

    # átlók
    if tabla[0][0] == tabla[1][1] == tabla[2][2] != " ":
        return tabla[0][0]
    if tabla[0][2] == tabla[1][1] == tabla[2][0] != " ":
        return tabla[0][2]
    return None

def uzenet_rajzol(uzenet):
    szoveg = uzenet_betu.render(uzenet, True, FEKETE)  # az üzenet szövegének létrehozása a kisebb betűmérettel
    x = (3*M)//2 - szoveg.get_width()//2  # vízszintes középre igazítás
    y = 3*M + (50 - szoveg.get_height())//2  # függőlegesen az alsó csík közepére
    ablak.blit(szoveg, (x, y))  # az üzenet kirajzolása az ablakra

ablak.fill(FEHER)

for i in range(1, 3):
    pygame.draw.line(ablak, FEKETE, (i*M, 0), (i*M, 3*M), 5)  # függőleges vonalak
    pygame.draw.line(ablak, FEKETE, (0, i*M), (3*M, i*M), 5)  # vízszintes vonalak

rajzol_tabla()
pygame.display.flip()

jelenlegi_jatekos = "X"
allapot = f"Következik: {jelenlegi_jatekos}"
fut = True

while fut:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fut = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if y < 3*M:  # csak a rács területén legyen érvényes kattintás
                sor = y // M
                oszlop = x // M

                if tabla[sor][oszlop] == " ":
                    tabla[sor][oszlop] = jelenlegi_jatekos
                    nyertes = ellenor(tabla)

                    if nyertes is not None:
                        print(f"Nyertes: {nyertes}")
                        allapot = f"Nyertes: {nyertes}"
                        fut = False
                    else:
                        ures_mezo = any(" " in sor for sor in tabla) # az any egy beépített Python függvény, ami azt vizsgálja, hogy a kapott iterálható (pl. lista, tuple) tartalmaz-e legalább egy igaz értéket
                        if not ures_mezo:
                            print("Döntetlen!")
                            allapot = "Döntetlen!"
                            fut = False
                        else:
                            jelenlegi_jatekos = "O" if jelenlegi_jatekos == "X" else "X"
                            allapot = f"Következik: {jelenlegi_jatekos}"

    # minden körben újrarajzolja a teljes képernyőt: először a rácsot,
    ablak.fill(FEHER)
    for i in range(1, 3):
        pygame.draw.line(ablak, FEKETE, (i*M, 0), (i*M, 3*M), 5)
        pygame.draw.line(ablak, FEKETE, (0, i*M), (3*M, i*M), 5)

    # majd a tábla X/O-jeleit,
    rajzol_tabla()

    # végül a játék aktuális állapotát (ki következik, vagy ki nyert/döntetlen).
    uzenet_rajzol(allapot)

    pygame.display.flip()

pygame.quit()
