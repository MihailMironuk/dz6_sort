def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    unsorted_list = [646, 346, 245, 132, 222, 141, 960]
    print("Неотсортированный список:",unsorted_list)
    sorted_list = bubble_sort(unsorted_list.copy())
    print("Пузырьковая сортировка:", sorted_list)

    target_element = 141

    index = binary_search(sorted_list, target_element)
    if index != -1:
        print(f"Число {target_element} найдено в индексе {index}.")
    else:
        print(f"Число {target_element} не найдено в списке.")
