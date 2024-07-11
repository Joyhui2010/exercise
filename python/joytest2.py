"""
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""
def paixu():
    sum=0
    for i in [1,2,3,4]:
        for j in [1,2,3,4]:
            for k in [1,2,3,4]:
                if j!=i and k!=i and k!=j:
                    print(f'{i}{j}{k}')
                    sum+=1
                    # print(i,j,k)
    print(sum)
paixu()




