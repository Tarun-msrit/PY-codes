class Animal():
    def __init__(self):
        print("ANIMAL CREATED")

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
         print("EATING")

mya =Animal()
mya.whoAmI()
mya.eat()
print("\n")
class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)   #not necessary
        print("DOG CREATED")

    def bark(self):           #its method
        print("WOOF")

    def eat(self):                #overwrite eat
         print("DOG EATING")

myd = Dog()
myd.whoAmI()
myd.eat()
myd.bark()

#special methods
class Book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def __str__(self):
        return "Title:{},Author:{},Pages:{}".format(self.title,self.author,self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print(("A book is destroyed"))
b=Book("Python","Jose",200)
print(b)
print(len(b))
del(b)

