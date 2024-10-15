my_dict={'Oleg':2000,'Alina':1999,'Miya':2021}
print(my_dict)
print(my_dict['Oleg'])
print(my_dict.get('Vasya'))
my_dict.update({'Kolya':1998,'Vasya':1996})
O=my_dict.pop('Oleg')
print(O)
print(my_dict)

my_set={1,1,1,3,4,5,6,5,4,5,7,3,3,3,6,3,2}
print(my_set)
my_set.update({'Sokol',(1,2,3)})
my_set.remove(1)
print(my_set)