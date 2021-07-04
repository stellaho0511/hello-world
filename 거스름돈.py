mon = [500, 100, 50, 10, 5, 1]
count = 0
num = 1000 - int(input())
for i in range(len(mon)):
    count += num // mon[i]
    num = num % mon[i]
print(count)
