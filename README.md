# Tic Tac Toe – Pygame alapú amőba játék

Ez egy egyszerű, grafikus felületű [Tic Tac Toe](w) (avagy amőba) játék, amelyet a [Pygame](w) könyvtár segítségével valósítottunk meg. A program két játékos (X és O) között váltogatja a köröket, és kijelzi a győztest vagy a döntetlent.

## 🕹️ Játékmenet

- A játékosok egymás után kattintanak a mezőkre.
- A cél: három azonos jel (X vagy O) egy sorban, oszlopban vagy átlóban.
- A program kijelzi, ha valaki nyert vagy ha döntetlen lett a játék.
- Az állapotjelző sáv alul mutatja, hogy ki következik, vagy ki nyert.

## 🧱 Felépítés

- **pygame ablak**: 3x3-as rács, plusz 50 pixel magas alsó sáv az üzeneteknek.
- **Két betűméret**:
  - Játékjelekhez (`X`, `O`): nagyobb méret
  - Állapotüzenethez: kisebb méret
- **Főbb függvények**:
  - `rajzol_tabla()` – kirajzolja az X/O jeleket
  - `ellenor()` – ellenőrzi, van-e győztes
  - `uzenet_rajzol()` – kiírja, ki következik vagy ki nyert

## 🛠️ Telepítés és futtatás

### 1. Követelmények

- [Python 3](w)
- [Pygame](w)

Telepítés pip-pel:
```bash
pip install pygame
```

### 2. A játék futtatása

Mentés pl. `tic_tac_toe.py` néven, majd:

```bash
python tic_tac_toe.py
```

## 🧠 Funkciók összefoglalása

- Teljes körű kattintásérzékelés a rácsban
- Egyszerű ellenőrzés győztesre és döntetlenre
- Grafikus megjelenítés minden frissítéskor
- Konzolra is kiírja az eredményt (győzelem/döntetlen)

## 📷 Képernyőkép

![Tic Tac Toe játékkép](./kepek/screenshot.png)

## 📄 Licenc

Ez a projekt szabadon felhasználható tanulási célokra.

---

**Kellemes játékot! 🎮**
