def ASSIGNMENT(new_list, i, old_list, j):
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

original_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
sorted_list = original_list.copy()

mergeSort(sorted_list)

positions = range(len(original_list))

fig, axes = plt.subplots(1, 2, sharey=True, figsize=(10, 4))

axes[0].bar(positions, original_list)
axes[0].set_title("Before sorting")
axes[0].set_xlabel("Index")
axes[0].set_ylabel("Value")
axes[0].set_xticks(positions)

axes[1].bar(positions, sorted_list)
axes[1].set_title("After sorting")
axes[1].set_xlabel("Index")
axes[1].set_xticks(positions)

fig.suptitle("Merge Sort: List before and after sorting")
fig.tight_layout()

plt.show()
