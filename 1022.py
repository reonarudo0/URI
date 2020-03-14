from fractions import Fraction

n = int(input())
for i in range(n):
    entry = input().split()
    if(entry[3] == '+'):
        n1=int(entry[0])*int(entry[6]) + int(entry[2])*int(entry[4])
        n2=int(entry[2])*int(entry[6])
    elif(entry[3] == '-'):
        n1 = int(entry[0]) * int(entry[6]) - int(entry[2]) * int(entry[4])
        n2 = int(entry[2]) * int(entry[6])
    elif(entry[3] == '*'):
        n1 = int(entry[0]) * int(entry[4])
        n2 = int(entry[2]) * int(entry[6])
    else:
        n1 = int(entry[0]) * int(entry[6])
        n2 = int(entry[2]) * int(entry[4])
    print('{}/{} = '.format(n1,n2),end='')
    frac = Fraction(n1,n2)
    print('{}/{}'.format(frac.numerator,frac.denominator))