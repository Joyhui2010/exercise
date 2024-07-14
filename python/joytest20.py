"""
题目：逆序输出一个list
"""

def nixuL(L):
    # L = [1, 2, 3, 4, 5]
    print(L[::-1])

user_input = input("请输入一个列表: ")
L = eval(user_input)

nixuL(L)