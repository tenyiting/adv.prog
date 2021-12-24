#Using Lists
bob = ['Bob Smith', 42, 30000, 'software'] 
sue = ['Sue Jones', 45, 40000, 'hardware']
print(bob[0].split()[-1])
sue [2] *= 1.25
print(sue)


#Using Dictionaries

bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'} 
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': "hdw"}
print(bob['name'], sue['pay']) 

# not bob[0], sue[2]

print(bob['name'].split()[-1]) 

sue['pay'] *= 1.10

print(sue['pay'])