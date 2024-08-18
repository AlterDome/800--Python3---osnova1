#
# Это однострочный комментарий.
#
# Author Rybochkin Aleksei
#
#  august 2024
#
######

from tkinter import *   # подключили все функции модуля ткинтер
from tkinter import ttk

import os  # подключили основной модуль и графику ткинтер как tkr


print ("Hello world")     # вывод текста

#tkr._test() # Тестовое окно от Ткинтер, Стандарт

######  Создаем окно
root = Tk()   # главная переменная к окну
root.title("   Main window  ")  # создание главного окна - назввние
root.geometry("700x400")   #  размеры окна  ширина - верх

###############

def click():  # 28
    window = Tk()
    window.title(" do4ernee okno  ")
    window.geometry("600x300")
    label=ttk.Label(window, text="New window")
    label.pack(anchor=CENTER, expand=1)


###########
btn = ttk.Button(text="  Кнопка создания окна ", command=click)
btn.pack(anchor=CENTER, expand=1)


root.mainloop()  # бесконечный цикл, который используется для запуска приложения,
                 #ожидания события и обработки события, пока окно не закрыто.

#####################################
#  Стандартные 2 строки на выяснение модуля или программа
if __name__ == "__main__":
    print("Этот файл майн")
else:
    print("Этот файл как модуль подключен")
