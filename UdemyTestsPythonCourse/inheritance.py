class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)


#mozna zastapic salary na *args, i zazwyczaj i tak sie dodaje **kwargs
    @classmethod
    def friend(cls, origin, friend_name, *args, **kwargs):
        return cls(friend_name, origin.school, *args, **kwargs )

## workingStudent contains everything what class Student
## inherit is not cloning.. we can reimplement methods with more stuff
## musimy wezwac super() !! bo Student jest powyzej,, i trzeba ja wczesniej dodac


class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name,school)
        self.salary = salary


anna = WorkingStudent("Anna", "Oxford", 25.00, job_title="test eng")

print(anna.salary)

#anna bedzie origin
friend = WorkingStudent.friend(anna,"Greg",17, "Dev")

print(friend.name)
print(friend.school)

#print(friend.salary)  -- tu sie wywali, bo student oryginalna klasa nie ma salary
# jesli dodamy classmethod do def friend, to wtedy wywolanie tej metody bedzie na
# klasie wyzszej, czyli w tym przypadku na WorkingStudent ktory juz ma Salary i bedzie dzialac

print(friend.salary)
