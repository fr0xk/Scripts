from typing import List
from math import gcd


def prime_factors(n: int) -> List[int]:
    """Returns a list of prime factors of a given number n"""
    def factors(n: int, i: int) -> List[int]:
        if i * i > n:
            return [n] if n > 1 else []
        elif n % i == 0:
            return [i] + factors(n // i, i)
        else:
            return factors(n, i + 1)

    return factors(abs(n), 2)


def hcf(a: int, b: int) -> int:
    """Returns the highest common factor of two numbers a and b"""
    return abs(a) if b == 0 else hcf(b, a % b)


def lcm(a: int, b: int) -> int:
    """Returns the lowest common multiple of two numbers a and b"""
    return abs(a * b) // gcd(a, b)


def read_int(prompt: str) -> int:
    """Reads an integer from user input with the given prompt"""
    while True:
        try:
            num: int = int(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter an integer.")


if __name__ == '__main__':
    num1: int = read_int("Enter first number: ")
    num2: int = read_int("Enter second number: ")
    pf1: List[int] = prime_factors(num1)
    hcf_val: int = hcf(num1, num2)
    lcm_val: int = lcm(num1, num2)
    pf2: List[int] = prime_factors(num2)
    print(f"Prime factors of {num1}: {pf1}")
    print(f"HCF of {num1} and {num2}: {hcf_val}")
    print(f"LCM of {num1} and {num2}: {lcm_val}\n")
    
