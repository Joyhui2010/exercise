print(r'''hello,\n 
world''')


def mul(x, *y):
    s = 1
    for n in y:
        s = s * n
        print(x * s)


mul(5, 6, 7, 9)


def strim(s):
    t = 0
    w = len(s)
    while t < w and s[t] == " ":
        t = t + 1
    while w > 0 and s[w - 1] == " ":
        w = w - 1
    if t >= w:
        return ""
    return s[t: w]


test = strim("  2erwerwer     ")

print(test)


def find(L):
    Min = L[0]
    Max = L[0]

    for i in L:

        if i < Min:
            Min = i

        if i > Max:
            Max = i

    return (Min, Max)


s = [4, 6, 1, 9, 5, 0, 3]

print(find(s))
