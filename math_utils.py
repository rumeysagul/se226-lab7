add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else ('you cannot divide by zero.')
power = lambda x, y: x ** y
mod = lambda x, y: x % y if y != 0 else ("you cannot divide by zero.")


if __name__ == '__main__':
    print(add(2, 3))
    print(subtract(2, 3))
    print(multiply(2, 3))
    print(divide(2, 3))
    print(power(2, 3))
    print(mod(2, 3))




