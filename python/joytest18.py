"""
题目：输入一个字符串，不引入新变量，
"""
def nixu(s):
    reversed_s = s[::-1]
    return reversed_s
input_string = input("请输入一行字符：")
print( nixu(input_string) )
