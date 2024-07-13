"""
题目：判断101-200之间有多少个素数，并输出所有素数。
"""


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if (num % i) == 0:
            return False
    return True


for num in range(101, 201):
    if is_prime(num):
        print(num)



