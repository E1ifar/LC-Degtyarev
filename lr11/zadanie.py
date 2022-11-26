import json
import requests
from tkinter import *
from tkinter import ttk 
import tkinter.messagebox as mb

def funs():
    name = txt11.get('1.0', END).lower().strip()
    if name == "apache spark":

        response = requests.get("https://api.github.com/repos/apache/spark", auth=('E1ifar', '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'))
        data = response.json()
        
        output = dict()
        output['company'] = data.get('company')
        output['created_at'] = data.get("created_at")
        output['email'] = data.get("email")
        output['id'] = data.get("id")
        output['name'] = data.get("name")
        output['url'] = data.get("url")
    
        with open ('lr11\lfail.json', 'w') as file:
            json.dump(output, file)
    else:
        mb.showerror('Предупреждение', 'Неверно введено имя пользователя!')

window = Tk()
window.title("Дегтярев Антон Николаевич Уб-21")
window.geometry('320x200') 

tab_control = ttk.Notebook(window)

txt11 = Text(window, font=("Times New Romane", 8))
txt11.place(x = 10, y = 100, width=300, height=20)
txt11.focus_set()

btn1 = Button(window, text="Сохранить в файл", font=("Times New Romane", 8), command=funs)
btn1.place(x=110, y = 150, width=100, height=40)

lbl = Label(window, text="Введите: apache spark ", font=("Times New Romane", 14))
lbl.place(x=10, y = 10, width=310, height=50 )

window.mainloop()