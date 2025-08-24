import pygame
from typing import List, Tuple, Optional

def tabla_inicializalas() -> List[List[str]]:
    """Üres 3x3-as amőba tábla inicializálása.

    Visszatérés:
        List[List[str]]: 3x3-as rács üres helyekkel inicializálva.
    """
    return [[" " for _ in range(3)] for _ in range(3)]

def tabla_rajzol(ablak: pygame.Surface, tabla: List[List[str]], betu: pygame.font.Font) -> None:
    """Az amőba tábla kirajzolása X/O szimbólumokkal.

    Argumentumok:
        ablak (pygame.Surface): A Pygame felület, amire rajzolunk.
        tabla (List[List[str]]): A 3x3-as játék tábla "X", "O" vagy " " értékekkel.
        betu (pygame.font.Font): Betűtípus az X/O szimbólumokhoz.
    """
    M = 200  # Konstans a main.py-ból
    FEKETE = (0, 0, 0)
    for sor in range(3):
        for oszlop in range(3):
            if tabla[sor][oszlop] != " ":
                szoveg = betu.render(tabla[sor][oszlop], True, FEKETE)
                x = oszlop * M + M // 2 - szoveg.get_width() // 2
                y = sor * M + M // 2 - szoveg.get_height() // 2
                ablak.blit(szoveg, (x, y))

def nyertes_ellenorzes(tabla: List[List[str]]) -> Optional[str]:
    """Ellenőrzi, van-e nyertes a táblán.

    Sorokat, oszlopokat és átlókat vizsgál három azonos szimbólumra.

    Argumentumok:
        tabla (List[List[str]]): A 3x3-as játék tábla.

    Visszatérés:
        Optional[str]: A nyertes szimbólum ("X" vagy "O"), vagy None, ha nincs nyertes.
    """
    for sor in tabla:
        if sor[0] == sor[1] == sor[2] != " ":
            return sor[0]
    for i in range(3):
        if tabla[0][i] == tabla[1][i] == tabla[2][i] != " ":
            return tabla[0][i]
    if tabla[0][0] == tabla[1][1] == tabla[2][2] != " ":
        return tabla[0][0]
    if tabla[0][2] == tabla[1][1] == tabla[2][0] != " ":
        return tabla[0][2]
    return None

def ures_mezok(tabla: List[List[str]]) -> List[Tuple[int, int]]:
    """Visszaadja az üres mezők koordinátáinak listáját.

    Argumentumok:
        tabla (List[List[str]]): A 3x3-as játék tábla.

    Visszatérés:
        List[Tuple[int, int]]: Üres mezők (sor, oszlop) koordinátáinak listája.
    """
    return [(sor, oszlop) for sor in range(3) for oszlop in range(3) if tabla[sor][oszlop] == " "]

def proba_gyoz(tabla: List[List[str]], jatekos: str) -> Optional[Tuple[int, int]]:
    """Ellenőrzi, hogy a játékos nyerhet-e egy lépéssel.

    Ideiglenesen elhelyezi a játékos szimbólumát minden üres mezőbe, és ellenőrzi a nyerést.

    Argumentumok:
        tabla (List[List[str]]): A 3x3-as játék tábla.
        jatekos (str): A játékos szimbóluma ("X" vagy "O").

    Visszatérés:
        Optional[Tuple[int, int]]: A nyerő lépés (sor, oszlop) koordinátái, vagy None.
    """
    for sor, oszlop in ures_mezok(tabla):
        tabla[sor][oszlop] = jatekos
        if nyertes_ellenorzes(tabla) == jatekos:
            tabla[sor][oszlop] = " "
            return (sor, oszlop)
        tabla[sor][oszlop] = " "
    return None

def ai_valaszt(tabla: List[List[str]]) -> Optional[Tuple[int, int]]:
    """Az AI lépésének meghatározása (O játékosként) szabályalapú stratégiával.

    Stratégia:
        1) Nyerés, ha lehetséges egy lépéssel.
        2) Ellenfél (X) nyerésének blokkolása.
        3) Ha az ellenfél a középen van (1,1), ellentétes sarok választása.
        4) Középső mező (1,1) elfoglalása, ha szabad.
        5) Bármelyik sarok elfoglalása.
        6) Bármelyik oldal elfoglalása.

    Argumentumok:
        tabla (List[List[str]]): A 3x3-as játék tábla.

    Visszatérés:
        Optional[Tuple[int, int]]: Az AI lépésének (sor, oszlop) koordinátái, vagy None, ha nincs lépés.
    """
    lep = proba_gyoz(tabla, "O")
    if lep:
        return lep
    lep = proba_gyoz(tabla, "X")
    if lep:
        return lep
    if tabla[1][1] == "X":
        ellentetes_sarkok = [((0, 0), (2, 2)), ((0, 2), (2, 0))]
        for sarok1, sarok2 in ellentetes_sarkok:
            if tabla[sarok1[0]][sarok1[1]] == " ":
                return sarok1
            if tabla[sarok2[0]][sarok2[1]] == " ":
                return sarok2
    if tabla[1][1] == " ":
        return (1, 1)
    sarkok = [(0, 0), (0, 2), (2, 0), (2, 2)]
    for sor, oszlop in sarkok:
        if tabla[sor][oszlop] == " ":
            return (sor, oszlop)
    oldalak = [(0, 1), (1, 0), (1, 2), (2, 1)]
    for sor, oszlop in oldalak:
        if tabla[sor][oszlop] == " ":
            return (sor, oszlop)
    return None

def uzenet_rajzol(ablak: pygame.Surface, uzenet: str, uzenet_betu: pygame.font.Font) -> None:
    """Az állapotsáv üzenetének kirajzolása az ablak alján.

    Argumentumok:
        ablak (pygame.Surface): A Pygame felület, amire rajzolunk.
        uzenet (str): A megjelenítendő üzenet (pl. "Következik: X" vagy "Nyertes: O").
        uzenet_betu (pygame.font.Font): Betűtípus az állapotsáv üzenetéhez.
    """
    TABLA_MERET = 600  # Konstans a main.py-ból
    ALLAPOT_SAV_MAGASSAG = 50
    FEKETE = (0, 0, 0)
    szoveg = uzenet_betu.render(uzenet, True, FEKETE)
    x = TABLA_MERET // 2 - szoveg.get_width() // 2
    y = TABLA_MERET + (ALLAPOT_SAV_MAGASSAG - szoveg.get_height()) // 2
    ablak.blit(szoveg, (x, y))

def racs_rajzol(ablak: pygame.Surface) -> None:
    """Az amőba rács vonalainak kirajzolása.

    Argumentumok:
        ablak (pygame.Surface): A Pygame felület, amire rajzolunk.
    """
    M = 200  # Konstans a main.py-ból
    FEKETE = (0, 0, 0)
    TABLA_MERET = 600
    for i in range(1, 3):
        pygame.draw.line(ablak, FEKETE, (i * M, 0), (i * M, TABLA_MERET), 5)
        pygame.draw.line(ablak, FEKETE, (0, i * M), (TABLA_MERET, i * M), 5)
        