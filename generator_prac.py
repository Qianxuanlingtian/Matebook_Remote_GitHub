def gen(x):
    for i in range(x):
        yield i ** 2

init = input('请输入要测试的数字：')
if init.isalnum():
    num = int(init)
    gent = gen(num)
    print(f'返回值为从0开始到{init}各整数的平方：')
    for each in range(num):
        print(f'{each}的平方为：', next(gent))
