"""Dieses Modul implementiert den Merge-Sort-Algorithmus.

Der Algorithmus sortiert eine Liste von Zahlen stabil nach dem Prinzip
'Teile und herrsche' (Divide and Conquer).
"""

from typing import List
import matplotlib.pyplot as plt


def merge_sort(items: List[int]) -> None:
    """Sortiert eine Liste von Ganzzahlen aufsteigend mittels Merge Sort.

    Die Sortierung erfolgt in-place (die originale Liste wird modifiziert).

    Args:
        items: Eine Liste von Ganzzahlen, die sortiert werden soll.
    """
    # Rekursionsbasis: Eine Liste mit 0 oder 1 Elementen ist bereits sortiert
    if len(items) <= 1:
        return

    # 1. Teilen: Ermittle die Mitte und spalte die Liste in zwei Hälften
    mid = len(items) // 2
    left_half = items[:mid]
    right_half = items[mid:]

    # Rekursiver Aufruf für beide Hälften
    merge_sort(left_half)
    merge_sort(right_half)

    # 2. Beherrschen/Zusammenführen (Merge):
    # Indizes für die linke Hälfte (idx_left), rechte Hälfte (idx_right)
    # und die Ziel-Liste (idx_merged)
    idx_left = 0
    idx_right = 0
    idx_merged = 0

    # Vergleiche die Elemente beider Hälften und füge das kleinere Element ein
    while idx_left < len(left_half) and idx_right < len(right_half):
        if left_half[idx_left] <= right_half[idx_right]:
            items[idx_merged] = left_half[idx_left]
            idx_left += 1
        else:
            items[idx_merged] = right_half[idx_right]
            idx_right += 1
        idx_merged += 1

    # Kopiere verbleibende Elemente der linken Hälfte, falls vorhanden
    while idx_left < len(left_half):
        items[idx_merged] = left_half[idx_left]
        idx_left += 1
        idx_merged += 1

    # Kopiere verbleibende Elemente der rechten Hälfte, falls vorhanden
    while idx_right < len(right_half):
        items[idx_merged] = right_half[idx_right]
        idx_right += 1
        idx_merged += 1


if __name__ == "__main__":
    # Testdaten definieren
    unsorted_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    indices = range(len(unsorted_list))

    # Visualisierung der unsortierten Liste
    plt.figure("Merge Sort Demonstration")
    plt.subplot(1, 2, 1)
    plt.plot(indices, unsorted_list, "ro-")
    plt.title("Unsortiert")

    # Sortierung ausführen
    merge_sort(unsorted_list)

    # Visualisierung der sortierten Liste
    plt.subplot(1, 2, 2)
    plt.plot(indices, unsorted_list, "go-")
    plt.title("Sortiert")

    plt.show()

'''ÄNDERUNGEN
1. Inlining der Redundanz (ASSIGNMENT-Funktion entfernt): 
Die Funktion ASSIGNMENT war völlig unnötig, blähte den Call-Stack auf und machte einfache Zuweisungen (a[i] = b[j]) unleserlich. Das wurde direkt im Code gelöst.

2. Namenskonventionen (PEP 8): Funktionen und Variablen in Python nutzen snake_case statt camelCase. mergeSort wurde zu merge_sort, list_to_sort_by_merge zu items, etc.

3. Sprechende Variablennamen: Die einbuchstabigen Variablen l, r und i wurden durch aussagekräftigere Namen (idx_left, idx_right, idx_merged) ersetzt, um Verwechslungen (z. B. l mit der Zahl 1) zu vermeiden.

4. Logische Vereinfachung der if-Bedingung: Der Ausdruck if len(...) > 1 and not len(...) < 1 and len(...) != 0 war extrem redundant (dreifache Prüfung derselben Eigenschaft). Er wurde durch einen sauberen Guard Clause (if len(items) <= 1: return) ersetzt.

5. Vollständige Dokumentation (Docstrings): Es wurden ein Modul-Docstring sowie ein standardisierter Funktions-Docstring (inklusive Parameter- und Rückgabetyp-Erklärung) hinzugefügt.

6. Code-Kommentare: Die Kernschritte des Algorithmus (Teilen, Rekursion, Zusammenführen) wurden im Code direkt kommentiert, um die Nachvollziehbarkeit zu erhöhen.

7. Ausführungsschutz (if __name__ == "__main__":): Der ausführbare Test- und Plot-Code stand ungeschützt im globalen Namensraum. Er wurde in den main-Block verschoben, damit das Modul importiert werden kann, ohne sofort Plots zu öffnen.

8. Typ-Hinweise (Type Hinting): Die Funktion verwendet nun items: List[int] -> None, was die statische Code-Analyse und IDE-Autovervollständigung massiv verbessert.
'''

# alte code
'''def ASSIGNMENT(new_list, i, old_list, j):
    new_list[i] = old_list[j]


def mergeSort(list_to_sort_by_merge):
    if (
        len(list_to_sort_by_merge) > 1
        and not len(list_to_sort_by_merge) < 1
        and len(list_to_sort_by_merge) != 0
    ):
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        mergeSort(left)
        mergeSort(right)

        l = 0
        r = 0
        i = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=left, j=l)
                l += 1
            else:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=right, j=r)
                r += 1
            i += 1

        while l < len(left):
            list_to_sort_by_merge[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            list_to_sort_by_merge[i] = right[r]
            r += 1
            i += 1


import matplotlib.pyplot as plt

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
mergeSort(my_list)
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()'''
