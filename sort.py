liste = [1,5,2,78,12,34,41]
error = True
op = 0
loop = 0
while error:
    loop +=1
    error = False
    for i in range(len(liste)-1):
        op +=1
        if liste[i] > liste[i+1]:
            error = True
            a = liste[i]
            liste[i] = liste[i+1]
            liste[i+1] = a

print("Final result :")
print(liste)
print("there have been "+str(op)+" operations and "+str(loop)+"loop")