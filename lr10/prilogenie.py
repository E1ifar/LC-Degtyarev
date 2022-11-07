from tkinter import *
from tkinter import ttk 

window = Tk()
window.title("Дегтярев Антон Николаевич Уб-21")
window.geometry('700x500') 

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Первая')

tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Вторая')

tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Третья', row=7)
tab_control.pack(expand=1, fill='both')


window.mainloop()