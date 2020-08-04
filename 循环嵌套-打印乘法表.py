i = 1
j = 9
multi = 0
while j > 0:
    while i <= j:
        multi = i * j
        print("%d*%d=%d" % (i, j, multi), end=" ")
        i += 1
        pass
    print("\n")
    i = 1
    j -= 1
    pass
