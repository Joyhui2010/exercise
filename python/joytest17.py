"""
题目：判断输入的字符串是回文，例如：aba，abba都是回文
"""
# def huiwen(s):
#     return s == s[::-1]
#
# input_string = input("请输入一行字符：")
# print(huiwen(input_string))

def huiwen(s):
    n=len(s)
    # for i in range(n//2):
    #     # print(s[i],end="")
    #     if s[i]!=s[n-i-1]:
    #         return False
    #     else:
    #         return True
    i = 0
    j = n - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

input_string = input("请输入一行字符：")
print(huiwen(input_string))
