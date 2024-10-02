#1
number=int(input('Enter the number: '))
number=str(number)
summa=0
for i in range(len(number)):
    summa+=int(number[i])
while len(str(summa))>1:
    new_sum=0
    summa=str(summa)
    for m in range(len(summa)):
        new_sum+=int(summa[m])
    summa=new_sum
print(summa)