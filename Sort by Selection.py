
l = [4,5,7,2,6]
for i in range(len(l)):
    minu = i
    for j in range(i+1, len(l)):
        if l[j] < l[minu]:
            minu = j
    l[i], l[minu] = l[minu], l[i]
print(l)

