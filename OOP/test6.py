import test5
print(test5)
obj3 =  test5.person1(" rahul","rama",1996)
print(obj3.yob1)

print(obj3.yob1)
print(obj3._name1)
print(obj3._person1__surname1)

from utils.utils import Person3

obj4 = Person3("rahul","chandran",1998)
print(obj4.dob)
print(obj4._name)
print(obj4._Person3__surname)


class person:

    _name = "sudh"
    __surname = "kumar"
    yob = 1990

    def _age(self, current_year):
        return current_year - self.yob
    def __age1(self, current_year):
        return current_year - self.yob

obj = person()
print(obj)
print(obj._age(2022))
print(obj._person__age1(2022))

class employee(person):

    _name = "rahul"
    __surname = "rama"
    yob = 1991

    def __age1(self, current_year):
        return current_year - self.yob

obj1 = employee()
print(obj1)
print(obj1.yob)
print(obj1._name)
print(obj1._person__surname)
print(obj1._employee__surname)

print(obj1._age(2022))
print(obj1._person__age1(2022))
print(obj1._employee__age1(2022))




