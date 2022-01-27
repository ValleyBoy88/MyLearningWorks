array = list(map(int, input("Введите последовательность чисел через пробел:\n").split()))
#print(array)

element = int(input("Введите число:\n"))
#print(element)

def func_sort(array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x
    return(array)

array = func_sort(array)
print(func_sort(array))

def func_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return "Подходящее под условие значение не найдено"  # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину

    if array[middle] >= element and array[middle - 1] < element:  # если элемент в середине,
        return middle-1  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине рекурсивно ищем в левой половине
        return func_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return func_search(array, element, middle + 1, right)
    if middle < 1 and array[len(array)-1] < element:
        return "Подходящее под условие значение не найдено"

# запускаем алгоритм на левой и правой границе
print(func_search(array, element, 0, len(array)))
