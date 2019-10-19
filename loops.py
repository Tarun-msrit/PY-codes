hungry = True

if hungry:
    print('feed me')
else:
    print('im not hungry')


loc = 'Bank'
if loc == 'auto shop':
    print("cars are cool")
elif loc =='Bank':
    print("Money is cool\n")
else:
    print("I do not know much.")

mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print(num)

for num in mylist:
    print('hello')

for num in mylist:
    #check for even
    if num % 2 == 0:
        print(num)

for num in mylist:
    #check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')

list_sum = 0
for num in mylist:
    list_sum = list_sum + num

print(list_sum)

mystring = 'Hello World'
for letter in mystring:
    print(letter)

mystring = 'Hello World'
for _ in mystring:
    print('Cool!')

tup = (1,2,3)
for item in tup:
    print(item)

my_tuplist=[(1,2),(3,4),(5,6),(7,8)]
for item in my_tuplist:
    print(item)


for (a,b) in my_tuplist:                 #tuple unpacking
    print(a)
    print(b)

d = {'k1':1,'k2':2,'k3':3}
for item in d.items():
    print(item)
for key,value in d.items():
    print(value)







