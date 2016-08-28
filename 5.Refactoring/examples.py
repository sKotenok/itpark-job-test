#!/usr/bin/env python3

"""
1.

try:
    f = open('/tmp/data.txt')
    data = f.readline()
    return data
except:
    f.close()
else:
    f.close()
"""
def myfunc():
    with open('/tmp/data.txt') as f:
        return f.readline()

"""
2.

a = [1, 2, 3, 4]
s = 0
for i in a:
    s+=i

print s
"""
a = [1, 2, 3, 4]
s = sum(a)

print(s)


"""
3.

a = [1, -2, 3, -4]
b = []
for i in a:
    if i > 0:
        b.append(i)

print b
"""
a = [1, -2, 3, -4]

# v1.
b = [i for i in a if i > 0]
print(b)

# v2.
b = list(filter(lambda i: i > 0, a))
print(b)
