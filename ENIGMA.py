from collections import deque
from curses.ascii import US

Rotors_1_P = deque([17, 21, 18, 10, 7, 19, 14, 13, 3, 12, 22, 23, 4, 2, 6, 25, 1, 9, 16, 8, 0, 11, 5, 24, 15, 20])
Rotors_2_P = deque([12, 23, 2, 17, 24, 21, 0, 16, 8, 18, 7, 25, 19, 4, 10, 22, 13, 1, 11, 6, 20, 5, 15, 14, 3, 9])
Rotors_3_P = deque([17, 8, 6, 1, 9, 15, 0, 20, 25, 24, 7, 4, 18, 11, 13, 19, 16, 23, 12, 21, 3, 2, 22, 14, 10, 5])

Reflector = [1, 0, 8, 6, 19, 7, 3, 5, 2, 10, 9, 13, 18, 11, 20, 16, 15, 22, 12, 4, 14, 24, 17, 25, 21, 23]

Rotors_3_N = deque([6, 3, 21, 20, 11, 25, 2, 10, 1, 4, 24, 13, 18, 14, 23, 5, 16, 0, 12, 15, 7, 19, 22, 17, 9, 8])
Rotors_2_N = deque([6, 17, 2, 24, 13, 21, 19, 10, 8, 25, 14, 18, 0, 16, 23, 22, 7, 3, 9, 12, 20, 5, 15, 1, 4, 11])
Rotors_1_N = deque([20, 16, 13, 8, 12, 22, 14, 4, 19, 17, 3, 21, 9, 7, 6, 24, 18, 0, 2, 5, 25, 1, 10, 11, 23, 15])


def limit(num):
    if num > 25:
        return num - 26
    elif num < 0:
        return num + 26
    else:
        return num


CODE = input("CODE:")

CODE1 = ord(CODE[0]) - 65
CODE2 = ord(CODE[1]) - 65
CODE3 = ord(CODE[2]) - 65

ENCODE = ""

print("-------------ENCODE-------------")

WORD = input("ENCO:")
for index in range(len(WORD)):

    if WORD[index] != ' ':
        ENCODE += chr(
            Rotors_1_N[limit(Rotors_2_N[limit(Rotors_3_N[limit(Reflector[limit(Rotors_3_P[limit(Rotors_2_P[limit(
                Rotors_1_P[ord(WORD[index]) - 65] + CODE1)] + CODE2)] + CODE3)] - CODE3)] - CODE2)] - CODE1)] + 65)

        CODE1 += 1
        if CODE1 > 25:
            CODE1 = 0
            CODE2 += 1
        if CODE2 > 25:
            CODE2 = 0
            CODE3 += 1
        if CODE3 > 25:
            CODE3 = 0
    else:
        ENCODE += ' '

print("DECO:" + ENCODE)

print("-------------DECODE-------------")

CODE1 = ord(CODE[0]) - 65
CODE2 = ord(CODE[1]) - 65
CODE3 = ord(CODE[2]) - 65

ENCODE = ""

WORD = input("ENCO:")
for index in range(len(WORD)):

    if WORD[index] != ' ':
        ENCODE += chr(
            Rotors_1_N[limit(Rotors_2_N[limit(Rotors_3_N[limit(Reflector[limit(Rotors_3_P[limit(Rotors_2_P[limit(
                Rotors_1_P[ord(WORD[index]) - 65] + CODE1)] + CODE2)] + CODE3)] - CODE3)] - CODE2)] - CODE1)] + 65)

        CODE1 += 1
        if CODE1 > 25:
            CODE1 = 0
            CODE2 += 1
        if CODE2 > 25:
            CODE2 = 0
            CODE3 += 1
        if CODE3 > 25:
            CODE3 = 0
    else:
        ENCODE += ' '

print("DECO:" + ENCODE)