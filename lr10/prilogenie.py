from tkinter import *
from tkinter import ttk 
from tkinter.ttk import Checkbutton
import tkinter.messagebox as mb

window = Tk()
window.title("Дегтярев Антон Николаевич Уб-21")
window.geometry('700x500') 

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Калькулятор')


tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Вторая')

def clicked():
    if s == True:
        mb.showinfo('Информация', 'Вы выбрали первый вариант ответа!')
    #mb.showinfo('Информация', 'Вы выбрали второй вариант ответа!')
    #mb.showinfo('Информация', 'Вы выбрали третий вариант ответа!')

def show():
    s = f'{chk_state1.get()}'
    ss = f'{chk_state2.get()}'
    sss = f'{chk_state3.get()}'

chk_state1 = BooleanVar()
chk_state1.set(False) 
chk1 = Checkbutton(tab2, text='Первый', var=chk_state1, command=show)
chk1.grid(column=2, row=0) 

chk_state2 = BooleanVar()
chk_state2.set(False) 
chk2 = Checkbutton(tab2, text='Второй', var=chk_state2)
chk2.grid(column=3, row=0) 

chk_state3 = BooleanVar()
chk_state3.set(False) 
chk3 = Checkbutton(tab2, text='Третий', var=chk_state3)
chk3.grid(column=4, row=0) 

btn = Button(tab2, text="Сохранить выбор", command=clicked)
btn.grid(column=5, row=0)

tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Третья')
tab_control.pack(expand=1, fill='both')

window.mainloop()