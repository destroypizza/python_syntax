# *** Функции ***

# создание функции
def func_1(arg_1, arg_2):
    res = arg_1 + arg_2
    # print(res)
    return res

# вызов функция
# func_1(10, 3)
# func_1(1, 5)
# func_1(5, 50)

result = func_1(100, 200)

# print(result)

# САМОСТОЯТЕЛЬНО: 
# - ОСТАЛЬНЫЕ ВАРИАНТЫ ФУНКЦИЙ
# - ЛЯМБДА-ВЫРАЖЕНИЯ
# - typehinting
# - пространство имён


# *** Классы ***

# создание класса
class Human:
    # метод-конструктор
    def __init__(self, n="John", a=30):
        # атрибуты (свойства)
        self.name = n
        self.age = a
        # var = 100

    # метод - функция объекта
    def info(self):
        # print(var)
        print(f"Name: {self.name}, Age: {self.age}")

# создание экземпляров (объектов) класса Human
p0 = Human()
p1 = Human("Kate")
p2 = Human("Peter", 32)

# print(p0.age, p0.name)
# print(p1.age, p1.name)
# p1.name = "Kate"
# p1.age = 20
# print(p0.age, p0.name)
# print(p1.age, p1.name)

# print(p0.age, p0.name)
# print(p1.age, p1.name)
# print(p2.age, p2.name)

p0.info()
p1.info()
p2.info()


# самостоятельно:
# - принцыпы ООП (наследование, полиморфизм, инкапсуляция, абстракция)

