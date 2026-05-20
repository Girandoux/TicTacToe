# =========================================================
# Projekt 7 - Tic-Tac-Toe II v3
# Datei: window_v3.py
# Aufgabe:
# GUI-Fenster für Tic-Tac-Toe II
# =========================================================

# ---------------------------------------------------------
# Module importieren
# ---------------------------------------------------------
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

import myboard_v3
import KI_v3


# =========================================================
# Klasse:
# TicTacToeGUI
# =========================================================
class TicTacToeGUI:

    # -----------------------------------------------------
    # Konstruktor
    # -----------------------------------------------------
    def __init__(self, root):

        self.root = root

        # -------------------------------------------------
        # Fenster-Einstellungen
        # -------------------------------------------------
        self.root.title("Tic-Tac-Toe II v3")

        self.root.geometry("500x750")

        # -------------------------------------------------
        # Spielername abfragen
        # -------------------------------------------------
        self.spielername = simpledialog.askstring(

            "Spielername",
            "Bitte Namen eingeben:"

        )

        # -------------------------------------------------
        # Standardname
        # -------------------------------------------------
        if not self.spielername:

            self.spielername = "Spieler"

        # -------------------------------------------------
        # Schwierigkeit auswählen
        # -------------------------------------------------
        self.schwierigkeit = simpledialog.askstring(

            "Schwierigkeit",
            "einfach, mittel oder schwer?"

        )

        # -------------------------------------------------
        # Standard-Schwierigkeit
        # -------------------------------------------------
        if self.schwierigkeit not in [

            "einfach",
            "mittel",
            "schwer"

        ]:

            self.schwierigkeit = "einfach"

        # -------------------------------------------------
        # Punktestand
        # -------------------------------------------------
        self.spieler_punkte = 0

        self.pc_punkte = 0

        # -------------------------------------------------
        # Spielfeld
        # -------------------------------------------------
        self.board = [" "] * 9

        # -------------------------------------------------
        # Titel
        # -------------------------------------------------
        self.title_label = tk.Label(

            root,

            text="Tic-Tac-Toe II v3",

            font=("Arial", 20, "bold")

        )

        self.title_label.pack(pady=10)

        # -------------------------------------------------
        # Spielername anzeigen
        # -------------------------------------------------
        self.name_label = tk.Label(

            root,

            text=f"Spieler: {self.spielername}",

            font=("Arial", 14)

        )

        self.name_label.pack()

        # -------------------------------------------------
        # Schwierigkeit anzeigen
        # -------------------------------------------------
        self.level_label = tk.Label(

            root,

            text=f"Schwierigkeit: {self.schwierigkeit}",

            font=("Arial", 12)

        )

        self.level_label.pack(pady=5)

        # -------------------------------------------------
        # Punktestand anzeigen
        # -------------------------------------------------
        self.score_label = tk.Label(

            root,

            text=self.punktestand_text(),

            font=("Arial", 14, "bold")

        )

        self.score_label.pack(pady=10)

        # -------------------------------------------------
        # Spielfeld-Frame
        # -------------------------------------------------
        self.frame = tk.Frame(root)

        self.frame.pack()

        # -------------------------------------------------
        # Button-Liste
        # -------------------------------------------------
        self.buttons = []

        # -------------------------------------------------
        # Spielfeld-Buttons erzeugen
        # -------------------------------------------------
        for i in range(9):

            button = tk.Button(

                self.frame,

                text=" ",

                width=8,

                height=4,

                font=("Arial", 20),

                command=lambda i=i: self.spielzug(i)

            )

            button.grid(

                row=i // 3,
                column=i % 3

            )

            self.buttons.append(button)

        # -------------------------------------------------
        # Restart-Button
        # -------------------------------------------------
        self.restart_button = tk.Button(

            root,

            text="🔄 Neues Spiel",

            font=("Arial", 14, "bold"),

            bg="lightblue",

            width=20,

            height=2,

            command=self.reset_game

        )

        self.restart_button.pack(pady=20)

        # -------------------------------------------------
        # Statusanzeige
        # -------------------------------------------------
        self.status_label = tk.Label(

            root,

            text="Du spielst mit X",

            font=("Arial", 12)

        )

        self.status_label.pack(pady=10)

    # =====================================================
    # Funktion:
    # Punktestand anzeigen
    # =====================================================
    def punktestand_text(self):

        return (

            f"{self.spielername}: {self.spieler_punkte}    "
            f"PC: {self.pc_punkte}"

        )

    # =====================================================
    # Funktion:
    # Spielerzug
    # =====================================================
    def spielzug(self, position):

        # -------------------------------------------------
        # Feld bereits besetzt
        # -------------------------------------------------
        if self.board[position] != " ":

            return

        # -------------------------------------------------
        # Spieler setzt X
        # -------------------------------------------------
        self.board[position] = "X"

        self.buttons[position]["text"] = "X"

        # -------------------------------------------------
        # Gewinn prüfen
        # -------------------------------------------------
        if myboard_v3.check_win_condition(self.board):

            self.spieler_punkte += 1

            self.score_label.config(

                text=self.punktestand_text()

            )

            messagebox.showinfo(

                "Gewonnen",

                f"{self.spielername} hat gewonnen!"

            )

            self.reset_board()

            return

        # -------------------------------------------------
        # Unentschieden
        # -------------------------------------------------
        if " " not in self.board:

            messagebox.showinfo(

                "Unentschieden",

                "Keiner hat gewonnen!"

            )

            self.reset_board()

            return

        # -------------------------------------------------
        # Computerzug
        # -------------------------------------------------
        self.computerzug()

    # =====================================================
    # Funktion:
    # Computerzug
    # =====================================================
    def computerzug(self):

        # -------------------------------------------------
        # Schwierigkeit auswählen
        # -------------------------------------------------
        if self.schwierigkeit == "schwer":

            zug = KI_v3.schwerer_zug(self.board)

        elif self.schwierigkeit == "mittel":

            zug = KI_v3.mittlerer_zug(self.board)

        else:

            zug = KI_v3.einfacher_zug(self.board)

        # -------------------------------------------------
        # Computer setzt O
        # -------------------------------------------------
        self.board[zug - 1] = "O"

        self.buttons[zug - 1]["text"] = "O"

        # -------------------------------------------------
        # Gewinn prüfen
        # -------------------------------------------------
        if myboard_v3.check_win_condition(self.board):

            self.pc_punkte += 1

            self.score_label.config(

                text=self.punktestand_text()

            )

            messagebox.showinfo(

                "Verloren",

                "Der Computer hat gewonnen!"

            )

            self.reset_board()

            return

        # -------------------------------------------------
        # Unentschieden
        # -------------------------------------------------
        if " " not in self.board:

            messagebox.showinfo(

                "Unentschieden",

                "Keiner hat gewonnen!"

            )

            self.reset_board()

    # =====================================================
    # Funktion:
    # Nur Spielfeld zurücksetzen
    # =====================================================
    def reset_board(self):

        # -------------------------------------------------
        # Neues Spielfeld
        # -------------------------------------------------
        self.board = [" "] * 9

        # -------------------------------------------------
        # Buttons leeren
        # -------------------------------------------------
        for button in self.buttons:

            button["text"] = " "

    # =====================================================
    # Funktion:
    # Komplettes Spiel zurücksetzen
    # =====================================================
    def reset_game(self):

        # -------------------------------------------------
        # Spielfeld zurücksetzen
        # -------------------------------------------------
        self.reset_board()

        # -------------------------------------------------
        # Punktestand zurücksetzen
        # -------------------------------------------------
        self.spieler_punkte = 0

        self.pc_punkte = 0

        # -------------------------------------------------
        # Punktestand aktualisieren
        # -------------------------------------------------
        self.score_label.config(

            text=self.punktestand_text()

        )

        # -------------------------------------------------
        # Statusanzeige aktualisieren
        # -------------------------------------------------
        self.status_label.config(

            text="Neues Spiel gestartet"

        )


# =========================================================
# Funktion:
# Fenster starten
# =========================================================
def start_window():

    root = tk.Tk()

    app = TicTacToeGUI(root)

    root.mainloop()