def methodception(another):
    return another()

def add_two_numbers():
    return 33+22

#jako argument funkcji podaje inna.. bez () bo methodception zwraca juz funkcje
# print(methodception(add_two_numbers))

# print(methodception(lambda: 33+22))

my_list = [12, 23, 11, 33, 442]

#usuwanie wszystkich ktore nie sa 13
print(list(filter(lambda x: x !=13, my_list)))
# jak list comperhantion:

print([x for x in my_list if x!=13])


(lambda x: x*3)(5)
#same as:

# def f(x):
#     return x * 3
#
# f(5)
