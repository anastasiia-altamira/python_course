class Person:
    def __init__(self, name=None, surname=None, age=0):
        self.name = name
        self.surname = surname
        self.age = age

    def full_name(self):
        "Возвращает имя и фамилию человека"
       # return str(self.name) + " " + str(self.surname)
       # return "{} {}".format(self.name, self.surname) 
        f"{self.name} {self.surname}"

    def get_older(self, years):
        "Увеличивает возраст человека на заданное количество лет"
        if self.age is None:
            self.age = years
        else:
            self.age += years
        return self.age
    



if name == "__main__":
    p1 = Person("John", "Doe", 30)
    print(p1.full_name())
    p2 = Person()
    print(p2.full_name())
    print(p1.get_older(5))
    print(p2.get_older(10))