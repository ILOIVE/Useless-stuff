'''
get someones id (e.g. name, family name, id number and age) and put it in a dict.
if person was under 18, ask for student ID
if person was over 18, ask for current occupation

return the dict. as a text file
'''
import os


info_dict= {
    "First name" : "",
    "Last name" : "",
    "ID number" : "",
    "age" : "",
    "Student ID" : "N/A",
    "Occupation" : "N/A"
}



class AdultInfo:
    def __init__(self, first_name, last_name, id_number, age):
        self.fname = first_name
        self.lname = last_name
        self.id = id_number
        self.age = age

        info_dict.update({"First name" : self.fname})
        info_dict.update({"Last name": self.lname})
        info_dict.update({"ID number": self.id})
        info_dict.update({"age": self.age})

class StudentInfo(AdultInfo):
    def __init__(self,first_name, last_name, id_number, age, sID):
        super().__init__(first_name, last_name, id_number, age)
        self.sID = sID

        info_dict.update({"Student ID": self.sID})

class AdultOccupation(AdultInfo):
    def __init__(self, first_name, last_name, id_number, age, occupation):
        super().__init__(first_name, last_name, id_number, age)
        self.occ = occupation

        info_dict.update({"Occupation": self.occ})


a = input("Please enter your first name: ")
b = input("Please enter your last name: ")
c = int(input("Please enter your ID number: "))
d = int(input("Please enter your age: "))

AdultInfo(a,b,c,d)

def age_check(d):
    if d <= 18 :
        o = int(input("Please enter your student ID: "))
        StudentInfo(a,b,c,d,o)
        print(info_dict)
    if d > 18 :
        o = input("Please enter your occupation: ")
        AdultOccupation(a,b,c,d,o)
        print(info_dict)

age_check(d)

def create_text_file_from_dict():
    with open("info.txt","w") as f :
        f.write(f"{info_dict}")
        f.close()
create_text_file_from_dict()






