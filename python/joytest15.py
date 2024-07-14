"""
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
"""
def rabbit(n):
    if n > 1:
        return (rabbit(n-1)+rabbit(n-2))
    else:
        return n

s=float(0)
for i in range(20):
    num=rabbit(i+3)/rabbit(i+2)
    s=s+num
print(s)