# *** Коллекции ***

#  Списки (list)

# Список - это упорядоченная (проиндекцированная), изменяемая (мутабельная) коллекция

# Объекты внутри списка - элементы
# каждый элемент проиндексирован
# прямая индексация начинается с 0
# обратная индексация начинается с -1

# Создание пустого списка
list_1 = []
list_1 = list()

# Создание предворительно заполненного списка
list_2 = [3,100,77,15]

list_3 = [10,20,3.14, "python", 'A', [1,2,3]]

list_4 = list("python")

# print(list_4)

# Добавление элемента в список
list_1.append(100)
list_1.append("hello")
list_1.append(5)
list_1.append([10,20,30])

# print(list_1)

# Чтение значений элементов
# при прямой индексации
el_1 = list_3[2]
el_1 = list_3[0]

# При обратной индексации
el_1 = list_3[-1]

# print(el_1)

# Чтение значений элементов вложенного списка
list_5 = [[10,20], [30,40,50], [60,70,80]]

# print(list_5[2][2])


# Замена значений
str_1 = "Hello, World!"
list_6 = list(str_1)

list_6[0] = 'h'
list_6[-3] = 100

# удаление элемента
# по индексу
# del list_6[-1]

# по значению
# list_6.remove('l')
# list_6.remove('l')

# по индексу с возвратом значения
# el_2 = list_6.pop()
# el_2 = list_6.pop(0)

# print(list_6)
# print(el_2)

# очистка списка
list_6.clear()

# print(list_6)


# срез списка
str_1 = "Hello, World!"
list_6 = list(str_1)

# срез от начала до конца
# l = len(list_6)
# print(l)
# slice_1 = list_6[:l]
slice_1 = list_6[:]

# срез от начала до индекса B (не включительно)
slice_1 = list_6[:6]

# срез от индекса А до конца списка
slice_1 = list_6[6:]

# срез от индекса А до индекса В (не включительно)
slice_1 = list_6[6:9]

# срез от начала до конца с шагом 2
slice_1 = list_6[::2]

# поворот списка (реверс)
slice_1 = list_6[::-2]

# срез от индекса А до индекса В (не включительно) с шагом 3
slice_1 = list_6[1:-2:3]

print(list_6)
print(slice_1)

                                                                  # посмотреть другие методы (не только append)