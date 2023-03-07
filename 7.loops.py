# *** Циклы ***

# Оператор while


# бесконечный цикл
# while True:
#   print("hello!")

# цикл с условием
val_1 = 0

# while val_1 <= 10:
#     print(f"Значение: {val_1}")
#     # инкремент - увеличение значения
#     # длинный вариант
#     # val_1 = val_1 + 1
#     # короткий вариант
#     val_1 += 1

# while val_1 > -10:
#     print(f"Значение: {val_1}")
#     # декремент - уменьшение значения
#     val_1 -= 2


# прерывание цикла по дополнительному условие
# while True:
#     val_2 = input("Enter the name: ")
#     if val_2 == "stop":
#         print("Bye-bye!")
#         break
#     print(f"Hello, {val_2}!")

val_3 = 10

# while val_3 > 0:
#     print(val_3)
#     val_3 -= 1
#     if val_3 == 5:
#         break

# пропуск части кода тела цикла
val_4 = 0

# while val_4 < 20:
#     # первый кусок 
#     print(val_4)
#     val_4 += 1

#     # if val_4 >= 10:
#     #     continue
#     # # второй кусок
#     # print("hello")

#     if val_4 < 10:
#         continue
#     # второй кусок
#     break


# оператор for

# 1. "чтение" значения итерируемого объекта (последовательности) по порядку
# 2. каждое считанное значение присваивается в собственную переменную
# 3. выполняет код своего тела

# for c in "python":
#     print(c)

list_0 = [10, 20, 4, 3, 100, 827641]

# for val in list_0:
#     # val = val ** 2
#     val *= 2
#     print(val)

# idx = 0
# for val in list_0:
#     if idx == 0:
#         list_0[idx] = 777
#     idx += 1

# print(list_0)

# for idx, val in enumerate(list_0):
#     if idx == 0:
#         list_0[idx] = 1000
#     elif idx == 2:
#         list_0[idx] = "python"

# print(list_0)

dict_1 = dict(a=100, b=200, c=300)

# print(dict_1)

# for v in dict_1:
#     print(v)

# for i in dict_1.items():
#     print(i)

# for v in dict_1.values():
#     print(v)

# for k in dict_1.keys():
#     print(k)    

s = set([1,2,3,4])

# print(s)

# if isinstance(s, set):
#     for v in s:
#         v*=2
#         print(v)
# elif isinstance(s, list):
#     for v in s:
#         v+= 2
#         print(v)
# elif isinstance(s, int):
#         print(s + 100)

# класс range()
r = range(10)
# r = range(10,20,2)

# print(r)

# for n in r:
#     print(n)

# for n in range(-5, 5):
#     print(n)

# безымянная переменная
# for _ in range(5):
#     print("hello")


                            # генератор списка
                            # генератор словаря