#CHALLENGE
l = []
print(l)

ing = 'salt', 'pepper','curry','thyme','lime','okra'
print(len(ing))
f,*m,z = ing
print(f)
print(*m)
print(z)

mixed_data_types = ['Kemi', '19', '5\'6','Single','Lagos']
print(mixed_data_types)

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
it_companies.remove('Facebook')
print(it_companies[3:7])
print(it_companies[::-2])


it_companies.pop()
it_companies.insert(0,'Yahoo')
print(it_companies)
print(len(it_companies))
print(' # '.join(it_companies))

first, *middle, last = it_companies
middle.append('Bing')
print(first)
print(*middle)
print(last)
print(first, *middle, last)

it_companies.clear()
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
fullstack = front_end + back_end
print(fullstack)
fullstack.copy()


#LEARN
list = list()
#print(len(list))

animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway'] 
#Print the lists and its length
#print(f'Fruits: {fruits}')
#print('Number of fruits:', len(fruits))
#print('Vegetables:', vegetables)
#print('Number of vegetables:', len(vegetables))

names = ['Kemi','TK', 'Ose', 'Kilo', 'Immanuel']
names.sort()
#print(names)
names.sort(reverse=True)
#print(names)

names[1] = 'LOLA'
names.append('kay')
ex = 'LOLA' in names
names.insert(1,'koko')
#names.remove('Ose')
names.pop(1)
del names[2]
names.clear()

#print(ex)
#print(names)
#print(names[0])
#print(names[-2])
#k,t,*rest,I = names
#print(I)
#print(rest)

del names
#print(names)