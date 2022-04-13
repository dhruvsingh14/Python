########## Module 2: Overview ##########

## Overview
# shebang line, first line in program
#!/usr/bin/env python3

# alternately, if we don't know the location of python 3: 
#!/usr/local/bin/python3

########## Module 5: Operators ##########

# Bitwise operators
x = 0x0a # hexadecimal litereal numbers
y = 0x02
z = x & y

print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')

# Comparison

x = 42
y = 73

if x > y:
    print('comparison is true')
else: 
    print('comparison is false')

# Boolean
a = True
b = False
x = ('bear', 'bunny', 'tree', 'sky', 'rain')
y = 'bear'

if y is x[0]:
    print('expression is true')
else: 
    print('expression is false')

########## Module 7: Functions ##########

# defining

def main(): # foreward declaration
    x = kitten()
    print(x)
    
def kitten():
    return 'Meow.'

if __name__ == '__main__':main() # this will return the name of the current module
                                # workaround for forward declarations

# function arguments
def main():
    x = [5] # integers are immutable
    kitten(x)
    print(f"in main: x is {x}")
    
def kitten(a):
    a[0] = 3
    print('Meow.')
    print(a)

if __name__ == '__main__': main()

# argument lists
def main():
    x = ('meow', 'grrr', 'purr', 'hello', 'world')
    kitten(*x)

def kitten(*args): # variable length argument list, actually a tuple
    if len(args):
        for s in args:
            print(s)
    else: print('Meow.')

if __name__ == '__main__': main()

# keyword arguments
def main():
    x = dict(Buffy = 'meow', Zilla = 'grrr', Angel = 'rawr')
    kitten(**x)

def kitten(**kwargs): # similar to list arguments, dictionaries instead of tuples
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else: print('Meow.')

if __name__ == '__main__': main()

# return values
def main():
    x = kitten()
    print(type(x), x)
    
def kitten():
    print('Meow.')
    return dict(x = 42, y = 43, z = 44)

if __name__ == '__main__':main()

# generators
def main():
    for i in inclusive_range(25):
        print(i, end = ' ')
    print()

def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1

    # initialize parameters
    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError(f'expected at most 3 arguments, got {numargs}')

    # generator
    i = start
    while i <= stop:
        yield i
        i += step

if __name__ == '__main__': main()

# decorators
def f1(f):
    def f2():
        print('this is before the function call')
        f()
        print('this is after the function call')
    return f2

@f1 # decorator, takes funct directly after it, takes func as arg, and assigns it to wrapper itself
def f3(): # function definition
    print('this is f3')

f3()

# example: use case for decorators
import time

def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1) * 1000} ms')
    return wrapper

@elapsed_time
def big_sum():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print(f'Big sum: {sum(num_list)}')

def main():
    big_sum()

if __name__ == '__main__': main()

########## Module 8: Structured Data ##########

# list comprehension
def main():
    seq = range(11)
    from math import pi
    # seq2 = [x for x in seq if x % 3 != 0] # if clause only allowed after for clause
    # seq2 = [(x, x**2) for x in seq] # list of tuples
    # seq2 = [round(pi, i) for i in seq]
    # seq2 = {x: x**2 for x in seq} # comprehension for dictionaries
    seq2 = {x for x in 'superduper' if x not in 'pd'} # comprehension for sets
    print_list(seq)
    print_list(seq2)
    #print(seq2)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()

########## Module 9: Classes ##########

# creating a class
class Duck:
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'

    def quack(self):
        print(self.sound)

    def move(self):
        print(self.movement) # dot operator dereferences the object

def main():
    donald = Duck()
    # donald.quack() # quack method, called on object donald
    print(donald.sound) # same result
    donald.move()

if __name__ == '__main__': main()

# constructing an object
class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten' # default value
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'rwar'

    # alternate way:
    # def __init__(self, type, name, sound): # two underscore characters
        #self._type = type
        #self._name = name
        #self._sound = sound

    def type(self):
        return self._type
    
    def name(self):
        return self._name

    def sound(self):
        return self._sound

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))

def main(): # constructor
    #a0 = Animal('kitten', 'fluffy', 'rwar') # creating objects, from the animal class
    #a1 = Animal('duck', 'donald', 'quack') # initializing objects with various parameters
    a0 = Animal(type='kitten', name='fluffy', sound='rwar')
    a1 = Animal(type='duck', name='donald', sound='quack')
    print_animal(a0)
    print_animal(a1)
    #print_animal(Animal('velociraptor', 'veronica', 'hello'))
    print_animal(Animal(type='velociraptor', name='veronica', sound='hello'))
    print_animal(Animal())

