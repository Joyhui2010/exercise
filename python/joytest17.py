"""
题目：判断输入的字符串是回文，例如：aba，abba都是回文
"""
def huiwen(s):
    return s == s[::-1]

input_string = input("请输入一行字符：")
print(huiwen(input_string))
