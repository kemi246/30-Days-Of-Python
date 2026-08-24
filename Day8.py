person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person)

kemi = {'level':'300',
        'status':'single',
        'course':'game dev'}
print(kemi['course'])
print(kemi.get('status'))
kemi['age']  = '19'
kemi['status'] = 'Dating'
print(kemi)
print('habit' in kemi)
kemi.pop('level')
kemi.popitem()
del kemi['course']
print(kemi.items())
l = kemi.keys
print(l)
print(kemi.values)

#challenge
print('''


''')
dog = {'name':'Max',
       'color':'Gray',
       'breed':'German',
       'legs':'four',
       'age':'3'}

student = {'first_name':'Kemi',
           'last_name':'Ibitoye',
           'gender': 'Female',
           'age':'19',
           'marital status':'Single',
           'skills':['Coding','Writing'],
           'Country':'Nigeria',
           'City':'Lagos',
           'Address':'Lekki'}
print(len(student))
print(student['skills'])
student['skills'] = ['Sleeping','Speaking']
print(student)
v = student.values
x = student.keys
print (dog.items())
print(v)
print(x)
del student['marital status']
del dog