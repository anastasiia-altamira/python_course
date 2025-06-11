from person import Person


class Employee(Person):
 def __init__(self, name=None, surname=None, age=None, salary = 0, position = None):
    super().__init__(name, surname, age)
    self.salary = salary
    self.position = position    


 def income(self, months=1):
       return self.salary * months

        

e = Employee("Alice", "Smith", 28, salary=1000)
print(e.name)
print(e.surname)
print(e.get_older(5))
print(e.age)
print(e.income(12))

class ITEmployee(Employee):
  #  def __init__(self, *args, **kwargs):
  #      super().__init__(*args, **kwargs)
   
    def __init__(self, name=None, surname=None, age=None, salary=0, position=None):
        super().__init__(name, surname, age, salary, position)
        self.skills = []
    
    def add_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)


ite = ITEmployee("Bob", "Johnson", 30, salary=1200, position="Developer")
ite.add_skill("Python")
print(ite.skills)