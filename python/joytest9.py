"""
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
"""

def count(input_string):
    letters_count = 0
    spaces_count = 0
    digits_count = 0
    others_count = 0
    for char in input_string:
        if char.isalpha():
            letters_count += 1
        elif char.isspace():
            spaces_count += 1
        elif char.isdigit():
            digits_count += 1
        else:
            others_count += 1
    return letters_count, spaces_count, digits_count, others_count

input_string = input("请输入一行字符：")
letters, spaces, digits, others = count(input_string)
print("英文字母个数:", letters)
print("空格个数:", spaces)
print("数字个数:", digits)
print("其他字符个数:", others)