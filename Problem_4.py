def check_pal (num):
    num = str(num)
    for i in range(int(len(num)/2)):
        if num[i] == num[-1-i]:
            pass
        else:
            return False
    return True

max = 0

for a in range (999, 600, -1):
    for b in range (999, 600, -1):
        if check_pal (a*b) == True:
            if a*b > max:
                max = a*b
                print (max, a, b)
            else:
                pass
