import typing
import functools
import concurrent.futures

def add(x: int, y: int) -> int:
    """Add two integers."""
    return x + y

def sum_list(numbers: typing.List[int]) -> int:
    """Calculate the sum of a list of integers."""
    return functools.reduce(add, numbers)

def filter_list(numbers: typing.List[int], max_value: int) -> typing.List[int]:
    """Filter a list of integers to include only those less than or equal to a maximum value."""
    return [num for num in numbers if num <= max_value]

def process_list(numbers: typing.List[int], max_value: int) -> typing.Dict[str, typing.Union[int, typing.List[int]]]:
    """Process a list of integers by filtering and summing."""
    filtered_numbers = filter_list(numbers, max_value)
    total = sum_list(filtered_numbers)
    return {'sum': total, 'filtered': filtered_numbers}

def main():
    """Demonstrate the use of concurrent programming with the above functions."""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    max_value = 5
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # Submit a job to process the list of numbers
        future = executor.submit(process_list, numbers, max_value)
        print(f'Processing list {numbers} with maximum value {max_value}...')
        # Do other work while waiting for the job to finish
        while not future.done():
            print('Doing other work...')
        # Retrieve the result of the job and print it
        result = future.result()
        print(f'Result: {result}')

if __name__ == '__main__':
    main()

