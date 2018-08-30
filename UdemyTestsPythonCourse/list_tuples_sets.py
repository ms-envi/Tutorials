

#list, append, delete etc, always ordered
grades = [70,80,90,90, 95,100]
#tuple - immutable cant be changed
tuple_grades = (70,80,90)
#set - unique, not ordered
set_grades = {70, 80, 90, 100,}

#
tuple_grades = tuple_grades + (100,)
grades.append(108)

##Set operations

set_one = {1,2,3,4,5}
set_two = {1,3,5,7,9,11}

print(set_one.intersection(set_two))

print(set_one.union(set_two))

print({1,2,3,4}.difference({1,2}))
