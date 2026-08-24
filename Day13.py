#exe
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
n_e = [i for i in numbers if i<=0]
print(n_e)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [number for row in list_of_lists for number in row]
print(flat_list)

tp1 = [(i,i+1,i,i,i,i,i) for i in range(1)]
print(tp1)

tp2 = [(i,i,i,i,i,i,i) for i in range(2) if i==1]
print(tp2)

tp3 = [(i,i-1,i,i*2,i**3,i**4,i**5) for i in range(3) if i == 2]
print(tp3)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
c = [(country.upper(), capital.upper()) for country in countries for (country, capital) in country]
print(c)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
c2 = [{'country': country.upper(), 'city': capital.upper()} for country in countries for (country, capital) in country]
print(c2)

slope = lambda x: 2*x + 3
print(slope(2))




language = 'Yoruba'
lst = list(language)
print(type(lst))
print(lst)

name = 'KEMI FOSHO'
lst =  list(name)
print(lst)

name = 'KEMI FOSHO'
lst = [i for i in name]
print(lst) 

numbers = [i for i in range(11)]
print(numbers)

sqr = [i**2 for i in range(11)]
print(sqr)

ntups = [(i, i, i) for i in range(11)]
print(ntups)

e_n = [i for i in range(20) if i%2 == 0]
print(e_n)

num = [-10, -5, 0, 5, 10]
p_e = [i for i in num if i%2==0 and i>0]
print(p_e)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)