#EXERCISE 1
tpl = tuple()
siblings = ('Kolade', 'Lanre')
print(len(siblings))
ls = list(siblings)
ls.insert(0,'Oyo')
ls.insert(1,'Tade')
print(ls)
family_members = tuple(ls)
print(family_members)

#EXERCISE  2
par1, par2, *sib = ls
print(par1)
print(par2)
print(*sib)


fruits = ('banana','apple',)
veg = ('weed','carrot')
ap = ('dairy','kilishi')
food_stuff_tp = fruits + veg + ap
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
print(food_stuff_lt[:2] + food_stuff_lt[4:])
print(food_stuff_lt[2:4])
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)


#LEARN
fruit = ('apple', 'avocado')
veg = ('tomato', 'seaweed')
mix = (fruit, veg)
del veg 
#print(fruit[1])
#print(fruit)
#print(len(fruit))
#lst = list(fruit)
#print(lst)
#print('banana' in fruit)
#print(mix)