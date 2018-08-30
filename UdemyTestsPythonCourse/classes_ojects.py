lotter_player_dict = {
'name:':'Rolf',
'number':(5,7,4,2,3,44,5)
}

class LotteryPlayer:
    def __init__(self,name):
        self.name=name,
        self.numbers=(5,7,4,2,3,44,5)

    def total(self):
        return sum(self.numbers)

player_one = LotteryPlayer("Dupa")
player_two = LotteryPlayer("John")
player_three = LotteryPlayer("Laa")


print(player_one.name == player_two.name)

##

class Student:
    def __init__(self, name, school):
        self.name=name
        self.school=school
        self.marks=[]

    def average(self):
        return sum(self.marks)/len(self.marks)

#mozemy usunac 'self' za argument  cls - to nasza klasa student
# @classmethod
#     def go_to_school(cls):
#         print("Im going to school.")
#         print("Im a {}".format(cls))


#albo dac jako metoda statyczna i bezposrednio wywolywac na kalsie Student

    @staticmethod
    def go_to_school():
        print(Im going to school)

Student.go_to_school()



anna = Student("Anna","MIT")
anna.marks.append(71)
anna.marks.append(56)
print(anna.marks)
