"""PRIME NUMBER PROGRAM."""


def prime(num: int, count: int = 0) -> bool:
    """Prime number program.

    Returns:
        Boolean Value: Returns a Boolean Value True if the number is prime,
        False otherwise.
    """
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    return count == 2


print(prime(10))
