import string
import tkinter
from tkinter import messagebox
from tkinter import ttk

letters = string.ascii_lowercase
letters_len = len(letters)
font = ('Arial Bold', 20)
encrypt_decrypt = ('Зашифровать', 'Расшифровать')
first_block_info = ['Шифр Цезаря', 0, 0, 0, 2, 0, 1, 2, 0, 2, 2, 'с шагом', 1, 0, 3, 1, 3, 'caesar', 0, 4]
second_block_info = ['Шифр Виженера', 0, 7, 0, 2, 7, 1, 2, 7, 2, 2, 'с ключом', 1, 7, 3, 8, 3, 'vigenere', 7, 4]
third_block_info = ['Шифр Вернама', 0, 0, 6, 2, 0, 7, 2, 0, 8, 2, 'с шагом', 1, 0, 9, 1, 9, 'vernam', 0, 10]


def to_caesar_en():
    """
    Шифр Цезаря(шифровка/расшифровка)
    :return: Зашифрованное/расшифрованное сообщение
    """
    usage = combo1.get().lower()
    input_text = txt1.get(1.0, tkinter.END).lower()
    try:
        step = int(step1.get())
    except ValueError:
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


def to_vigenere_en():
    """
    Шифр Виженера(шифровка/расшифровка)
    :return: Зашифрованное/расшифрованное сообщение
    """
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


def to_vernam_en():
    """
    Шифр Вернама(шифровка/расшифровка)
    :return: Зашифрованное/расшифрованное сообщение
    """
    usage = combo3.get().lower()
    input_text = txt3.get(1.0, tkinter.END).lower()
    key = step3.get().lower()
    flag = 1
    if len(key) != len(input_text) - 1:
        tkinter.messagebox.showerror('Error', 'Wrong input')
        return
    if usage == 'Расшифровать':
        flag *= -1
    global letters
    global letters_len
    output_text = ''
    for i, letter in enumerate(input_text):
        if letter not in letters:
            output_text += letter
        else:
            output_text += letters[(letters.find(letter) + flag * letters.find(key[i])) % letters_len]
    tkinter.messagebox.showinfo('Result', output_text)


def create_button(cmd):
    """
    Создание кнопки
    :param cmd: Название используемой команды(шифра)
    :return: Создана кнопка
    """
    if cmd == 'caesar':
        return tkinter.Button(window, text='Начать', command=to_caesar_en)
    elif cmd == 'vigenere':
        return tkinter.Button(window, text='Начать', command=to_vigenere_en)
    elif cmd == 'vernam':
        return tkinter.Button(window, text='Начать', command=to_vernam_en)


def create_combobox():
    """
        Создание поля выбора
        :return: Создано поле выбора
        """
    global font
    return ttk.Combobox(window, text='Зашифровать', font=font)


def create_entry():
    """
        Создание поля ввода
        :return: Создано поле ввода
        """
    return tkinter.Entry(window, width=10)


def create_label(text, font_usage=0):
    """
    Создание текстового поля
    :param text: текст в поле
    :param font_usage: не использавать форматирование/использавать форматирование
    :return:
    """
    if font_usage == 1:
        global font
        name = tkinter.Label(window, text=text, font=font)
        return name
    name = tkinter.Label(window, text=text)
    return name


def create_text():
    """
    Создание строки ввода
    :return: Создана строка ввода
    """
    return tkinter.Text(window, width=50, height=10, wrap=tkinter.WORD)


def grid_button(cmd, col, row, cols=1, rows=1):
    """
    Расположение кнопки на окне
    :param cmd: команда кнопки
    :param col: column
    :param row: row
    :param cols: columnspan
    :param rows: rowspan
    :return: Кнопка создана и расположена на окне
    """
    name = create_button(cmd)
    name.grid(column=col, row=row, columnspan=cols, rowspan=rows)
    return name


def grid_combobox(col, row, cols=1, rows=1):
    """
    Расположение combobox на окне
    :param col: column
    :param row: row
    :param cols: columnspan
    :param rows: rowspan
    :return: Combobox создан и расположен на окне
    """
    name = create_combobox()
    name['values'] = encrypt_decrypt
    name.current(0)
    name.grid(column=col, row=row, columnspan=cols, rowspan=rows)
    return name


def grid_entry(col, row, cols=1, rows=1):
    """
    Расположение поля ввода на окне
    :param col: column
    :param row: row
    :param cols: columnspan
    :param rows: rowspan
    :return: Поле ввода создано и расположено на окне
    """
    name = create_entry()
    name.grid(column=col, row=row, columnspan=cols, rowspan=rows)
    return name


def grid_label(text, font_usage, col, row, cols=1, rows=1):
    """
    Расположение combobox на окне
    :param text: текст в поле
    :param font_usage: не использавать форматирование/использавать форматирование
    :param col: column
    :param row: row
    :param cols: columnspan
    :param rows: rowspan
    :return: Combobox создан и расположен на окне
    """
    name = create_label(text, font_usage)
    name.grid(column=col, row=row, columnspan=cols, rowspan=rows)
    print(type(name))
    return name


def grid_text(col, row, colsp=1, rowsp=1):
    """
    Расположение поля ввода на окне
    :param col: column
    :param row: row
    :param cols: columnspan
    :param rows: rowspan
    :return: Поле ввода создано и расположено на окне
    """
    name = create_text()
    name.grid(column=col, row=row, columnspan=colsp, rowspan=rowsp)
    return name


def create_block(block_info, whitespace=False):
    """
    Сокзание блока в окне
    :param block_info: Необходимые данные для создания и расположения элементов
    :param whitespace: Отсутствие/наличие отступа
    :return: Блок создан на окне
    """
    name = grid_label(*block_info[:5])
    combo = grid_combobox(*block_info[5:8])
    txt = grid_text(*block_info[8:11])
    lbl = grid_label(*block_info[11:15])
    step = grid_entry(*block_info[15:17])
    btn = grid_button(*block_info[17:])
    if whitespace:
        # Разделитель между блоками
        grid_label('                          ', 0, 3, 0, 4, 4)
    return name, combo, txt, lbl, step, btn


# Создание окна
window = tkinter.Tk()
window.title('Ciphers')
window.geometry('950x600+100+50')
window.resizable(False, False)

# Блоки с шифрами  Цезаряб Виженера и Вернама
name1, combo1, txt1, lbl1, step1, btn1 = create_block(first_block_info, True)
name2, combo2, txt2, lbl2, step2, btn2 = create_block(second_block_info)
name3, combo3, txt3, lbl3, step3, btn3 = create_block(third_block_info)
