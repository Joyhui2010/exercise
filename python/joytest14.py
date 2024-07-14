"""
题目：打印出如下图案（菱形）:

   *
  ***
 *****
*******
 *****
  ***
   *

"""
def sque(n):
    for i in range(n):
        for j in range(n-1-i):
            print(" ",end="")
        for k in range(2*i+1):
            print("*",end="")
        print()
    for i in range(n-2,-1,-1):
        for j in range (n-1-i):
            print(" ",end="")
        for k in range (2*i+1):
            print("*",end="")
        print()
sque(4)