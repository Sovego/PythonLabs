import random


def first_task():
    stri = input("Input string: ")
    if stri == stri[::-1]:
        print("Palindrome")
    else:
        print("No Palindrome")


def second_task():
    stri = input("Input string: ")
    word_list = stri.split(" ")
    max_word = ""
    for s in word_list:
        if len(max_word) < len(s):
            max_word = s
    print(max_word)


def third_task():
    a_list = [random.randint(0, 10000) for i in range(205)]
    even = 0
    odd = 0
    for a in a_list:
        if a % 2 == 0:
            even += 1
        else:
            odd += 1
    print(a_list, "\n", "Even: ", even, "\n", "Odd: ", odd)


def four_task():
    stri = input("Input Keys for dictionary (sep space): ")
    key_list = stri.split(" ")
    stri = input("Input Values for dictionary (sep space): ")
    value_list = stri.split(" ")
    dictionary = dict(zip(key_list, value_list))
    print(dictionary)
    stri = input("Input string: ")
    word_list = stri.split(" ")
    out_str = ""
    for word in word_list:
        if dictionary.get(word) is None:
            out_str += word + " "
        else:
            out_str += str(dictionary.get(word)) + " "
    print(out_str)


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def sixth_task():
    file = open("input.txt", "r")
    stri = file.read()
    word_list = stri.split(" ")
    print("Word count: ", len(word_list))
    #print("Char count: ",sum([b for b in [len(a for a in word_list)]]))

sixth_task()