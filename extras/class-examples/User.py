import datetime
class User():
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
    def describe_user(self):
        print("Name: " + self.first_name + " " + self.last_name + ". DOB: " \
                + str(self.date_of_birth))
    def greet_user(self):
        if datetime.datetime.now().time() < datetime.time(12):
            print("Good morning " + self.first_name + "!")
        else:
            print("Good afternoon " + self.first_name + "!")

joe = User("Joe", "Durrant", datetime.date(1996,2,14))

joe.describe_user()