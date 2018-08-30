import functools


#tworzenie decoratora ktory printuje przed i po mojej fukcji
#w deokarotrze zawsze musi byc jakas funkcja, bo inaczej jak sie go gdzied doda to ta funkcja z dekoratorem sie nie wykona, tylko to co w dekoratorze

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the decorator!")
        func()
        print("After the decorator!")
    return function_that_runs_func

@my_decorator
def my_function():
    print("Im the function!")

# my_function()


## dekorators with arguments

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print ("in the decorator")
            if number==56:
                print("Not running the func")
            else:
            func(*args, **kwargs)
            print("After the decorator")
        return function_that_runs_func
    return my_decorator

##ags i kwargs warto dodac, zeby potem moc uzyc czegos w funkcji wnad ktora jest dekorator
##func w dekoratorze to jest ta funkcja ktora ma nad soba dekorator

@decorator_with_arguments(66)
def my_function_two():
    print("Hello")

my_function_two()
