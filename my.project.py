# Программа с графическим пользовательским интерфейсом (GUI)

# *** Генератор паролей ***

# импортирование необходимых модулей
import hashlib as h
from tkinter import Tk, Label, Entry, Button, StringVar

# основная функция
def pwdGenerator(pwd_str: str):
    # кодирование в байт-строку
    byte_str = pwd_str.encode()
    # хеширование
    hash_str = h.sha256(byte_str)
    # преобразуем в обычную строчку
    hex_str = hash_str.hexdigest()[:10]
    return hex_str



# тестирование
# print(pwdGenerator(input("Введите пароль: ")))

# объект окна
app = Tk()

# объекты для хранения строк
raw_pwd = StringVar()
hash_pwd = StringVar()

# виджет текстовой метки
Label(text="Пароль:").grid(row=0, column=0)

# виджет поля ввода
Entry(textvariable=raw_pwd).grid(row=0, column=1)

# функция кнопки
def btn_func():
    hash_pwd.set(pwdGenerator(raw_pwd.get()))

# виджет кнопки
Button(text="ПУСК", command=btn_func).grid(row=1, column=0)

# виджет поля вывода
Entry(textvariable=hash_pwd).grid(row=1, column=1)

# точка входа программы
app.mainloop()

# самостоятельно:
# - калькулятор
# - что-то другое
# - kivy
# - PyQT