if __name__ == '__main__': main()

# class methods
class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten' 
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'rwar'

    def type(self, t = None): # serves as both a getter, and setter
        if t: self._type = t # _ in name indicates private variable
        return self._type
    
    def name(self, n = None): # getter / setter
        if n: self._name = n
        return self._name

    def sound(self, s = None): # first arg 'self' makes this a method, and not a plain function
        if s: self._sound = s
        return self._sound

    def __str__(self): # special method, provides str representation of object
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

def main(): # constructor
    a0 = Animal(type='kitten', name='fluffy', sound='rwar')
    a1 = Animal(type='duck', name='donald', sound='quack')
    a0.sound('bark') # changing sound using sound function for a0 object
    print_animal(a0)
    print_animal(a1)

if __name__ == '__main__': main()

# object data
class Animal:
    #x = [1, 2, 3] # class variable, not object var
                    # defined in class, not in any method
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten' # object variables
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'rwar'

    def type(self, t = None): 
        if t: self._type = t 
        return self._type
    
    def name(self, n = None):
        if n: self._name = n
        return self._name

    def sound(self, s = None):
        if s: self._sound = s
        return self._sound

    def __str__(self): 
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

def main(): 
    a0 = Animal(type='kitten', name='fluffy', sound='rwar')
    a1 = Animal(type='duck', name='donald', sound='quack')    
    print_animal(a0)
    print_animal(a1)

    #print(a0.x)
    #a1.x[0] = 7 # changed in a1
    #print(a0.x) # printing from a0, still changed, bc var not attached to object, only class
                # ie, x variable is not 'encapsulated'

if __name__ == '__main__': main()


# inheritance
class Animal:
    def __init__(self, **kwargs):
        if 'type' in kwargs: self._type = kwargs['type'] # init method, no longer providing default values
        if 'name' in kwargs: self._name = kwargs['name'] # this is now just going to be a base class
        if 'sound' in kwargs: self._sound = kwargs['sound'] # going to be inherited in order to be used

    def type(self, t = None): 
        if t: self._type = t 
        try: return self._type
        except AttributeError: return None
    
    def name(self, n = None):
        if n: self._name = n
        try: return self._name
        except AttributeError: return None

    def sound(self, s = None):
        if s: self._sound = s
        try: return self._sound
        except AttributeError: return None

    def __str__(self): 
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

class Duck(Animal): # to use base class, inheriting it to create other classes
    def __init__(self, **kwargs):
        self._type = 'duck' # setting type
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs) # super always calles the parent class (initializer)

class Kitten(Animal):
    def __init__(self, **kwargs):
        self._type = 'kitten'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs)

    # special case: define a method that doesn't exist
    def kill(self, s):
        print(f'{self.name()} will now kill all {s}!')

def main(): 
    a0 = Kitten(name='fluffy', sound='rwar')
    a1 = Duck(name='donald', sound='quack')    
    print_animal(a0)
    print_animal(a1)
    a0.kill('humans')
    #a1.kill('humans') # won't work

if __name__ == '__main__': main()

# example use case for inheritance
class RevStr(str):
    def __str__(self): # using built in method to extend class
        return self[::-1]

def main():
    hello = RevStr('Hello, World.') # using inheritance to reverse string
    print(hello)

if __name__ == '__main__': main()

# iterator objects
class inclusive_range:
    def __init__(self, *args): # constructor
        numargs = len(args)
        self._start = 0
        self._step = 1

        if numargs < 1:
            raise TypeError(f'expected at least 1 argument, got {numargs}')
        elif numargs == 1:
            self._stop = args[0] # checks the arguments
        elif numargs == 2:
            (self._start, self._stop) = args
        elif numargs == 3:
            (self._start, self._stop, self._step) = args
        else: raise TypeError(f'expected at most 3 arguments, got {numargs}')

        self._next = self._start

    def __iter__(self): # special iterator method
        return self # identifies this as an iterator object

    def __next__(self): # the iteration itself
        if self._next > self._stop:
            raise StopIteration # exception
        else:
            _r = self._next
            self._next += self._step # increment
            return _r # iterators pre-dated generators. hence no yield here. 

def main():
    for n in inclusive_range(5, 25, 3):
        print(n, end=' ')
    print()

if __name__ == '__main__': main()