from typing import List, Tuple

import math

def prime_factors(n: int) -> List[int]:

    """Returns a list of prime factors of a given number."""

    factors = []

    i = 2

    while i <= n:

        if n % i == 0:

            factors.append(i)

            n //= i

        else:

            i += 1

    return factors

def hcf(a: int, b: int) -> int:

    """Returns the highest common factor of two numbers."""

    while b != 0:

        a, b = b, a % b

    return a

def lcm(a: int, b: int) -> int:

    """Returns the lowest common multiple of two numbers."""

    return a * b // hcf(a, b)

def hcf_lcm(numbers: List[int]) -> Tuple[int, int]:

    """Returns the highest common factor and lowest common multiple of a list of numbers."""

    if not numbers:

        return 0, 0

    elif len(numbers) == 1:

        return numbers[0], numbers[0]

    else:

        hcf_val = numbers[0]

        lcm_val = numbers[0]

        for n in numbers[1:]:

            hcf_val = hcf(hcf_val, n)

            lcm_val = lcm(lcm_val, n)

        return hcf_val, lcm_val

def get_numbers() -> List[int]:

    """Prompts the user to enter a list of integers and returns the list."""

    numbers = []

    while True:

        try:

            n = int(input("Enter a number (or 0 to stop): "))

            if n == 0:

                return numbers

            else:

                numbers.append(n)

        except ValueError:

            print("Invalid input. Please enter a valid integer.")

def main() -> None:

    """Main function that prompts the user for input and prints prime factors, HCF, and LCM."""

    numbers = get_numbers()

    for n in numbers:

        factors = prime_factors(n)

        hcf_val, lcm_val = hcf_lcm([n] + [m for m in numbers if m != n])

        print(f"Prime factors of {n}: {factors}")

        print(f"HCF of {n} and {numbers}: {hcf_val}")

        print(f"LCM of {n} and {numbers}: {lcm_val}")

if __name__ == "__main__":

    main()

