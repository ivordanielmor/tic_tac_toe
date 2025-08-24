# Tic Tac Toe – Pygame-based Game

This is a graphical [Tic Tac Toe](https://en.wikipedia.org/wiki/Tic-tac-toe) game built using the [Pygame](https://www.pygame.org/news) library. The game supports both single-player mode (against an AI) and two-player mode, with additional features like game reset and an enhanced AI strategy.

## 🕹️ Gameplay

- Players take turns clicking on the grid squares to place their marks (X or O).
- The goal is to place three identical marks in a row, column, or diagonal.
- The game shows when someone wins or if it’s a draw.
- The status bar at the bottom indicates the current mode (AI or two-player), whose turn it is, or the game result.
- **Mode switching**: Press **F1** to toggle between single-player (AI) and two-player modes.
- **Game reset**: Press **R** to reset the board and start a new game.
- **Smart AI**: In single-player mode, the AI (playing as O) uses an enhanced strategy, prioritizing winning, blocking, and choosing opposite corners if the opponent takes the center.
- **Game end message**: After the game ends (win or draw), the status bar shows "Restart with R key!" alongside the result.

## 🧱 Structure

- **Pygame window**: 3x3 grid with a 50-pixel bottom bar for status messages.
- **Two font sizes**:
  - Larger font for game marks (`X`, `O`)
  - Smaller font for status messages
- **Main files**:
  - `main.py`: Contains the main game loop, event handling, and game initialization.
  - `helper.py`: Contains helper functions for board management, drawing, and AI logic.
- **Main functions** (in `helper.py` unless noted):
  - `tabla_rajzol()` – renders the X/O marks
  - `nyertes_ellenorzes()` – checks for a winning condition
  - `uzenet_rajzol()` – shows the game mode, next turn, or winner
  - `ai_valaszt()` – implements the AI strategy
  - `main()` (in `main.py`) – handles the game loop and event handling

## 🛠️ Installation & Running

### 1. Requirements

- [Python 3](https://www.python.org/)
- [Pygame](https://www.pygame.org/news)

Install with pip:
```bash
pip install pygame
```

### 2. Running the game

Save the files as `main.py` and `helper.py` in the same directory, then run:

```bash
python main.py
```

## 🧠 Features Overview

- Full click detection in the grid
- Simple win/draw checking
- Graphical updates after every turn
- Prints results (win/draw) to the console
- **Mode switching** with F1 key (AI vs two-player)
- **Game reset** with R key, with a message "Restart with R key!" shown after the game ends
- **Enhanced AI** that prioritizes:
  1. Winning in one move
  2. Blocking opponent's win
  3. Choosing opposite corners if the opponent takes the center
  4. Taking the center, corners, or sides in that order

## 📷 Screenshot

![Tic Tac Toe screenshot](./kepek/screenshot.png)

## 📄 License

This project is free to use for learning purposes.

---

**Have fun playing! 🎮**

---

# Amőba – Pygame alapú játék

Ez egy grafikus felületű [Tic Tac Toe](https://en.wikipedia.org/wiki/Tic-tac-toe) (amőba) játék, amelyet a [Pygame](https://www.pygame.org/news) könyvtár segítségével valósítottunk meg. A játék támogatja az egyjátékos módot (AI ellen) és a kétjátékos módot, valamint további funkciókat, mint a játék újraindítása és egy okosabb AI stratégia.

## 🕹️ Játékmenet

- A játékosok egymás után kattintanak a mezőkre, hogy elhelyezzék jeleiket (X vagy O).
- A cél: három azonos jel egy sorban, oszlopban vagy átlóban.
- A program kijelzi, ha valaki nyert vagy ha döntetlen lett a játék.
- Az alsó állapotsáv mutatja az aktuális módot (AI vagy kétjátékos), hogy ki következik, vagy az eredményt.
- **Módváltás**: Az **F1** billentyűvel válthatsz egyjátékos (AI) és kétjátékos mód között.
- **Újraindítás**: Az **R** billentyűvel újraindíthatod a játékot, üres táblával.
- **Okosabb AI**: Egyjátékos módban az AI (O játékosként) fejlettebb stratégiát használ, prioritást adva a nyerésnek, blokkolásnak, és ellentétes sarkok választásának, ha az ellenfél a középen van.
- **Játék vége üzenet**: A játék vége után (győzelem vagy döntetlen) az állapotsáv kiírja: "Újraindítás R billentyűvel!" az eredmény mellett.

## 🧱 Felépítés

- **Pygame ablak**: 3x3-as rács, plusz 50 pixel magas alsó sáv az üzeneteknek.
- **Két betűméret**:
  - Játékjelekhez (`X`, `O`): nagyobb méret
  - Állapotüzenethez: kisebb méret
- **Főbb fájlok**:
  - `main.py`: Tartalmazza a fő játékciklust, eseménykezelést és inicializálást.
  - `helper.py`: Tartalmazza a segédfüggvényeket a tábla kezeléséhez, rajzoláshoz és AI logikához.
- **Főbb függvények** (a `helper.py`-ban, kivéve ahol jelezve):
  - `tabla_rajzol()` – kirajzolja az X/O jeleket
  - `nyertes_ellenorzes()` – ellenőrzi, van-e győztes
  - `uzenet_rajzol()` – kiírja a játék módját, hogy ki következik, vagy ki nyert
  - `ai_valaszt()` – megvalósítja az AI stratégiát
  - `main()` (a `main.py`-ban) – kezeli a játék ciklust és az eseménykezelést

## 🛠️ Telepítés és futtatás

### 1. Követelmények

- [Python 3](https://www.python.org/)
- [Pygame](https://www.pygame.org/news)

Telepítés pip-pel:
```bash
pip install pygame
```

### 2. A játék futtatása

Mentés `main.py` és `helper.py` néven ugyanabba a könyvtárba, majd:

```bash
python main.py
```

## 🧠 Funkciók összefoglalása

- Teljes körű kattintásérzékelés a rácsban
- Egyszerű ellenőrzés győztesre és döntetlenre
- Grafikus frissítés minden körben
- Eredmény kiírása a konzolra (győzelem/döntetlen)
- **Módváltás** F1 billentyűvel (AI vs kétjátékos)
- **Újraindítás** R billentyűvel, játék vége után "Újraindítás R billentyűvel!" üzenettel
- **Okosabb AI**, amely a következő prioritásokat követi:
  1. Nyerés egy lépésben
  2. Ellenfél nyerésének blokkolása
  3. Ellentétes sarok választása, ha az ellenfél a középen van
  4. Közép, sarkok vagy oldalak elfoglalása ebben a sorrendben

## 📷 Képernyőkép

![Amőba játékkép](./kepek/screenshot.png)

## 📄 Licenc

Ez a projekt szabadon felhasználható tanulási célokra.

---

**Kellemes játékot! 🎮**
