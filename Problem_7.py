i = 6 
prime = 3
j = 2

while True:
    while j <= i//2:
        if i % j == 0:
            j = 2
            i += 1
        else:
            if j == i//2: 
                prime += 1
                j = 2
                i += 1
                print ("Prime no. " + str(prime) + ": " + str(i-1))
            else:
                j += 1
