for a in range(200, 400):
    for b in range(200, 400):
        for c in range(350, 500):
            if (a**2 + b**2) == c**2:
                if (a+b+c == 1000):
                    print (str(a) + " + " + str(b) + " + " + str(c) + " = " + str(a+b+c)) 
