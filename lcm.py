a = int(input())
b = int(input())
A = []
B = []
for i in range(1,b):
    y = a * i
    A.append(y)

for j in range(1,a):
    x = b * j
    B.append(x)



for k in range(b - 1):
    if A[k] in B:
        print(A[k])
        break
    else:
        pass