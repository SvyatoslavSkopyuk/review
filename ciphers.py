import argparse
import os
import random
import string
from collections import Counter

letters_en = string.ascii_lowercase
letters_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'


def get_args():
    """Считывание аргументов"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'cipher_type_or_app',
        type=str,
        default='0',
        help='Input type of cipher or app'
    )
    parser.add_argument(
        '--indir',
        type=str,
        default='0',
        help='Input dir for videos'
    )
    parser.add_argument(
        '--en_de',
        type=str,
        default='0',
        help='Encode or decode file'
    )
    parser.add_argument(
        '--key',
        type=str,
        default='0',
        help='Input step/key/seed for cipher'
    )
    parser.add_argument(
        '--outdir',
        type=str,
        default='0',
        help='Input dir for videos'
    )
    my_namespace = parser.parse_args()
    return my_namespace


def rand_key(seed, len_of_key):
    """
    Генерация псевдорандомного ключа с помощью сида
    :param seed: Сид для функции random.choise
    :param len_of_key: длина необходимого ключа
    :return:
    """
    global letters_en
    random.seed(seed)
    return ''.join(random.choice(letters_en) for i in range(len_of_key))


def caesar(args):
    """
    Шифратор/дешифратор Цезаря
    :param args: Все необходимые аргументы: indir, en_de, key, outdir
    :return: Зашифрованный/расшифрованный текст
    """
    global letters_en
    global letters_ru
    len_en = len(letters_en)
    len_ru = len(letters_ru)
    step = 0
    if args.en_de.lower() in ['e', 'en', 'encrypt']:
        step = int(args.key)
    if args.en_de.lower() in ['d', 'de', 'decrypt']:
        step = -1 * int(args.key)
    with open(args.indir, 'r') as usr_file:
        with open(args.outdir, 'w') as cipher:
            for line in usr_file.readlines():
                new_txt = ''
                for symbol in line.lower():
                    if symbol not in letters_en and symbol not in letters_ru:
                        new_txt += symbol
                    elif symbol in letters_ru:
                        new_txt += letters_ru[(letters_ru.find(symbol) + step) % len_ru]
                    else:
                        new_txt += letters_en[(letters_en.find(symbol) + step) % len_en]
                cipher.write(new_txt)
    return 'Result in ' + args.outdir


def vigenere(args):
    """
    Шифратор/дешифратор Вижнера
    :param args: Все необходимые аргументы: indir, en_de, key, outdir
    :return: Зашифрованный/расшифрованный текст
    """
    global letters_en
    global letters_ru
    len_en = len(letters_en)
    len_ru = len(letters_ru)
    if not args.key.isalpha():
        raise TypeError
    len_key = len(args.key)
    step = 0
    if args.en_de.lower() in ['e', 'en', 'encrypt']:
        step = 1
    if args.en_de.lower() in ['d', 'de', 'decrypt']:
        step = -1
    with open(args.indir, 'r') as usr_file:
        with open(args.outdir, 'w') as cipher:
            spase_couner = 0
            for line in usr_file.readlines():
                new_txt = ''
                for j, symbol in enumerate(line.lower()):
                    if symbol == ' ':
                        spase_couner += 1
                    if symbol not in letters_en and symbol not in letters_ru:
                        new_txt += symbol
                    elif symbol in letters_ru:
                        new_txt += letters_ru[
                            (letters_ru.find(symbol) + step * letters_ru.find(
                                args.key[(j - spase_couner) % len_key])) % len_ru]
                    else:
                        new_txt += letters_en[
                            (letters_en.find(symbol) + step * letters_en.find(
                                args.key[(j - spase_couner) % len_key])) % len_en]
                cipher.write(new_txt)
    return 'Result in ' + args.outdir


def vernam(args):
    """
    Шифратор/дешифратор Вернама
    :param args: Все необходимые аргументы: indir, en_de, key, outdir
    :return: Зашифрованный/расшифрованный текст
    """
    global letters_en
    global letters_ru
    len_en = len(letters_en)
    len_ru = len(letters_ru)
    step = 0
    if args.en_de in ['e', 'en', 'encrypt']:
        step = 1
    if args.en_de in ['d', 'de', 'decrypt']:
        step = -1
    gen_str = rand_key(args.key, os.stat(args.indir).st_size)
    with open(args.indir, 'r') as usr_file:
        with open(args.outdir, 'w') as cipher:
            spase_couner = 0
            for line in usr_file.readlines():
                new_txt = ''
                for j, symbol in enumerate(line.lower()):
                    if symbol == ' ':
                        spase_couner += 1
                    if symbol not in letters_en and symbol not in letters_ru:
                        new_txt += symbol
                    elif symbol in letters_ru:
                        new_txt += letters_ru[
                            (letters_ru.find(symbol) + step * letters_en.find(gen_str[j - spase_couner])) % len_ru]
                    else:
                        new_txt += letters_en[
                            (letters_en.find(symbol) + step * letters_en.find(gen_str[j - spase_couner])) % len_en]
                cipher.write(new_txt)
    return 'Result in ' + args.outdir


def caesar_crack(args):
    """
        автовзлом шифра Цезаря(частотный анализ)
        :param args: Все необходимые аргументы: indir, outdir
        :return: Расшифрованный текст
        """
    global letters_en
    global letters_ru
    with open(args.indir, 'r') as file:
        ammount = Counter()
        for line in file.readlines():
            ammount += Counter(line)
    try:
        most_c = ammount.most_common(1)[0][0]
    except IndexError:
        return 'Empty file'
    if most_c == ' ':
        most_c = ammount.most_common(2)[1][0]
    if most_c in letters_ru:
        args.key = letters_ru.find(most_c) - letters_ru.find('о')
    elif most_c in letters_en:
        args.key = letters_en.find(most_c) - letters_en.find('e')
    else:
        return 'Too many special characters'
    args.en_de = 'de'
    return caesar(args)


def res(user_params):
    """
    Исполнение задачи, поставленной пользователем
    :param user_params: Аргументы пользователя
    :return: Вывод результата работы шифрофункций
    """
    try:
        result = eval(user_params.cipher_type_or_app.lower())(user_params)
    except IndexError:
        result = 'Wrong input'
    return result
