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

#2
sits=[[0,1,1,0], [1,0,0,0], [0,1,0,0]]
required=int(input('Enter number of tickets: '))
found=False

for n in range(len(sits)):
    row=sits[n]
    count=0
    for seat in range(len(row)):
        if row[seat]==0:
            count+=1
            if count == required:
                found = True
                break
        else:
            count=0
    if found:
        print(n)
        break
else:
    print('False')

#3
string=input('Enter the symbols: ')
coded=[]
count=1
for i in range(1,len(string)):
    if string[i]==string[i-1]:
        count+=1
    else:
        coded.append(f'{count}{string[i-1]}')
        count=1
coded.append(f"{count}{string[-1]}")
coded_str=''.join(coded)
print(coded_str)

#4
line=input('Enter words and key: ')
string,key=line.split(',')
key=int(key)
alph_low=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alph_up=[letter.upper() for letter in alph_low]
letter_list=[]
for letter in string:
    if letter in alph_low:
        index=alph_low.index(letter)
        new_index=index+key
        if new_index<len(alph_low):
            new_letter=alph_low[index+key]
        else:
            another_index=new_index-len(alph_low)
            new_letter=alph_low[another_index]
    elif letter in alph_up:
        index=alph_up.index(letter)
        new_index=index+key
        if new_index<len(alph_up):
            new_letter=alph_up[index+key]
        else:
            another_index=new_index-len(alph_up)
            new_letter=alph_up[another_index]
    else:
        new_letter=letter
    letter_list.append(new_letter)
coded_string = ''.join(letter_list)
print(coded_string)

# 5
subj_dict = {}
while line := input('Enter subject, surname and grade (or press Enter to finish): '):
    subject, surname, grade = line.split()

    if subject not in subj_dict:
        subj_dict[subject] = {surname: [grade]}
    else:
        if surname not in subj_dict[subject]:
            subj_dict[subject][surname] = [grade]
        else:
            subj_dict[subject][surname].append(grade)
for subject in subj_dict:
    print(f'{subject}')
    for surname in subj_dict[subject]:
        print(f'  {surname} {" ".join(subj_dict[subject][surname])}')