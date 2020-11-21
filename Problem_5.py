i = 20

while True:
    mistakes = 0
    for j in range (20, 0, -1):
        if i % j == 0:
            pass
        else:
            mistakes += 1
    if (mistakes >= 1):
        i += 20 
    else:
        break
    
print (i)
