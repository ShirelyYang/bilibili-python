sum = 0
for i in range(1, 50):
    sum += i
    if sum > 100:
        print("i=%d" % i)
        break
print("sum=%d" % sum)