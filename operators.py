for num in range(0,11,2):
    print(num)

print(list(range(0,11,2)))

index_count=0
for letter in 'abcde':
    print(('At index {} the letter is {}'.format(index_count,letter)))
    index_count=index_count+1

index=0
word = 'abcde'
for letter in word:
    print(word[index])
    index=index+1


for item in enumerate(word):
    print(item)

for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

mylist1 = [1,2,3]
mylist2 = ['a','b','c']
for item in zip(mylist1,mylist2):
    print(item)

print(list(zip(mylist1,mylist2)))

'x' in [1,2,3]


mylist=[10,20,30,40,50]
print(min(mylist))
print(max(mylist))

from random import shuffle
mylist3 =[1,2,3,4,5,6,7,8,9,10]
shuffle(mylist3)
print(mylist3)

from random import randint
print(randint(0,100))

m =input('what is your name: ')
print(m)

n=int(input('choose a number:'))
square=n*n
print(square)