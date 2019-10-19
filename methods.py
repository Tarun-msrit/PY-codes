mylist = [1, 2, 3]
help(mylist.insert)


def add_function(num1, num2):
    return num1 + num2


result = add_function(1, 2)
print(result)


def name_function():
    '''
    DOCSTRING: Information about the function
    Input: no input
    Output: Hello
    '''
    print('Hello')


name_function()


def hello(name='tarun'):  # default name
    print('hello ' + name)


hello('david')


def add(n1, n2):
    return n1 + n2


add_result = add(20, 30)
print(add_result)


def dog_check(mystring):
    if 'dog' in mystring.lower():
        return True
    else:
        return False


stringfun = dog_check('hello Mog')
print(stringfun)


# Pig latin function

def pig_latin(word):
    first_letter = word[0]
    # check vovel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word


newstr = pig_latin('amazing')
print(newstr)


# args and #kwargs

def myfunc(*args):  # returns tuple
    return sum(args) * 0.05


result = myfunc(40, 60)
print(result)
print('\n')


def newfunc(*args):
    for item in args:
        print(item)


newfunc(3, 4, 5, 6)


def myfunc2(**kwargs):  # returns dictionary
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')
myfunc2(fruit='apple',veggie ='lettuce')
print('\n')

def myfunc3(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))
myfunc3(10,20,30,fruit='orange',food='chocolates',animal='dog')



def square(num):
    return num**2
my_nums=[1,2,3,4,5]

for item in map(square,my_nums):
    print(item)
print(list(map(square,my_nums)))

def check_even(num):
    return num%2 == 0
mynums=[1,2,3,4,5,6]
print(list(filter(check_even,mynums)))

cube = lambda nim : nim**3
print(list(map(lambda nim : nim**3,mynums)))
print(list(map(cube,mynums )))
print(list(filter(lambda nom:nom%2 == 0,mynums)))