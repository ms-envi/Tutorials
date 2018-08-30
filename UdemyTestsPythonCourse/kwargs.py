def my_method(arg1, arg2):
    return arg1 + arg2

my_method(5,6)


def my_long_method(arg1, arg2, arg3, arg4, arg5):
    return arg1 + arg2 + arg3 +arg4 +arg5

def my_list_addition(list_arg):
    return sum (list_arg)


my_long_method(3,4,5,6,7,8)
my_list_addition([2,4,6,2])

#zamiast podawac wszystkie, mozna zrobic tak *arg to lista argumentow
 def addition_simplified(*args):
     return sum(args)

addition_simplified(3,5,7,12,14,55)

##

def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

what_are_kwargs(12, 34, 56)  #zwroci tuple (12,34,56) i pusty staticmethod

what_are_kwargs(12, 24, 56, name='Jose', location='UK') # zwroci to samo plus dictionary z name i location

# positional arguments are following kwargs, te argumenty co maja name, zawsze musza byc na koncu

what_are_kwargs(56, name='Laaa', location='Sara')
