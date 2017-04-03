# Avinash Sharma
# Cole Grisby
# Lab 1

#object for students
class Student:
    def __init__(self, in_stlastname, in_stfirstname, in_grade, in_room, in_bus, in_gpa, in_tlastname, in_tfirstname) :
        self.stlastname = in_stlastname
        self.stfirstname = in_stfirstname
        self.grade = in_grade
        self.room = in_room
        self.bus = in_bus
        self.gpa = in_gpa
        self.tlastname = in_tlastname
        self.tfirstname = in_tfirstname

#student list
studentList = []

#read through students.txt
inputFile = open("students.txt", 'r')
while True:
    line = inputFile.readline()
    if len(line) == 0:
        break
    data = line.split(',')
    #add data to list
    studentList.append(Student(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))

#get user input commands
userInput = raw_input("Enter command ")


if userInput.startswith('S: ') or userInput.startswith('Student: '):
    print "find student"


inputFile.close()
