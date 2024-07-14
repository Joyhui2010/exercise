"""
题目：输入一行字符，分别统计出各个字符分别的个数。
"""
def count(input_string):
    d=dict()
    for i in input_string:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    print(d)
count("534tetokpojtowet33333")