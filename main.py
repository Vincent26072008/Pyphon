# ============================================================
#  a1 Grundlagen: Mein erstes Programm
#  Informatik BK1T1  |  Programmierprojekt
# ============================================================
#
#  Aufgabe: Fülle alle ___ Stellen mit deinen eigenen Werten aus.
#  Lies den Kommentar rechts neben jeder Zeile – er sagt dir, was dort hinkommt.
#  Ändere NUR die ___ Stellen, den Rest lässt du so.
#
#  Wenn du fertig bist:
#    1. Ctrl+F5  →  Programm ausführen (Terminal unten)
#    2. Ctrl+S   →  Datei speichern
#    3. Source Control (Ctrl+Shift+G)  →  committen  →  pushen
# ============================================================

# Kein zusätzlicher Wert nötig – das Programm kann direkt gestartet werden.


# --- Variablen deklarieren ---

name     = "Max"    # str   – dein Vorname (in Anführungszeichen)
alter    = 10      # int   – dein Alter als Zahl (keine Anführungszeichen)
groesse  = 1.72      # float – deine Größe in Metern, z. B. 1.72
hat_bike = True      # bool  – hast du ein Fahrrad? Schreibe True oder False


# --- Konstante (Konvention: GROSSBUCHSTABEN) ---

KLASSE = "BK1T1"      # str   – deine Klassenbezeichnung, z. B. "BK1T1"


# --- Berechnung ---

geburtsjahr = 2026 - alter   # Hinweis: das Ergebnis ist eine ganze Zahl (int)


# --- Ausgabe ---

print("Hallo", name, "aus Klasse", KLASSE)
print("Geburtsjahr:", geburtsjahr)
print("Größe:", groesse, "m")
print("Fahrrad vorhanden:", hat_bike)


# ============================================================
#  ERWEITERUNG (freiwillig – wenn du schnell fertig bist)
# ============================================================
#
#  Füge hier eine eigene Variable hinzu (z. B. Lieblingsfarbe oder Schuhgröße)
#  und gib sie mit print() aus.
#
#  lieblingsfarbe = "___"   # str
#  print("Lieblingsfarbe:", lieblingsfarbe)
#
# ============================================================

