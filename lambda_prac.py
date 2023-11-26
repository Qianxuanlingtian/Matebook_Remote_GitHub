init = input('请输入一个整数：')
if init.isalnum():
    num = int(init)
    temp = list(map(lambda x: str(x), filter(lambda x: x % 2 == 0, range(num))))
    print(f'返回0-{num}之间的偶数：', ', '.join(temp))
