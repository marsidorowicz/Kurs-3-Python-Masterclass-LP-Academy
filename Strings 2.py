key = n
y = i = j = sumall = 0
for i in range(0, n):
    while j < n:
        val = arr[i][j]
        sumall = sumall + val
        i += 1
        j += 1