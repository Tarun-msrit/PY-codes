mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)

print(mylist)


mylist2=[x for x in 'word']
print(mylist2)

mylist3=[num for num in range(0,11)]
print(mylist3)

mylist4=[num**2 for num in range(0,11)]
print(mylist4)

mylist5=[x for x in range(0,11) if x%2==0]
print(mylist5)

celcius=[0,10,20,34.5]
fahrenheit=[((9/5)*temp +32) for temp in celcius]
print(fahrenheit)

results = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(results)

newlist=[]
for x in [2,4,6]:
    for y in [1,10,1000]:
        newlist.append(x*y)
print(newlist)

newlist2=[x*y for x in [2,4,6] for y in [1,10,1000]] #using list comprehension
print(newlist2)

st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':
        print(word)

print(list(range(0,11,2)))

stu = 'Print every word in this sentence that has an even number of letters'
for word in stu.split():
    if len(word)%2 == 0:
        print(word+" <-- has an even length!")

for num in range(1,60):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

str = 'Create a list of the first letters of every word in this string'
mynewlist=[word[0] for word in str.split()]
print(mynewlist)






