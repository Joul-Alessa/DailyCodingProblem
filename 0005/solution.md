## Personal implementation attempt in Python

I haven't read a lot about Lambda Calculus to get to know the field perfectly but with the concepts that I learned, I've been exploring this problem from the perspective of this field treating every entity as a function.

In this case, ```cons(a, b)``` returns a function type which encapsulates both two values from the problem's statement.

So for the solution I thought that it is posible to take the first element of the ```pair``` function to other function that asks for the entire function as a parameter in case of the ```car``` function and the same for the ```cdr``` function but taking the second element:

```py
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def first(a, b):
    return a

def second(a, b):
    return b

def car(pair):
    return pair(first)

def cdr(pair):
    return pair(second)
```

An upgrade I found while I was writing my solution was using the Python kyeword ```lambda``` due to the nature of the function which no require additional instructions in order to return its corresponding value. So my personal solution stands as follows:

```py
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    return pair(lambda a, b: a)

def cdr(pair):
    return pair(lambda a, b: b)
```