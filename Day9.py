fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter a fruit: ')
if fruit in fruits:
    print('That fruit already exists in the list.')
else:
    fruits.append(fruit)
    print('Modified list:', fruits)
    
    
Autumn = ['September', 'October', 'November']
Winter = ['December', 'January', 'February']
Spring = ['March', 'April', 'May']
Summer = ['June', 'July', 'August']
month = input('Enter month:')
if month in Autumn:
    print('The season is Autumn.')
elif month in Winter:
    print('The season is Winter.')
elif month in Spring:
    print('The season is Spring.')        
else:
    print('The season is Summer.')


age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive.")
else:
    print('You need', 18 - age, 'more years to learn to drive.')



myage = 19
yourage = int(input("Enter your age: "))
if yourage == myage:
    print('We are the same age.')
elif yourage > myage:
    print('You are', yourage - myage, 'years older than me.')
else:
    print('I am', myage - yourage, 'years older than you.')


a = int(input('Enter a: '))
b = int(input('Enter b: '))
if a>b:
    print(f'{a} is greater than {b}')
elif a<b:
    print(f'{a} is less than {b}')
else:
    print(f'{a} is equal to {b}') 


score = int(input('Enter your score: '))
if score >=90:
    print('Your score is A')
elif score >=80:
    print('Your score is B')
elif score >=70:
    print('Your score is C')
elif score >=60:
    print('Your score is D')
else:
    print('Your score is F')
