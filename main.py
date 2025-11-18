b, c = 2, 4


def g_func(d):
    global a
    a = d*c


g_func(b)
print(a)
