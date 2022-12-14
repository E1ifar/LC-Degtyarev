from tkinter import *
from tkinter import ttk 
from tkinter.ttk import Checkbutton
import tkinter.messagebox as mb
from tkinter.ttk import Combobox
from tkinter import filedialog
from tkinter import Menu

window = Tk()
window.title("Дегтярев Антон Николаевич Уб-21")
window.geometry('1000x500') 

#первая вкладка

tab1_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab1_control)
tab1_control.add(tab1, text='Калькулятор')
tab1_control.place(x=0, y=0, width=450, height=250)

def vichisleniya():
    a=combo.get()
    b=int(txt1.get())
    c=int(txt2.get())
    if a == '-':
        l=b-c
        lbl.configure(text=l)
    elif a == '+':
        l=b+c
        lbl.configure(text=l)
    elif a == '*':
        l=b*c
        lbl.configure(text=l)
    elif a== '/':
        if c==0:
            mb.showerror('Предупреждение', 'На ноль делить нельзя!')
        else:        
            l=b/c
            lbl.configure(text=l)

txt1 = Entry(tab1, justify=CENTER,  font=("Times New Romane", 30))
txt1.place(x = 10, y = 10, width=100, height=50,)

combo = Combobox(tab1, font=("Times New Romane", 20))
combo.place(x=120, y = 15, width=50, height=40)
combo['values'] = ('+', '-', '*', '/')

txt2 = Entry(tab1, justify=CENTER,  font=("Times New Romane", 30))
txt2.place(x = 180, y = 10, width=100, height=50)

btn1 = Button(tab1, text="=", font=("Times New Romane", 30), command=vichisleniya)
btn1.place(x=290, y = 15, width=50, height=40)

lbl = Label(tab1, text="", font=("Times New Romane", 30))
lbl.place(x=350, y = 10, width=100, height=50 )

#вторая вкладка

tab2_control = ttk.Notebook(window)
tab2 = ttk.Frame(tab2_control)
tab2_control.add(tab2, text='Флажки')
tab2_control.place(x=0, y=250, width=450, height=250)

def clicked():
    a=chk_state1.get()
    if a == True:
        mb.showinfo('Информация', 'Вы выбрали первый вариант ответа!')
    b=chk_state2.get()
    if b == True:
        mb.showinfo('Информация', 'Вы выбрали второй вариант ответа!')
    c=chk_state3.get()
    if c == True:
        mb.showinfo('Информация', 'Вы выбрали третий вариант ответа!')
    if a != True and b != True and c!= True:
        mb.showwarning('Предупреждение', ' Вы не выбрали ни один вариант ответа!!!')

chk_state1 = BooleanVar()
chk_state1.set(0) 
chk1 = Checkbutton(tab2, text='Первый', var=chk_state1, onvalue=1, offvalue=0,)
chk1.grid(column=2, row=0)

chk_state2 = BooleanVar()
chk_state2.set(0) 
chk2 = Checkbutton(tab2, text='Второй', var=chk_state2, onvalue=1, offvalue=0)
chk2.grid(column=3, row=0) 

chk_state3 = BooleanVar()
chk_state3.set(0) 
chk3 = Checkbutton(tab2, text='Третий', var=chk_state3, onvalue=1, offvalue=0)
chk3.grid(column=4, row=0) 

btn = Button(tab2, text="Сохранить выбор", command=clicked)
btn.grid(column=5, row=0)

#третья вкладка
def clicked():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r", encoding="UTF-8") as file:
            text =file.read()
            txt11.insert("1.0", text)

tab3_control = ttk.Notebook(window)
tab3 = ttk.Frame(tab3_control)
tab3_control.add(tab3, text='Текст')
tab3_control.place(x=475, y=0, width=500, height=500)

txt11 = Text(tab3, font=("Times New Romane", 14))
txt11.place(x = 10, y = 10, width=480, height=450)
txt11.focus_set()

maimenu = Menu(window)

filemenu = Menu(maimenu, tearoff=0)
filemenu.add_command(label="Открыть...", command=clicked)

maimenu.add_cascade(label="Файл", menu=filemenu)
window.config(menu=maimenu) 

window.mainloop()