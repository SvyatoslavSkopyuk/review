import tkinter
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
'''Только набросок'''

def to_Caesar_en():
    usage = combo1.get().lower()
    strk = txt1.get(1.0, tkinter.END).lower()
    try:
        stepp = int(step1.get())
    except:
        tkinter.messagebox.showerror("Error", "Wrong input")
        return
    if usage == "Расшифровать":
        stepp *= -1
    dec = 'abcdefghijklmnopqrstuvwxyz'
    len_d = len(dec)
    new_strk = ''
    for i in strk:
        if i not in dec:
            new_strk += i
        else:
            new_strk += dec[(dec.find(i) + stepp) % len_d]
    tkinter.messagebox.showinfo("Result", new_strk)


def to_Vigenere_en():
    usage = combo2.get().lower()
    strk = txt2.get(1.0, tkinter.END).lower()
    keyy = (step2.get()).lower()
    flag = 1
    if not keyy.isalpha():
        tkinter.messagebox.showerror("Error", "Wrong input")
        return
    len_k = len(keyy)
    if usage == "Расшифровать":
        flag *= -1
    dec = 'abcdefghijklmnopqrstuvwxyz'
    len_d = len(dec)
    new_strk = ''
    for j, i in enumerate(strk):
        if i not in dec:
            new_strk += i
        else:
            new_strk += dec[(dec.find(i) + flag * dec.find(keyy[j % len_k])) % len_d]
    tkinter.messagebox.showinfo("Result", new_strk)


def to_Vernam_en():
    usage = combo3.get().lower()
    strk = txt3.get(1.0, tkinter.END).lower()
    keyy = step3.get().lower()
    flag = 1
    if len(keyy) != len(strk) - 1:
        tkinter.messagebox.showerror("Error", "Wrong input")
        return
    len_k = len(keyy)
    if usage == "Расшифровать":
        flag *= -1
    dec = 'abcdefghijklmnopqrstuvwxyz'
    len_d = len(dec)
    new_strk = ''
    for j, i in enumerate(strk):
        if i not in dec:
            new_strk += i
        else:
            new_strk += dec[(dec.find(i) + flag * dec.find(keyy[j])) % len_d]
    tkinter.messagebox.showinfo("Result", new_strk)


window = tkinter.Tk()
window.title("Недоделано")
window.geometry('950x600')

name1 = tkinter.Label(window, text="Шифр Цезаря")
name1.grid(column=0, row=0, columnspan=2)
combo1 = ttk.Combobox(window, text="Зашифровать", font=("Arial Bold", 20))
combo1['values'] = ("Зашифровать", "Расшифровать")
combo1.current(0)
combo1.grid(column=0, row=1, columnspan=2)
txt1 = tkinter.Text(window, width=50, height=10, wrap=tkinter.WORD)
txt1.grid(column=0, row=2, columnspan=2)
lbl1 = tkinter.Label(window, text="с шагом", font=("Arial bold", 20))
lbl1.grid(column=0, row=3)
step1 = tkinter.Entry(window, width=10)
step1.grid(column=1, row=3)
btn1 = tkinter.Button(window, text="Начать", command=to_Caesar_en)
btn1.grid(column=0, row=4)

whitespace1 = tkinter.Label(window, text='                          ')
whitespace1.grid(column=3, row=0, rowspan=4, columnspan=4)

name2 = tkinter.Label(window, text="Шифр Виженера")
name2.grid(column=7, row=0, columnspan=2)
combo2 = ttk.Combobox(window, text="Зашифровать", font=("Arial Bold", 20))
combo2['values'] = ("Зашифровать", "Расшифровать")
combo2.current(0)
combo2.grid(column=7, row=1, columnspan=2)
txt2 = tkinter.Text(window, width=50, height=10, wrap=tkinter.WORD)
txt2.grid(column=7, row=2, columnspan=2)
lbl2 = tkinter.Label(window, text="с ключом", font=("Arial bold", 20))
lbl2.grid(column=7, row=3)
step2 = tkinter.Entry(window, width=20)
step2.grid(column=8, row=3)
btn2 = tkinter.Button(window, text="Начать", command=to_Vigenere_en)
btn2.grid(column=7, row=4)

name3 = tkinter.Label(window, text="Шифр Вернама")
name3.grid(column=0, row=6, columnspan=2)
combo3 = ttk.Combobox(window, text="Зашифровать", font=("Arial Bold", 20))
combo3['values'] = ("Зашифровать", "Расшифровать")
combo3.current(0)
combo3.grid(column=0, row=7, columnspan=2)
txt3 = tkinter.Text(window, width=50, height=10, wrap=tkinter.WORD)
txt3.grid(column=0, row=8, columnspan=2)
lbl3 = tkinter.Label(window, text="с кодом", font=("Arial bold", 20))
lbl3.grid(column=0, row=9)
step3 = tkinter.Entry(window, width=10)
step3.grid(column=1, row=9)
btn3 = tkinter.Button(window, text="Начать", command=to_Vernam_en)
btn3.grid(column=0, row=10)
