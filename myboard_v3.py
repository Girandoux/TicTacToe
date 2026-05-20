# =========================================================
# Projekt 7 - Tic-Tac-Toe II v3
# Datei: myboard_v3.py
# Aufgabe:
# Enthält alle Spielfeld-Funktionen
# =========================================================


# =========================================================
# Funktion:
# Prüft, ob ein Zug gültig ist
# =========================================================
def check_if_valid(board, auswahl):

    return auswahl in range(1, 10) and board[auswahl - 1] == " "


# =========================================================
# Funktion:
# Prüft die Gewinnbedingungen
# =========================================================
def check_win_condition(board):

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

    # --- Prüft jede Gewinnkombination
    for kombination in gewinnkombinationen:

        a, b, c = kombination

        # --- Wenn alle drei Felder gleich sind
        if board[a] == board[b] == board[c] != " ":
            return True

    return False


# =========================================================
# Funktion:
# Erstellt ein leeres Spielfeld
# =========================================================
def clear_board():

    return [" "] * 9