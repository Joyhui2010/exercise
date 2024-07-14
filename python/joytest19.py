"""
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
"""
def weishu(num):
    # for i in range(5,0,-1):
    #     if (num/(10*i))>=1:
    #         return (i)
    return(len(str(num)))
def nixu(num):
        str1= str(num)
        p=str1[::-1]
        print (p)

input_num = int(input("input a num:"))
print(weishu(input_num))
print(nixu(input_num))