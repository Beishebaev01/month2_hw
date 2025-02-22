def selection_sort(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[j] > lst[i]:
                lst[j], lst[i] = lst[i], lst[j]


unsorted_list = [2, 3, 1, 1, -3, 4, 10, 0, 2]
selection_sort(unsorted_list)
print(f'List by Selection Sort: {unsorted_list}')


def bubble_sort(lst1):
    for i in range(len(lst1)):
        for j in range(len(lst1) - i - 1):
            if lst1[j] > lst1[j + 1]:
                lst1[j], lst1[j + 1] = lst1[j + 1], lst1[j]


unsorted_list = [2, 3, 1, 1, -3, 4, 10, 0, 2]
bubble_sort(unsorted_list)
print(f'List Bubble Sort: {unsorted_list}')


def binary_search(elm, lst2):
    n = len(lst2)
    resultOk = False
    first = 0
    last = n - 1
    pos = -1
    while first < last:
        middle = (first + last) // 2
        if elm == lst2[middle]:
            first = middle
            last = first
            resultOk = True
            pos = middle

        else:
            if elm > lst2[middle]:
                first = middle + 1
            else:
                last = middle - 1

    if resultOk == True:
        print(f'Элемент {elm} найден под индексом {pos}')

    else:
        print("Элемент не найден")


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
binary_search(8, lst)
