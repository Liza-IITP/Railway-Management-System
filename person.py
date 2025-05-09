class Person:
    def __init__(self, name, age, gender, user_id):
        self.name = name
        self.age = age
        self.gender = gender
        self.user_id = user_id
        
def view_profile(self):
        print("----- Profile -----")
        print(f"Name     : {self.name}")
        print(f"Age      : {self.age}")
        print(f"Gender   : {self.gender}")
        print(f"User ID  : {self.user_id}")