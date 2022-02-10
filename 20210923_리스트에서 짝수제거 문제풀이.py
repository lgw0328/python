
a =[20 , 34 , 214 , 65 , 124 , 44 ,388 ,57, 21,68]
i = 0

while i < len(a):
    if a[i]%2 == 0:
        del a[i]
    else:
        i += 1


print(a)
