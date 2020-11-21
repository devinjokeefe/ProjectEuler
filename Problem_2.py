fibs = []

fibs.append (1)
fibs.append (2)

for i in range (2,34):
	fibs.append(fibs[i-2] + fibs[i-1])

num = 0

for i in range (32):
    if fibs[i] % 2 == 0:
        num += fibs[i]
    else:
        pass

print (num)
