# A lambda functions is a anonymous function.
# Lambda can take any number of arguments but can only have one expression.
# The expression is executed and the result is returned.

### syntax
# lambda arguments : expression
x = lambda a,b: a + b
print(x(7,3))

# Power of lambda is better shown when you use them inside another functions.
def double_lambda(n):
    return lambda a : a * n
my_lambda = double_lambda(2)
print(my_lambda(3)) # my_lambda = lambda a : a * n becuase power_lambda is that
print("################################")


def tripler_double(i):
    return lambda j: j * i

double = tripler_double(2)
tripler = tripler_double(3)

print(double(10))
print(double(20))


# Use lambda functions when an anonymous function is required for a short period of time.