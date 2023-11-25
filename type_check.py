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

print('double第一个参数：2，打印结果为：', double(2))
print('double第二个参数：\'2\'，打印结果为：', double('2'))

print('\nupp第一个参数：\'I Love The World\'，打印结果为：', upp('I Love The World'))
print('upp第二个参数：250，打印结果为：', upp(250))