# Avinash Sharma
# Cole Grisby
# CPE 365 Lab 1

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

#empty list to store each student
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

inputArray = userInput.split(' ')

resultsArray = []

#function to search for student last name
def studentLastName(results, students, inArr):
    for i in range(0, len(students)):
        if students[i].stlastname == inArr[1]:
            results.append(students[i])

#function to search for teacher last name
def teacherLastName(results, students, inArr):
    for i in range(0, len(students)):
        if students[i].tlastname == inArr[1]:
            results.append(students[i])

if len(inputArray) == 2:
    #R4 S[tudent]: <lastname> 
    #check if input is for student lastname
    if inputArray[0] == "S:" or inputArray[0] == "Student:":
        studentLastName(resultsArray, studentList, inputArray)
        for i in range(0, len(resultsArray)):
            print resultsArray[i].stlastname + "," + resultsArray[i].stfirstname + "," + resultsArray[i].grade + "," + resultsArray[i].room + "," + resultsArray[i].tlastname + "," + resultsArray[i].tfirstname,
    #R6 T[eacher]: <lastname>
    #check if input is for teacher lastname
    elif inputArray[0] == "T:" or inputArray[0] == "Teacher:":
        teacherLastName(resultsArray, studentList, inputArray)
        print len(resultsArray)
        for i in range(0, len(resultsArray)):
            print resultsArray[i].stlastname + "," + resultsArray[i].stfirstname
    
#R5 S[tudent]: <lastname> [B[us]]
#check if input is for student lastname and bus route
elif len(inputArray) == 3:
    if inputArray[0] == "S:" or inputArray[0] == "Student:":
        if inputArray[2] == "B" or inputArray[2] == "Bus":
            studentLastName(resultsArray, studentList, inputArray) 
            for i in range(0, len(resultsArray)):
                print resultsArray[i].stlastname + "," + resultsArray[i].stfirstname + "," + resultsArray[i].bus,


inputFile.close()
