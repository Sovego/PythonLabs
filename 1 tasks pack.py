import random
import math
import os


def first_task():
    suma = 0
    a = random.randint(100, 999)
    while a > 0:
        digit = a % 10
        suma = suma + digit
        a //= 10
    print(suma)


def second_task():
    suma = 0
    a = random.randint(1, 999)
    while a > 0:
        digit = a % 10
        suma = suma + digit
        a //= 10
    print(suma)


def third_task():
    radian = float(input('Radius of sphere: '))
    sur_area = 4 * math.pi * radian ** 2
    volume = (4 / 3) * (math.pi * radian ** 3)
    print("Surface Area is: ", sur_area)
    print("Volume is: ", volume)


def four_task():
    year = int(input("Input Year: "))
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        print("Regular")
    else:
        print("Leap")


def fifth_task():
    n = int(input("Input N: "))
    a = list(range(n + 1))
    a[1] = 0
    for i in range(2, n + 1):
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
    a = set(a)
    a.remove(0)
    print(a)


def sixth_task():
    balance = int(input("Input Balance: "))
    deadline = int(input("Input Deadline: "))
    for _ in range(deadline):
        a = balance / 100 * 10
        balance += a
    print("Total balance: ", balance)


def seventh_task():
    path = input("Input directory path: ")
    for root, dirs, files in os.walk(path):
        for filename in files:
            print(root+filename)
