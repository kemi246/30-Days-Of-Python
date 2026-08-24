li = {'one','two','three'}
li.add('four')
s = {'seven','eight'}
li.update(s)
print(li)
li.update(['five','six'])
print(li)
li.pop()
print(li)

s3 = li.union(s)
print(s3)

fru = {'apple','pear','ham'}
veg = {'spinach','carrot','ham'}
s = {'apple'}
mim = fru.union(veg)
print(mim)
print(fru.intersection(veg))
print(s.issubset(fru))
print(fru.issuperset(s))
print(fru.difference(veg))
print(fru.symmetric_difference(veg))
print(fru.isdisjoint(veg))

#challenge
print(''' 


''')
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.update(['AMZ','AWS'])
print(it_companies)
it_companies.discard('AWS')
print(it_companies)
print(''' 
''')
AB = A.union(B)
print(AB)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))
del A
del B
