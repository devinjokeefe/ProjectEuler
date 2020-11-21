sumNum = 10
i = 6
j = 2

def isprime(n):
    n = abs(int(n))
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

while i < 2000000:

    if isprime (i):
        sumNum += i
        print (sumNum, i)
    else:
        pass
    i+=1
