# Alright, let's simplify and rephrase the problem set to avoid using functions:
import student_data

# print(student_data.students)
students = student_data.students
# print(len(students))
# print(students[4]['Combo,Name'])
# print(students[4]['Email'][0])
# print(students[4]['Email'][1])
# print(students[4]['HR'])
# print(students[4]['GL'])
# for loops allow us to
#iterate through the data
#and perform some function

#we are iterating through the data
#and printing the name and email of the students
#we are also printing a line of underscores to separate the students
#we are also printing a line of underscores to separate the students
# for student in students:
#     print(student['Combo,Name'])
#     print(student['Email'][0])
#     print(student['Email'][1])
#     print(student['MName'])
#     print(student['LName'])
#     print("_"*30)


# we are asking the user to input their name
# then we are checking if the name is in the data
# if the name is in the data we are printing the name and "this works"
# name = input("what is you name?") 
# id = int(input("What is your ID? "))
# for student in students:
#     if id == student['CPSID']:
#         print(student['Combo,Name'])
#         print("this works")


# Let's try to print out the emails of the students:    



homeroom = input('What is your homeroom? ')
#here I set found to False as a default
found = False
for student in students:
#This checks if what th user inputs is in the database,
#and if it is prints this
    if homeroom == student['HR']:
        print(student['Combo,Name'])
        print(student['Email'][0])
        print(student['Email'][1])
        found = True
#if the the students homeroom is found in the database. found
#changes into True
if not found: 
#if not found means if false, so it wouod print this out
        print("No students found in this homeroom.")

