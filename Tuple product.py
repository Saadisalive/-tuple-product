tup1 = (4,3,2,2,-1,18)
tup2 = (2,4,8,8,3,2,9)
tup3 = []
for i in range(0,len(tup1)):
    tup3.append(tup1[i]*tup2[i])
print(tuple(tup3))