nums = input('Введите числа через пробел: ')

def external(start=0):
    def middle(func):
        def inner(string):
            return func(string) + start
        return inner
    return middle

@external(start=5)
def f(string):
    return sum(list(map(int, string.split())))

print(f(nums))