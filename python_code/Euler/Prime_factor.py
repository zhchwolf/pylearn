#! /usr/bin/env python3
# -*- conding = utf-8 -*-

def is_prime(input_integer):
    isprime = 1
    if input_integer > 1:
        for a in range(2, input_integer):
            print("loop ",a)
            if input_integer % a == 0:
                print(input_integer, " is not prime. break")
                isprime=0
                break
    else:
        print("Please input number bigger than 1.")
    return isprime

def max_prime_factor( input_number):
#    prime_list = [2]
    for i in range(input_number, 2, -2):
        print(i)
        if is_prime(i) == 1:
            prime_list = i
            break
    return prime_list

#f = is_prime(50)
n = max_prime_factor(1475143)
#print(is_prime(97451))
print(n)
#m= max_prime_factor(600851475143)
#print(m)


array = [1, 2, 5, 3, 6, 8, 4]
for i in range(len(array) - 1, 0, -1):
    print(i)
    for j in range(0, i):
        print(j)
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print(array)