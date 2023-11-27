import timeit
#迭代函数
def fibIter(n):
    num1, num2 = 0, 1
    for i in range(n):
        num1, num2 = num2, num1 + num2
    return num1
#普通递归函数
def fibRecursion(n):
    if n == 1 or n == 2:
        return 1
    return fibRecursion(n - 1) + fibRecursion(n - 2)
#递归优化方法一：尾递归(Tail recursion)
def fibRec_TailRec(n, ret1 = 0, ret2 = 1):
    if n <= 1:
        return ret2
    return fibRec_TailRec(n - 1, ret2, ret1 + ret2)
#递归优化方法二：记忆化递归(Memorization recursion)
def fibRec_MemoRec(n, cache = {}):
    if n in cache:
        return cache[n]
    elif n <= 1:
        return n
    cache[n] = fibRec_MemoRec(n - 1) + fibRec_MemoRec(n - 2)
    return cache[n]
#递归优化方法三：分治法递归(Divide and conquer recursion)

#递归优化方法四：动态规划(Dynamic programming recursion)
    

#迭代函数调用
print('计算斐波那契数列f(12)的迭代函数调用结果', fibIter(12))
#普通递归函数调用
print('计算斐波那契数列f(12)的普通递归函数调用结果', fibRecursion(12))
#尾递归函数调用
print('计算斐波那契数列f(12)的尾递归函数调用结果', fibRec_TailRec(12))
#记忆化递归函数调用
print('计算斐波那契数列f(12)的记忆化递归函数调用结果', fibRec_MemoRec(12))

print('10万次迭代函数调用用时间：', round(timeit.timeit('fibIter(12)', setup="from __main__ import fibIter"), 2), '秒')
print('10万次普通递归函数调用时间：', round(timeit.timeit('fibRecursion(12)', setup="from __main__ import fibRecursion"), 2), '秒')
print('10万次尾递归函数调用时间：', round(timeit.timeit('fibRec_TailRec(12)', setup="from __main__ import fibRec_TailRec"), 2), '秒')
print('10万次记忆化递归函数调用时间：', round(timeit.timeit('fibRec_MemoRec(12)', setup="from __main__ import fibRec_MemoRec"), 2), '秒')