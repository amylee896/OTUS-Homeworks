#1
def format_transf(line:str):
    if '_' in line:
        splitted_string=line.split('_')
        capital=[x.capitalize() for x in splitted_string]
        transformed=''.join(capital)
    else:
        upper=[i.isupper() for i in line]
        for i in range(1,len(upper)):
            upper=[i.isupper() for i in line]
            if upper[-i]:
                line=list(line)
                line.insert(-i,'_')
                lower=[x.lower() for x in line]
                transformed=''.join(lower)
    return(transformed)

#Using key default arguments:
def format_transf(line:str,case='camel'):
    if '_' in line and case=='snake':
        transformed=line
    elif '_' in line and case=='camel':
        splitted_string=line.split('_')
        capital=[x.capitalize() for x in splitted_string]
        transformed=''.join(capital)
    elif '_' not in line and case=='camel':
        transformed=line
    elif '_' not in line and case=='snake':
        upper=[i.isupper() for i in line]
        for i in range(1,len(upper)):
            upper=[i.isupper() for i in line]
            if upper[-i]:
                line=list(line)
                line.insert(-i,'_')
                lower=[x.lower() for x in line]
                transformed=''.join(lower)
    return(transformed)

#2
def valid_date():
    line=input('Enter the date: ')
    day,month,year=line.split('.')
    digit_check=year.isdigit()
    if digit_check:
        year=int(year)
    else:
        print('False')
        return
    if year not in range(100,3001):
        print('False')
        return
    days={'01':31,'02':29 if (year%4==0 and year%100 != 0) or year%400==0 else 28,'03':31,
                  '04':30,'05':31,'06':30,'07':31,'08':31,'09':30,'10':31,'11':30,'12':31}
    if month not in days:
        print('False')
        return
    if day.isdigit() and 1<=int(day)<=days[month]:
        print('True')
    else:
        print('False')

#3
def prime_numb_check(number:int):
    prime_numb=[1,2,3,5,7,11,13,17,19]
    last_number_prime=[1,3,7,9]
    dividers=[3,7,9,11,13,17,19]
    if number in prime_numb:
        result='True'
    elif int(str(number)[-1]) in last_number_prime:
        for num in dividers:
            if number % num == 0:
                return'False'
        result='True'
    else:
        result='False'
    return result

#4
def input_data():
    user_data={}
    lowercase = list(map(chr, range(97, 123))) #codes from ASCII
    uppercase = list(map(chr, range(65, 91)))
    while line := input('Enter name, surname, age and ID: '):
        name,surname,age,ID=line.split(',')
        digit_check=ID.isdigit()
        length=len(ID)
        if digit_check and length==8:
            ID=ID
        elif digit_check and length<8:
            number_zeros=8-length
            ID=ID+number_zeros*'0'
        else:
            print('Invalid ID!')
            continue
        if ID in user_data:
            print('User is already in the list')
        if age.isdigit() and 18 <= int(age) <= 60:
            age = age
        else:
            print('Invalid age!')
            continue
        if all(letter in lowercase+uppercase for letter in name):
            name = name.lower().capitalize()
        else:
            print('Invalid user name!')
            continue
        if all(letter in lowercase+uppercase for letter in surname):
            surname = surname.lower().capitalize()
        else:
            print('Invalid user surname!')
            continue
        user_data[ID] = (name, surname, age)
    print(f"{'ID':<10} {'Name':<15} {'Surname':<15} {'Age':<5}")
    for ID, (name, surname, age) in user_data.items():
        print(f"{ID:<10} {name:<15} {surname:<15} {age:<5}")
    return user_data