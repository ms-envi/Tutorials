my_list = [0,1,2,3,4]

an_equal_list = [x for x in range(5)]
multiply_list = [x * 3 for x in range(5)]

print ([n for n in range(10) if n%2 == 0])


people_u_know = ["Rolf", "John", "anna", "GERG"]
normalised_people = [person.strip().lower() for person in people_u_know]
