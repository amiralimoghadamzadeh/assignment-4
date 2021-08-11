def delta(a,b,c):
    x = (b ** 2) - (4 * a * c)
    return(x)

m = float(input("zaribe x^2"))
n = float(input("zaribe x"))
p = float(input("adade sabet"))

if delta(m,n,p) > 0:
    x1 = float(((-m) + delta(m,n,p)) / (2 * m))
    x2 = float(((m) + delta(m,n,p)) / (2 * m))
    print("the roots of the equation are:",x1,x2)
elif delta(m,n,p) == 0:
    x = (-n) / (2 * m)
else:
    print("your equation does not have a real root")

