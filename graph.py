import string
import tkinter
from tkinter import messagebox
from tkinter import ttk

letters = string.ascii_lowercase
letters_len = len(letters)
font = ('Arial Bold', 20)
encrypt_decrypt = ('Зашифровать', 'Расшифровать')


# Шифр Цезаря(шифровка/расшифровка)
def to_Caesar_en():
    usage = combo1.get().lower()
    input_text = txt1.get(1.0, tkinter.END).lower()
    try:
        step = int(step1.get())
    except:
        tkinter.messagebox.showerror('Error', 'Wrong input')
        return
    if usage == 'Расшифровать':
        step *= -1
    global letters
    global letters_len
    output_text = ''
    for letter in input_text:
        if letter not in letters:
            output_text += letter
        else:
            output_text += letters[(letters.find(letter) + step) % letters_len]
    tkinter.messagebox.showinfo('Result', output_text)


# Шифр Виженера(шифровка/расшифровка)
def to_Vigenere_en():
    usage = combo2.get().lower()
    input_text = txt2.get(1.0, tkinter.END).lower()
    keyy = (step2.get()).lower()
    flag = 1
    if not keyy.isalpha():
        tkinter.messagebox.showerror('Error', 'Wrong input')
        return
    len_k = len(keyy)
    if usage == 'Расшифровать':
        flag *= -1
    global letters
    global letters_len
    output_text = ''
    for j, letter in enumerate(input_text):
        if letter not in letters:
            output_text += letter
        else:
            output_text += letters[(letters.find(letter) + flag * letters.find(keyy[j % len_k])) % letters_len]
    tkinter.messagebox.showinfo('Result', output_text)


# Шифр Вернама(шифровка/расшифровка)
def to_Vernam_en():
    usage = combo3.get().lower()
    input_text = txt3.get(1.0, tkinter.END).lower()
    keyy = step3.get().lower()
    flag = 1
    if len(keyy) != len(input_text) - 1:
        tkinter.messagebox.showerror('Error', 'Wrong input')
        return
    len_k = len(keyy)
    if usage == 'Расшифровать':
        flag *= -1
    global letters
    global letters_len
    output_text = ''
    for j, letter in enumerate(input_text):
        if letter not in letters:
            output_text += letter
        else:
            output_text += letters[(letters.find(letter) + flag * letters.find(keyy[j])) % letters_len]
    tkinter.messagebox.showinfo('Result', output_text)


def create_button(cmd):
    if cmd == 'caesar':
        return tkinter.Button(window, text='Начать', command=to_Caesar_en)
    elif cmd == 'vigenere':
        return tkinter.Button(window, text='Начать', command=to_Vigenere_en)
    elif cmd == 'vernam':
        return tkinter.Button(window, text='Начать', command=to_Vernam_en)


def create_combobox():
    global font
    return ttk.Combobox(window, text='Зашифровать', font=font)


def create_entry():
    return tkinter.Entry(window, width=10)


def create_label(text, font_usage=0):
    if font_usage == 1:
        global font
        return tkinter.Label(window, text=text, font=font)
    return tkinter.Label(window, text=text)


def create_text():
    return tkinter.Text(window, width=50, height=10, wrap=tkinter.WORD)


# Создание окна
window = tkinter.Tk()
window.title('Ciphers')
window.geometry('950x600+100+50')
window.resizable(False, False)

# Блок с шифром Цезаря
name1 = create_label('Шифр Цезаря')
name1.grid(column=0, row=0, columnspan=2)
combo1 = create_combobox()
combo1['values'] = encrypt_decrypt
combo1.current(0)
combo1.grid(column=0, row=1, columnspan=2)
txt1 = create_text()
txt1.grid(column=0, row=2, columnspan=2)
lbl1 = create_label('с шагом', 1)
lbl1.grid(column=0, row=3)
step1 = create_entry()
step1.grid(column=1, row=3)
btn1 = create_button('caesar')
btn1.grid(column=0, row=4)

# Разделитель между блоками
whitespace1 = create_label('                          ')
whitespace1.grid(column=3, row=0, rowspan=4, columnspan=4)

# Блок с шифром Виженера
name2 = create_label('Шифр Виженера')
name2.grid(column=7, row=0, columnspan=2)
combo2 = create_combobox()
combo2['values'] = encrypt_decrypt
combo2.current(0)
combo2.grid(column=7, row=1, columnspan=2)
txt2 = create_text()
txt2.grid(column=7, row=2, columnspan=2)
lbl2 = create_label('с ключом', 1)
lbl2.grid(column=7, row=3)
step2 = create_entry()
step2.grid(column=8, row=3)
btn2 = create_button('vigenere')
btn2.grid(column=7, row=4)

# Блок с шифром Вернама
name3 = create_label('Шифр Вернама')
name3.grid(column=0, row=6, columnspan=2)
combo3 = create_combobox()
combo3['values'] = encrypt_decrypt
combo3.current(0)
combo3.grid(column=0, row=7, columnspan=2)
txt3 = create_text()
txt3.grid(column=0, row=8, columnspan=2)
lbl3 = create_label('с шагом', 1)
lbl3.grid(column=0, row=9)
step3 = create_entry()
step3.grid(column=1, row=9)
btn3 = create_button('vernam')
btn3.grid(column=0, row=10)
