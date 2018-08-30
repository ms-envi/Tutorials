# should_continue = True
# if should_continue:
#     print ("hello")
#
#
# known_people = ["John", "Anna", "Mary"]
# person = input("Entern name:")
#
#
# if person in known_people:
#     print ("U know {}!".format(person))
# else:
#     print ("U dont know {}".format(person))

def who_do_you_know():
    peeps_they_know = input("Gimme list of ur friends: ")
    peeps_they_know_list = peeps_they_know.split(",")

    people_withou_spaces = [peps.strip().lower() for peps in peeps_they_know_list]
    return people_withou_spaces


def ask_user():
    name = input("Whats ur name: ").lower()
    for names in who_do_you_know():
        if names == name:
            return print ("Ya know yrself")
        else:
            return print ("Ya dont know yrself")


ask_user()
