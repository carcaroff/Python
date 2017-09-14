from random import randint
import string

lista1 = [x for x in range(300)]


lista2 = [randint(0, 5000000) for x in range(500)]


lista3 = [randint(0, 5000000) for x in range(50000)]


# test 1


def find_number(num):
    
    if  0 <= num < 300 :
        print("O número informado está presente no Array, na posição: ", num)
        return lista1[num]
    else:
        print("O número informado não está presente no array")


# test 2


def sort_list(list):
    return list.sort


def number_matches(list1, list2):
    sort_list(lista2)
    sort_list(lista3)
    match = []
    for i in range (0 , len(lista3)):
        if lista3[i] in lista2 :
            match.append(lista3[i])
    return match


# test 3



def prime_numbers(num):
    num1 = abs(num)
    prime_array = []
    if num1 < 1:
        return prime_array
    if num1 >= 2:
        prime_array.append(2)
    for i in range(3, num1):
        if is_prime(i, prime_array):
            prime_array.append(i)
    prime_array = [1] + prime_array
    return prime_array


def is_prime(number, num_array):
    for n in num_array:
        if number % n == 0:
            return False
    return True


# test 4

def prime_word(word):
    return is_prime2(word_value(word))

def word_value(word):
    alphabet = string.ascii_letters
    sum = 0
    for char in word:
        for x in range(0, len(alphabet)):
            if char == alphabet[x]:
                sum += x + 1
    return sum

def is_prime2(num):
    if num == 1:
        return True
    for i in range (2, num):
        if num % i == 0:
            return False
    return True
