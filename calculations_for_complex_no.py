#print the addition, subtraction, multiplication, division and modulus operations of two complex numbers
p = list(map(float, input().split()))
A = p[0] + p[1] * 1j
p = list(map(float, input().split()))
B = p[0] + p[1] * 1j
def printc(A):
    sign = ""
    if A.imag >= 0: 
        sign = "+"
    else:
        sign = "-"
    if A.imag == 0:
        print("%.2f" % A.real)
    elif A.real != 0:
        print("%.2f" % A.real, sign, "%.2fi" % abs(A.imag))
    else:
        print("%.2fi" % A.imag)
printc(A + B)
printc(A - B)
printc(A * B)
printc(A / B)
print("%.2f" % abs(A))
print("%.2f" % abs(B))
