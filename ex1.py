n1= float(input("entre com n1"))
n2= float(input("entre com n2"))
n3= float(input("entre com n3"))
ME= float(input("entre com ME"))

MA = (n1 + n2*2  + n3*3 + ME)/7

if MA >= 9:
    print("Sua média final foi: ", MA, ". Parabéns, essa é uma média alta!")
elif MA < 4:
    print("Sua média final foi: ", MA, ". Atenção, essa é uma média baixa!")
else:
    print("Sua média final foi: ", MA)