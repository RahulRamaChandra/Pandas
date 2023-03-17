class  Person :

    def __init__(self,name,surname,emailid, year_of_birth):
        self.name = name
        self.surname = surname
        self.emailid = emailid
        self.year_of_birth = year_of_birth
        self.full_name = name +","+ surname




"""    def __init__(self,name,surname,emailid, year_of_birth):
        self.name1 = name
        self.surname = surname
        self.emailid = emailid
        self.year_of_birth = year_of_birth"""

"""anuj_var = Person("anuj","bhandari", "anuj@gmail.com", 1994)
sudh = Person("Sudhanshu", "Kumar", "sudhanshu@gmail.com", 2324)
gargi = Person("Gargi","srehul", "Gargi@gmail.com",1234)
print(anuj_var.name)
print(sudh.name)
print(gargi.name)

print(type(sudh))"""



anuj_var = Person("anuj","bhandari", "anuj@gmail.com", 1994)
sudh = Person("Sudhanshu", "Kumar", "sudhanshu@gmail.com", 2324)
gargi = Person("Gargi","srehul", "Gargi@gmail.com",1234)
"""print(anuj_var.name1)
print(sudh.name1)
print(gargi.name1)"""

print(anuj_var.full_name)


print(type(sudh))
