def fib(n):
    _, curr = fib_helper(n)
    return curr

def fib_helper(n):
    if n == 1:
        return 0, 1
    
    prev, curr = fib_helper(n-1)
    
    return curr, curr + prev

# starts at 1 to avoid "RecursionError: maximum recursion depth
# exceeded in comparison" (we assume the input is valid)
print([fib(i) for i in range(1, 11)])