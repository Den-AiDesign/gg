def hangman(word):
    wrong = 0
    stages = ['',
              ' _________          ',
              ' |                  ',
              ' |        |         ',
              ' |        0         ',
              ' |      / | \       ',
              ' |       / \        ',
              ' |                  '
                ]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('Добро пожаловать на казнь!')
    while wrong < len(stages) - 1:
        print('\n')
        msg = 'Введите букву: '
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((' '.join(board)))
        e = wrong + 1
        print('\n'.join(stages[0: e]))
        if '_' not in board:
            print('Вы выйграли! Было загадано слово: ')
            print(' '.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong]))
        print('Вы проиграли! Было загадано слово: {}.'.format(word))

import nltk

nltk.download('stopwords')
nltk.download('words')

import random

from nltk.corpus import words

russian_words = words.words('ru')

random_word = random.choice(russian_words)
'''
with open('/home/wolf/.cursor-tutor/projects/book/Виселица/russian.txt', 'r', encoding='latin-1') as f:
    lines = f.readlines()
    
word_list = [line.strip() for line in lines]

ran_word = random.choice(word_list)
'''

hangman(russian_words)