name = 'kemi'
last = 'ibitoye' 
level = '300'
koko = 'I am %s %s and i\'m a %s level student' % (name, last, level)
print(koko)

length = 40
breadth = 30
area = length * breadth
rectangle = 'The area of the rectangle with a length of %d and breadth of %d is %d.'%(length, breadth, area)
print(rectangle)

length = 40
breadth = 30
area = length * breadth
rectangle = 'The area of the rectangle with a length of {} and breadth of {} is {}.' .format(length, breadth, area)
print(rectangle)

a = 3
b = 7
ans = 'The answer above would be {} + {} = {}.'.format(a, b, a + b)
print(ans)

name = 'kemi'
print(name[-1])

name = 'Immanuel'
print(name[4:8])

name = 'Immanuel'
print(name[::-1])

name = 'Immanuel'
print(name[0:8:2])  

name = 'Oluwafolakemi'
print(name[0:14:3])

name = 'oshodi'
print(name.capitalize())

name = 'oshodi'
print(name.count('o'))

name = 'oshodi'
print(name.endswith('o'))

greet = 'Hello,\tWorld!'
print(greet.expandtabs(1))

greet = 'Hello,\tWorld!'
print(greet.find('o'))

intro = ['I', 'AM', 'GAY']
print(' and '.join(intro))

intro = ['I', 'AM', 'GAY']
f = ' and '.join(intro)
print(f)

name = 'My name is Folakemi'
print(name.replace('Folakemi', 'Eseohe'))

name = 'My name is Folakemi'
print(name.split(', '))

name = 'My name is Folakemi'
print(name.title())

name = 'my name is Folakemi'
print(name.swapcase())

#CHALLENGE
th = ['Thirty', 'Days', 'Of', 'Python']
print(' '.join(th))

cod = ['Coding', 'For', 'All']
print(' '.join(cod))

company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[7:14])
print(company.find('Coding'))
print(company.replace('Coding', 'Python'))
print(company.split())

one = ('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon')
print(one.split(', '))

print(company[0])
print(company[-1])
print(company[10])
print(company[0:14:2])
print(company.index('C'))
print(company.index('F'))
print(company.find('i'))

sen = 'You cannot end a sentence with because because because is a conjunction'
print(sen.index('because'))
print(sen.rindex('because'))
print(company.startswith('Coding'))
print(company.endswith('Coding'))

t = '30DaysOfPython'
v = 'thirty_days_of_python'
print(t.isidentifier())
print(v.isidentifier())

library = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(library))

print('I am enjoying this challenge.\nI just wonder what is next.')
table = 'Name\tAge\tCountry\tCity\nAsabeneh\t50\tFinland\tHelsinki'
print(table.expandtabs(10))

radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square.'.format(radius, area))

a = 8
b = 6
print('{} + {} = {}'.format(8,6,8+6))
print('{} - {} = {}'.format(8,6,8-6))
print('{} * {} = {}'.format(8,6,8*6))
print('{} / {} = {:.2f}'.format(8,6,8/6))
print('{} % {} = {}'.format(8,6,8%6))
print('{} // {} = {}'.format(8,6,8//6))
print('{} ** {} = {}'.format(8,6,8**6))