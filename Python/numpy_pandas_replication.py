from typing import List, Tuple, Callable, Union
import random


def np_random(shape: Tuple[int, int]) -> List[List[float]]:
    """
    Returns a NumPy-like array of random floats with the given shape.

    Example:
    >>> np_random((2, 3))
    [[0.8415504634427585, 0.9089211930093746, 0.6554788710727981], [0.6724108698175846, 0.9831866924753739, 0.9509883583194048]]
    """
    return [[random.random() for _ in range(shape[1])] for _ in range(shape[0])]


def np_mean(arr: List[List[float]]) -> float:
    """
    Returns the mean of all values in a NumPy-like array.

    Example:
    >>> np_mean([[1, 2, 3], [4, 5, 6]])
    3.5
    """
    return sum([num for row in arr for num in row]) / (len(arr) * len(arr[0]))


class Series:
    def __init__(self, data: List[float]):
        self.data = data

    def __repr__(self):
        return f"Series({self.data})"

    def __getitem__(self, key: int) -> float:
        return self.data[key]

    def __len__(self) -> int:
        return len(self.data)

    def apply(self, func: Callable[[float], float]) -> 'Series':
        """
        Applies a function to each element of the Series and returns a new Series with the results.

        Example:
        >>> s = Series([1.2, 2.5, 3.7, 4.8])
        >>> s.apply(lambda x: x ** 2)
        Series([1.44, 6.25, 13.69, 23.04])
        """
        return Series([func(val) for val in self.data])


class DataFrame:
    def __init__(self, data: List[List[float]]):
        self.data = data

    def __repr__(self):
        return f"DataFrame({self.data})"

    def __getitem__(self, key) -> Union['Series', 'DataFrame']:
        if isinstance(key, str):
            return Series([row[key] for row in self.data])
        else:
            return DataFrame([row for row_with_index in enumerate(self.data) if row_with_index[0] == key])

    def apply(self, func: Callable[[float], float], axis: int = 0) -> 'DataFrame':
        """
        Applies a function to each element of the DataFrame along a specified axis and returns a new DataFrame with the results.

        Example:
        >>> df = DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> df.apply(lambda x: x / 2, axis=0)
        DataFrame([Series([0.5, 1.0, 1.5]), Series([2.0, 2.5, 3.0]), Series([3.5, 4.0, 4.5])])
        >>> df.apply(lambda x: x / 2, axis=1)
        DataFrame([Series([0.5, 1.0, 1.5]), Series([2.0, 2.5, 3.0]), Series([3.5, 4.0, 4.5])])

