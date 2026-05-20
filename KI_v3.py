# =========================================================
# Projekt 7 - Tic-Tac-Toe II v3
# Datei: KI_v3.py
# Aufgabe:
# Verbesserte KI mit 3 Schwierigkeitsgraden
# =========================================================

# ---------------------------------------------------------
# Modul importieren
# ---------------------------------------------------------
import random


# =========================================================
# Funktion:
# Prüft Gewinnmöglichkeiten
# =========================================================
def pruefe_gewinn(board, symbol):

    gewinnkombinationen = [

        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [2, 4, 6]
    ]

    for kombination in gewinnkombinationen:

        a, b, c = kombination

        if board[a] == board[b] == symbol:
            return True

    return False


# =========================================================
# Funktion:
# Einfache KI
# Zufälliger Zug
# =========================================================
def einfacher_zug(board):

    freie_felder = []

    for i in range(len(board)):

        if board[i] == " ":
            freie_felder.append(i + 1)

    return random.choice(freie_felder)


# =========================================================
# Funktion:
# Mittlere KI
# Blockiert Spieler-Gewinn
# =========================================================
def mittlerer_zug(board):

    # -----------------------------------------------------
    # Prüft ob Spieler gewinnen kann
    # -----------------------------------------------------
    for i in range(9):

        if board[i] == " ":

            temp_board = board.copy()

            temp_board[i] = "X"

            # --- Spieler könnte gewinnen
            if pruefe_gewinn(temp_board, "X"):
                return i + 1

    # -----------------------------------------------------
    # Sonst zufälliger Zug
    # -----------------------------------------------------
    return einfacher_zug(board)


# =========================================================
# Funktion:
# Schwere KI
# Gewinnen + Blockieren
# =========================================================
def schwerer_zug(board):

    # -----------------------------------------------------
    # 1. Prüfen ob Computer gewinnen kann
    # -----------------------------------------------------
    for i in range(9):

        if board[i] == " ":

            temp_board = board.copy()

            temp_board[i] = "O"

            if pruefe_gewinn(temp_board, "O"):
                return i + 1

    # -----------------------------------------------------
    # 2. Spieler blockieren
    # -----------------------------------------------------
    for i in range(9):

        if board[i] == " ":

            temp_board = board.copy()

            temp_board[i] = "X"

            if pruefe_gewinn(temp_board, "X"):
                return i + 1

    # -----------------------------------------------------
    # 3. Mitte bevorzugen
    # -----------------------------------------------------
    if board[4] == " ":
        return 5

    # -----------------------------------------------------
    # 4. Zufälliger Zug
    # -----------------------------------------------------
    return einfacher_zug(board)