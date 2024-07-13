"""
题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
"""
def flower(num):
    a=num//100
    b=(num-100*a)//10
    c=num%10
    if (num== a*a*a+b*b*b+c*c*c):
        return True
    else:
        return False

for num in range (100,999) :
    if flower(num):
        print(num)