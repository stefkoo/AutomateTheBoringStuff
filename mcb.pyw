#! python3
# mcb.pyw - Speichert Text und Lädt ihn in die Zwischenablage
# Nutzung: py.exe mcb.pyw save <Schlüssel> - Speichert den Inhalt der
#                                 Zwischen ablage unter dem Schlüssel
#
#          py.exe mcb.pyw <schlüssel> -Lädt den Wert zu dem Schlüssel
#                                               in die Zwischenablage
#          py.exe mcb.pyw list - lädt alle Schlüsselwörter in die
#                                               Zwischenablage

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# inhalt der zwischenablage speichern
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # Schlüsselwörter auflisten und Inhalt laden
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    # Löscht alle Schlüsselwörter
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
    # Kopiert Schlüsselwörter in die Zwischenablage
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    # löscht ein Schlüsselwort
    del mcbShelf[sys.argv[2]]

mcbShelf.close()
