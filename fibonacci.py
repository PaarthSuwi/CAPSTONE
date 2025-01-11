def fast_doubling(n):
    def _fast_doubling(n):
        if n == 0:
            return (0, 1)
        a, b = _fast_doubling(n // 2)  # Recursive call
        c = a * (2 * b - a)
        d = b * b + a * a
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

    return _fast_doubling(n)[0]

# Example usage
n = int(input("Enter the value of n: "))
print(f"Fibonacci({n}) = {fast_doubling(n)}")


def fibonacci_iterative(n):
    fib_series = []
    a, b = 1, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Example usage
n = int(input("Enter the number of terms: "))
print(f"Fibonacci Series (Iterative): {fibonacci_iterative(n)}")