def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


def tailFibonacci(n, before1=1, before2=1):
    if n < 2:
        return before1

    return tailFibonacci(n-1, before1 + before2, before1)


print(fibonacci(5))
print(tailFibonacci(5))
