#Ofek Elgozi, 318432085
#Ido Hazan, 316613769
#Stav Sharabi, 208163840

#Q1
#השאלה מצורפת בקובץ Word

#Q2
eps = 1.0
while eps + 1 > 1:
    eps /= 2
eps *= 2
print("The machine epsilon is:", eps)

#Q3 + Q4
ans = abs(3.0*(4.0/3.0-1)-1)
print("Answer is:", ans)

fixed = abs(round(3.0*(4.0/3.0-1)-1))
print("Fixed Answer is:", fixed)


