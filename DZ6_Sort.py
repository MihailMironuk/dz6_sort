def Bubble_sort(arr):
    n = len(arr)
    for run in range(n - 1):
        for i in range(n - 1 - run):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


def binary_search(find_obj, lst):
    pos = 0
    Rusult0k = False
    first = 0
    last = len(lst) - 1

    while first < last:
        middle = (first + last) // 2
        if lst[middle] == find_obj:
            first = middle
            last = first
            Rusult0k = True
            pos = middle
        elif find_obj < lst[middle]:
            first = middle + 1
        else:
            last = middle - 1

    if Rusult0k:
        print("Число найдено, Индекс", pos)
    else:
        print("Число не найдено.")


from random import randint as gen_nums

my_list = []
for num in range(11):

    my_list.append(gen_nums(0, 20000))

print("Несортированный список:", my_list)
sorted_list = Bubble_sort(my_list)

print("Пузырьковая сортировка:", sorted_list)
search = int(input("Вы нашли число:"))

binary_search(search, sorted_list)
