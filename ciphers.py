import os
import random
import string
from collections import Counter

letters_en = string.ascii_lowercase
letters_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'


def get_args():
    '''Считывание аргументов'''
    ars = input().split()
    if len(ars) < 5:
        ars += [0, 0, 0, 0, 0]
    return ars[:5]


def rand_key(seed, l):
    '''Генерация псевдорандомного ключа с помощью сида'''
    random.seed(seed)
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(l))


def caesar(args):
    '''Шифратор/дешифратор Цезаря'''
    global letters_en
    global letters_ru
    len_en = len(letters_en)
    len_ru = len(letters_ru)
    if args[1].lower() in ['e', 'en', 'encrypt']:
        step = int(args[2])
    if args[1].lower() in ['d', 'de', 'decrypt']:
        step = -1 * int(args[2])
    try:
        usr_file = open(args[0], 'r')
    except:
        return 'No such file'
    with open(args[3], 'w') as cipher:
        for line in usr_file.readlines():
            new_txt = ''
            for i in line.lower():
                if i not in letters_en and i not in letters_ru:
                    new_txt += i
                elif i in letters_ru:
                    new_txt += letters_ru[(letters_ru.find(i) + step) % len_ru]
                else:
                    new_txt += letters_en[(letters_en.find(i) + step) % len_en]
            cipher.write(new_txt)
    usr_file.close()
    return 'Result in ' + args[3]


def vigenere(args):
    '''Шифратор/дешифратор Вижнера'''
    global letters_en
    global letters_ru
    len_en = len(letters_en)
    len_ru = len(letters_ru)
    if not args[2].isalpha():
        raise TypeError
    len_key = len(args[2])
    if args[1].lower() in ['e', 'en', 'encrypt']:
        step = 1
    if args[1].lower() in ['d', 'de', 'decrypt']:
        step = -1
    try:
        usr_file = open(args[0], 'r')
    except:
        return 'No such file'
    with open(args[3], 'w') as cipher:
        spase_couner = 0
        for line in usr_file.readlines():
            new_txt = ''
            for j, i in enumerate(line.lower()):
                if i == ' ':
                    spase_couner += 1
                if i not in letters_en and i not in letters_ru:
                    new_txt += i
                elif i in letters_ru:
                    new_txt += letters_ru[
                        (letters_ru.find(i) + step * letters_ru.find(args[2][(j - spase_couner) % len_key])) % len_ru]
                else:
                    new_txt += letters_en[
                        (letters_en.find(i) + step * letters_en.find(args[2][(j - spase_couner) % len_key])) % len_en]
            cipher.write(new_txt)
    usr_file.close()
    return 'Result in ' + args[3]


def vernam(args):
    '''Шифратор/дешифратор Вернама'''
    global letters_en
    global letters_ru
    len_en = len(letters_en)
    len_ru = len(letters_ru)
    if args[1] in ['e', 'en', 'encrypt']:
        step = 1
    if args[1] in ['d', 'de', 'decrypt']:
        step = -1
    gen_str = rand_key(args[2], os.stat(args[0]).st_size)
    try:
        usr_file = open(args[0], 'r')
    except:
        return 'No such file'
    with open(args[3], 'w') as cipher:
        spase_couner = 0
        for line in usr_file.readlines():
            new_txt = ''
            if i == ' ':
                spase_couner += 1
            for j, i in enumerate(line.lower()):
                if i not in letters_en and i not in letters_ru:
                    new_txt += i
                elif i in letters_ru:
                    new_txt += letters_ru[(letters_ru.find(i) + step * letters_en.find(gen_str[j - spase_couner])) % len_ru]
                else:
                    new_txt += letters_en[(letters_en.find(i) + step * letters_en.find(gen_str[j - spase_couner])) % len_en]
            cipher.write(new_txt)
    usr_file.close()
    return 'Result in ' + args[3]


def caesar_crack(args):
    '''автовзлом шифра Цезаря(частотный анализ)'''
    global letters_en
    global letters_ru
    with open(args[0], 'r') as file:
        ammount = Counter()
        for line in file.readlines():
            ammount += Counter(line)
    most_c = ammount.most_common(1)[0][0]
    if most_c == ' ':
        most_c = ammount.most_common(2)[1][0]
    if most_c in letters_ru:
        step = letters_ru.find(most_c) - letters_ru.find('о')
    elif most_c in letters_en:
        step = letters_en.find(most_c) - letters_en.find('e')
    else:
        return 'Too many special characters'
    return caesar([args[0], 'de', step, args[1]])


def res(ch):
    '''Вывод результата'''
    try:
        result = eval(ch[0].lower())(ch[1:])
    except:
        result = 'Wrong input'
    return result
