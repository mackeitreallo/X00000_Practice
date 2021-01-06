n = int(input("\nCheck this number: "))

def prime_checker(number = n):
    if number % 2 != 0:
        print("\nIts a prime number.")
    else:
        print("\nNot a prime number.")

prime_checker(number = n)