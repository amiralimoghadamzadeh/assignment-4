def GCD(x,y):
    while y > 0:
        x, y = y ,x % y 
    return x


a = int(input())
b = int(input())

print(GCD(a,b))