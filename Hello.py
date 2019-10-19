print("Hello world")
print("bye")
mystring = 'abcdefghijk'
print(mystring)
print(mystring[2:9])
print(mystring[2])
print(mystring[-2])
print(mystring[:3])
print(mystring[::])
print(mystring[::2])
print(mystring[::-1])
print(mystring[::-2])
print(mystring[0:7:2])

name = 'Sam'
# name[0] = 'P'
last_letters = name[1:]
print('P' + last_letters)
x = "Hello World"
x = x + " it is beautiful outside!"
print(x)
letter = 'z'
y = letter * 10
print(y)

m = 'bye'
k = m.upper()
print(k)

print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))
print("The {q} {b} {f}".format(f='fox', b='brown', q='quick'))

result = 100/777
print('the result was {r:1.5f}'.format(r=result))
my_list = [1,2,3]
print(len(my_list))
mylist = ['one','two','three']
print(mylist[1])
print(mylist[1:])
anotherlist = ['four','five']
newlist = mylist + anotherlist
print(newlist)
newlist[0] = 'ONE ALL CAPS'
print(newlist)
newlist.append('six')
print(newlist)
newlist.pop()
print(newlist)
newlist = ['a','e','x','b','c']
newlist.sort()
sortedlist = newlist
print(sortedlist)
numlist = [8,3,9,4]
numlist.sort()
newnumlist = numlist
print(newnumlist)
