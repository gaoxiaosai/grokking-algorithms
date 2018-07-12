# 尾递归求阶乘100！
import time


def factorials(num, sum1):
    if num == 1:
        return sum1
    else:
        return factorials(num - 1, num * sum1)


if __name__ == '__main__':
    t1 = time.time()
    print(factorials(1000, 1))
    t2 = time.time()
    print(t2 - t1)
# 0.0004999637603759766
# 递归求阶乘100！
# import time
#
#
# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)
#
#
# if __name__ == '__main__':
#     t1 = time.time()
#     print(factorial(1000))
#     t2 = time.time()
#     print(t2 - t1)
