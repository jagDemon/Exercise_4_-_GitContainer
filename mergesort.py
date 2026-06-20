"""Dieses Modul implementiert den Merge-Sort-Algorithmus.

Der Algorithmus sortiert eine Liste von Zahlen stabil nach dem Prinzip
'Teile und herrsche' (Divide and Conquer).
"""

from typing import List

import matplotlib.pyplot as plt


def merge_sort(items: List[int]) -> None:
    """Sortiert eine Liste von Ganzzahlen aufsteigend mittels Merge Sort.

    Die Sortierung erfolgt in-place. Das bedeutet, dass die originale Liste
    direkt verändert wird.

    Args:
        items: Eine Liste von Ganzzahlen, die sortiert werden soll.
    """
    if len(items) <= 1:
        return

    middle_index = len(items) // 2
    left_half = items[:middle_index]
    right_half = items[middle_index:]

    merge_sort(left_half)
    merge_sort(right_half)

    left_index = 0
    right_index = 0
    target_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            items[target_index] = left_half[left_index]
            left_index += 1
        else:
            items[target_index] = right_half[right_index]
            right_index += 1

        target_index += 1

    while left_index < len(left_half):
        items[target_index] = left_half[left_index]
        left_index += 1
        target_index += 1

    while right_index < len(right_half):
        items[target_index] = right_half[right_index]
        right_index += 1
        target_index += 1


def mergeSort(items: List[int]) -> None:
    """Kompatibilitätsfunktion für den ursprünglichen Funktionsnamen."""
    merge_sort(items)


def plot_before_and_after_sorting(original_items: List[int]) -> None:
    """Visualisiert die Liste vor und nach der Sortierung."""
    sorted_items = original_items.copy()
    merge_sort(sorted_items)

    positions = range(len(original_items))

    fig, axes = plt.subplots(1, 2, sharey=True, figsize=(10, 4))

    axes[0].bar(positions, original_items)
    axes[0].set_title("Before sorting")
    axes[0].set_xlabel("Index")
    axes[0].set_ylabel("Value")
    axes[0].set_xticks(positions)

    axes[1].bar(positions, sorted_items)
    axes[1].set_title("After sorting")
    axes[1].set_xlabel("Index")
    axes[1].set_xticks(positions)

    fig.suptitle("Merge Sort: List before and after sorting")
    fig.tight_layout()

    plt.show()


def main() -> None:
    """Führt ein kleines Beispiel für Merge Sort aus."""
    values = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    plot_before_and_after_sorting(values)


if __name__ == "__main__":
    main()