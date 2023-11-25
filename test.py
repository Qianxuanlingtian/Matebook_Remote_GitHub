def type_check(correct_type):
    def outer(func):
        def inner(x):
            if type(x) == correct_type:
                return func(x)
            else:
                return '参数类型错误'
        return inner
    return outer

@type_check(int)
def double(x):
    return x * 2

@type_check(str)
def upp(x):
    return x.upper()

print(double(2))
print(double('2'))
print()
print(upp('I love the world!'))
print(upp(250))
