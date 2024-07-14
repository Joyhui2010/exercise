"""
题目：求1+2!+3!+...+20!的和。
"""
def jiecheng(n):
    a=1
    s=0
    for i in range(1,n+1):
        a=a*i
        s=s+a
    print(s)

jiecheng(20)


# # print(jiecheng(5))
# s=0
# for i in range(20):
#     s=s+jiecheng(i+1)
# print (s)




