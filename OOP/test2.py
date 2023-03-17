class  Person :

    def __init__(sudh,name,surname,emailid, year_of_birth):
        sudh.name = name
        sudh.surname = surname
        sudh.emailid = emailid
        sudh.year_of_birth = year_of_birth

    def age(sudh, current_year):
        return current_year - sudh.year_of_birth

anuj_var = Person("anuj","bhandari", "anuj@gmail.com", 1994)
sudh = Person("Sudhanshu", "Kumar", "sudhanshu@gmail.com", 1997)
gargi = Person("Gargi","srehul", "Gargi@gmail.com",1234)

print(sudh.age(2022))
print(anuj_var.age(2022))

print(anuj_var.name)
print(sudh.name)
print(gargi.name)

print(type(sudh))

print(anuj_var.name + "," + anuj_var.surname)