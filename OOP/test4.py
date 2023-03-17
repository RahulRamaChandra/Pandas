class person:

    def age(self, current_year, year_of_birth):
        return current_year - year_of_birth

    def email_id_input(self, email_id):
        print("take an email id from a person and print it", email_id)

    def ask_name(self):
        name = input("tell me your name")
        return name

    def ask_dob(self):
        dob = input("tell me your dob")
        return dob

sudh = person()
anuj = person()
krish = person()
hithesh = person()
gargi = person()

sudh.email_id_input("sudhanshukumar@gmail.com")
print(krish.ask_name())

print (hithesh.ask_dob())



