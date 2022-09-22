from re import A
import tkinter as tk
import random

def rnd():
    a = pol1.get()
    b = pol2.get()
    t = random.randint(a = int(a),b= int(b))
    res.configure(text = t)

Window = tk.Tk()
Window.title("RandomizerMY")
Window.rowconfigure(0,minsize=150,weight=1)
Window.columnconfigure(1,minsize=150,weight=1)
Window.configure(bg='gray')

okno= tk.Frame(Window)
txt1 = tk.Label(okno, text= "От" ,bg="#857f71",fg="white" )
txt2 = tk.Label(okno, text= "До",bg="#857f71",fg= "white")
pol1 = tk.Entry(okno)
pol2 = tk.Entry(okno)
res = tk.Label(okno, text= "Результат")
btn = tk.Button(okno, text="Сгенерировать", command= rnd)

txt1.grid(row= 0, column= 0)
txt2.grid(row= 0,column= 2)
pol1.grid(row= 1,column=0)
pol2.grid(row= 1,column=2)
res.grid (row=1, column=1, pady=10)
btn.grid(row=3,column=1)
okno.grid(row=0,column=1)
okno.configure(bg="#857f71")

Window.mainloop()