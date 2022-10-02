"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError
    num = 2
    count = 1
    list = []
    while count <= number_of_primes:
        flag = False
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
        if not flag:
            list.append(num)
            count += 1
        num += 1

    return list

