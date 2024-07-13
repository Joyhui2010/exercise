"""
题目：打印斐波那契数列前10个数
"""
def rabbit():
    yi=1
    er=1
    n=8
    print(yi)
    print(er)
    while n>0:
        san=yi+er
        print(san)
        yi=er
        er=san
        n-=1
rabbit()

# 1 1 2 3 5 8
