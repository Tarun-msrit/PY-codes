x=0
while x < 5:
    print(f'The current value of x is {x}')
    x=x+1
else:
    print("X is not less than 5")


m=[1,2,3]
for item in m:
    #comment
    pass

print('end of my script')
mystring='Sammy'
for letter in mystring:
    if letter =='a':
        continue
    print(letter)

print('\n\n')
for letter in mystring:
    if letter =='m':
        break
    print(letter)

