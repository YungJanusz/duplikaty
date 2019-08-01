import random as rand
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
d = []

for i in a:
    if i not in b:
        c.append(i)
for x in b:
    if x not in c:
        c.append(x)
print (sorted(c))

tab1 = rand.sample(range(0,30),9)
tab2 = rand.sample(range(0,30),9)
print(sorted(tab1))
print(sorted(tab2))

for i in tab1:
    if i not in tab2:
        d.append(i)
for x in tab2:
    if x not in d:
        d.append(x)
print (sorted(d))




