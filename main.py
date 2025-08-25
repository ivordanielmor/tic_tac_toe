import pygame
import sys
from helper import tabla_inicializalas, tabla_rajzol, nyertes_ellenorzes, ures_mezok, proba_gyoz, ai_valaszt, uzenet_rajzol, racs_rajzol

# Pygame inicializálása
pygame.init()

# Konstansok
M = 200  # Egy mező mérete pixelben
FEHER = (255, 255, 255)  # Fehér szín a háttérhez
FEKETE = (0, 0, 0)  # Fekete szín a szöveghez és vonalakhoz
TABLA_MERET = 3 * M  # Tábla teljes szélessége/magassága
ALLAPOT_SAV_MAGASSAG = 50  # Alsó állapotsáv magassága

def main():
    """Fő függvény az amőba játék futtatásához.

    Inicializálja a játékot, kezeli az eseménysort, és irányítja a játék állapotát.
    A játékos (X) egy AI (O) ellen játszik, vagy két játékos mód is választható (F1 billentyű).
    Újraindítás R billentyűvel lehetséges.
    """
    ablak = pygame.display.set_mode((TABLA_MERET, TABLA_MERET + ALLAPOT_SAV_MAGASSAG))
    pygame.display.set_caption("Amőba")
    tabla = tabla_inicializalas()
    betu = pygame.font.SysFont(None, 120)
    uzenet_betu = pygame.font.SysFont(None, 40)
    jelenlegi_jatekos = "X"
    egyedulijatekos = True
    allapot = f"{'Mód: AI | ' if egyedulijatekos else 'Mód: 2 játékos | '}Következik: {jelenlegi_jatekos}"
    fut = True

    while True:
        if not fut:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    tabla = tabla_inicializalas()
                    jelenlegi_jatekos = "X"
                    allapot = f"{'Mód: AI | ' if egyedulijatekos else 'Mód: 2 játékos | '}Következik: {jelenlegi_jatekos}"
                    fut = True

        while fut:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F1:
                        egyedulijatekos = not egyedulijatekos
                        allapot = f"{'Mód: AI | ' if egyedulijatekos else 'Mód: 2 játékos | '}Következik: {jelenlegi_jatekos}"
                    elif event.key == pygame.K_r:
                        tabla = tabla_inicializalas()
                        jelenlegi_jatekos = "X"
                        allapot = f"{'Mód: AI | ' if egyedulijatekos else 'Mód: 2 játékos | '}Következik: {jelenlegi_jatekos}"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if y < TABLA_MERET:
                        sor = y // M
                        oszlop = x // M
                        if tabla[sor][oszlop] == " ":
                            tabla[sor][oszlop] = jelenlegi_jatekos
                            nyertes = nyertes_ellenorzes(tabla)
                            if nyertes:
                                allapot = f"Nyertes: {nyertes} | Újraindítás R billentyűvel!"
                                fut = False
                            elif not any(" " in sor for sor in tabla):
                                allapot = f"Döntetlen! | Újraindítás R billentyűvel!"
                                fut = False
                            else:
                                jelenlegi_jatekos = "O" if jelenlegi_jatekos == "X" else "X"
                                allapot = f"{'Mód: AI | ' if egyedulijatekos else 'Mód: 2 játékos | '}Következik: {jelenlegi_jatekos}"
                                if egyedulijatekos and fut and jelenlegi_jatekos == "O":
                                    ai_sor, ai_oszlop = ai_valaszt(tabla)
                                    if ai_sor is not None:
                                        tabla[ai_sor][ai_oszlop] = "O"
                                        nyertes = nyertes_ellenorzes(tabla)
                                        if nyertes is not None:
                                            allapot = f"Nyertes: {nyertes} | Újraindítás R billentyűvel!"
                                            fut = False
                                        else:
                                            ures_mezo = any(" " in sor for sor in tabla)
                                            if not ures_mezo:
                                                allapot = f"Döntetlen! | Újraindítás R billentyűvel!"
                                                fut = False
                                            else:
                                                jelenlegi_jatekos = "X"
                                                allapot = f"{'Mód: AI | ' if egyedulijatekos else 'Mód: 2 játékos | '}Következik: {jelenlegi_jatekos}"

            # Képernyő újrarajzolása
            ablak.fill(FEHER)
            racs_rajzol(ablak)
            tabla_rajzol(ablak, tabla, betu)
            uzenet_rajzol(ablak, allapot, uzenet_betu)
            pygame.display.flip()

        # Játék vége utáni képernyő frissítése
        ablak.fill(FEHER)
        racs_rajzol(ablak)
        tabla_rajzol(ablak, tabla, betu)
        uzenet_rajzol(ablak, allapot, uzenet_betu)
        pygame.display.flip()

if __name__ == "__main__":
    main()
    