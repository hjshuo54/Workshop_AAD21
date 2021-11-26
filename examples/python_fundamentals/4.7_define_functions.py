# The keyword def introduces a function definition.
# It must be followed by the function name and the parenthesized list of
# formal parameters. The statements that form the body of the
# function start at the next line, and must be indented.

def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:

fib(10000)

def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

print(fib2(10000))