#1
number=input('Enter the number: ')
print(number[0]+number[3]+number[2]+number[1]+number[4])

#2
number_of_days=int(input('Enter the number of days: '))
num_of_weeks=number_of_days//7
rest_days=number_of_days%7
if rest_days==6:
    num_of_weekends=num_of_weeks*2+1
else:
    num_of_weekends=num_of_weeks*2
print(f'Number of weekends before vacation: {num_of_weekends}')

#3
length = int(input('Enter the length of chocolate: '))
width = int(input('Enter the width of chocolate: '))
desired_piece = int(input('Enter the size of desired piece: '))

if desired_piece <= length * width and (desired_piece % length == 0 or desired_piece % width == 0):
    print('True')
else:
    print('False')

#4
thous_num=['','M','MM','MMM']
hundr_num=['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
dec_num=['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
units_num=['','I','II','III','IV','V','VI','VII','VIII','IX']
arabic=int(input('Enter the number: '))
dig_1=arabic//1000
dig_2=(arabic//100)%10
dig_3=(arabic//10)%10
dig_4=arabic%10
if dig_1 <=3 and arabic >= 1:
 print(thous_num[dig_1]+hundr_num[dig_2]+dec_num[dig_3]+units_num[dig_4])
else:
 print('Out of range')

 #5
 number = input("Enter the number: ")
 is_positive_float = False
 digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

 if number.count('.') > 1 or number[0] == '.' or number[-1] == '.':
     print('False')
 else:
     for letter in range(len(number)):
         if number[letter] in digits:
             is_positive_float = True
         else:
             is_positive_float = False
             print(is_positive_float)
             break
 if is_positive_float:
     print('True')

 #5 for negative values
number = input("Enter the number: ")
is_negative_float = False
digits=['0','1','2','3','4','5','6','7','8','9','.']

if number.count('.') > 1 or number[-1]=='.' or number[0]!='-':
    print('False')
else:
    for letter in range(1,len(number)):
        if number[letter] in digits:
            is_negative_float = True
        else:
            is_negative_float=False
            print(is_negative_float)
            break
if is_negative_float:
    print('True')

