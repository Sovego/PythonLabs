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
    a_list = [random.randint(0, 10000) for _ in range(205)]
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
    out_str = "".join(
        f"{word} "
        if dictionary.get(word) is None
        else f"{str(dictionary.get(word))} "
        for word in word_list
    )
    print(out_str)


def fib(n):
    return n if n <= 1 else fib(n - 1) + fib(n - 2)


def sixth_task():
    file = open("input.txt", "r")
    stri = file.read()
    word_list = stri.split(" ")
    print("Words count: ", len(word_list))
    abc_count = sum(1 for a in stri if a.isalpha)
    print("Letters count: ", abc_count)
    print("Strings count: ", stri.count("\n"))


def generator(n, q, x):
    for _ in range(n):
        yield x
        x*=q



def seventh_task():
    x = int(input("Input first number: "))
    q = int(input("Input generator step: "))
    n = int(input("Input count of elements: "))
    res = list(generator(n, q, x))
    print(res)


seventh_task()
