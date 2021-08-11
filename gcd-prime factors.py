def prime_detector(n):
    for i in range (1, round(n // 2 )):
        count = 0
        if n % i == 0:
            count = count+1
    return(count)

A = []
B = []
BB = []
AA = []
a = int(input("enter first nummber"))
b = int(input("second number"))
for i in range(1,round(a ** (0.5))):
    if prime_detector(i) == 1:
        A.append(i)

for k in range(1,round(b ** (0.5))):
    if prime_detector(k) == 1:
        B.append(k)
    else:
        pass

for j in B:
    if b % j == 0:
        BB.append(j)
    else:
        pass

for t in A:
    if b % t == 0:
        BB.append(t)
    else:
        pass


for  p in  A:
    if a % p == 0:
        AA.append(p)
    else:
        pass

gcd = 1
for u in AA:
    if u in BB:
        gcd = gcd * u
    else:
        pass





