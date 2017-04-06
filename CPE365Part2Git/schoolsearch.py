# Avinash Sharma
# Cole Grisby
# CPE 365 Lab 1

#object for students
class Student:
    def __init__(self, in_stlastname, in_stfirstname, in_grade, in_room, in_bus, in_gpa):
        self.stlastname = in_stlastname
        self.stfirstname = in_stfirstname
        self.grade = in_grade
        self.room = in_room
        self.bus = in_bus
        self.gpa = in_gpa

#object for teachers
class Teacher:
    def __init__(self, in_tlastname, in_tfirstname, in_room):
        self.tlastname = in_tlastname
        self.tfirstname = in_tfirstname
        self.room = in_room

# Traceability: implements requirements R3, R4
#function to search for student last name

def studentLastName(teachResults, results, students, teachers, inArr):
    for s in students:
        if s.stlastname == inArr[1]:
            results.append(s)
    for t in teachers:
        for r in results:
            if r.room == t.room:
                teachResults.append(t)

# Traceability: implements requirements R3, R6

#function to search for teacher last name
def teacherLastName(teachResults, results, students, teachers, inArr):
    for t in teachers:
        if t.tlastname == inArr[1]:
            teachResults.append(t)
    for t in teachResults:
        for s in students:
            if s.room == t.room:
                results.append(s)

# Traceability: implements requirements R3, R7

#function to search for same grade (0-6)
def gradeNumber(results, students, inArr):
    for s in students:
        if s.grade == inArr[1]:
            results.append(s)


# Traceability: implements requirements R3, R8

#function to search for same bus route
def busRoute(results, students, inArr):
    for s in students:
        if s.bus == inArr[1]:
            results.append(s)

# Traceability: implements requirements R3, R9

#function to search for the highest student in a grade
def gradeTop(teachResults, results, students, teachers, inArr):
    gradeNumber(results, students, inArr)
    if len(results) > 0:
        max = results[0]
        for s in results:
            if float(s.gpa) > float(max.gpa):
                max = s
        for t in teachers:
            if t.room == max.room:
                teachResults.append(t)
        return max

# Traceability: implements requirements R3, R9
#function to search for the lowest student GPA in a grade
def gradeLow(teachResults, results, students, teachers, inArr):
    gradeNumber(results, students, inArr)
    if len(results) > 0:
        min = results[0]
        for s in results:
            if float(s.gpa) < float(min.gpa):
                min = s
        for t in teachers:
            if t.room == min.room:
                teachResults.append(t)
        return min



# Traceability: implements requirements R3, R10

#function to find the average gpa of a grade
def average(results, students, inArr):
    gradeNumber(results, students, inArr)
    sum = 0
    for s in results:
        sum += float(s.gpa)
    if len(results) == 0:
        return 0
    return sum/len(results)

# Traceability: implements requirements R3, R11

#function to find the info for students
def info(results, students, inArr):
    for g in range(0,7):
        r = []
        gradeNumber(r, students, [0, str(g)])
        results.append(len(r))

# Traceability: implements requirement NR1

# method to list all students from a classroom
def classRoomStudents(results, students, inArr):
    for s in students:
        if s.room == inArr[1]:
            results.append(s)


# Traceability: implements requirement NR2

# method to list all teachers from a classroom
def classRoomTeachers(results, teachers, inArr):
    for t in teachers:
        if t.room == inArr[1]:
            results.append(t)

# Traceability: implements requirement NR3

# method to list all students from a classroom
def gradeTeachers(results, teachers, inArr):
    for t in teachers:
        if t.grade == inArr[1]:
            results.append(t)

# Traceability: implements requirement NR4

# method to list all students from a classroom
def classRoom(results, students, inArr):
    #Todo make a list of the enrollment numbers for room
    dict = {}
    for s in students:
        if dict.has_key(s.room):
            dict[s.room] = dict[s.room] + 1
        else:
            dict[s.room] = 1
    results = dict






# Traceability: implements requirements R3 through R13, E1

#get user input commands
def runProg():
    #empty list to store each student
    studentList = []

    #empty list to store each teacher
    teacherList = []
    
    # TRACE E1 if file doesn't exist
    #read through students.txt

    #MAKE SURE IT'S THE CORRECT TEXT FILES!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    try:
        inputListFile = open("list.txt", 'r')
        inputTeachFile = open("teachers.txt", 'r')
    except:
        return
    while True:
        line1 = inputListFile.readline()
        
        if len(line1) == 0:
            break
        data1 = line1.replace(" ", "").split(',')
        
        #add data to list
        studentList.append(Student(data1[0],data1[1],data1[2],data1[3],data1[4],data1[5].rstrip('\n')))

    while True:
        line2 = inputTeachFile.readline()
        
        if len(line2) == 0:
            break

        #MAKE SURE THIS IS RIGHT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        data2 = line2.replace(" ", "").split(',')
        
        #add data to list
        teacherList.append(Teacher(data2[0],data2[1],data2[2].rstrip('\n')))
    
    #run program inputs R1 R2
    while True:
        userInput = raw_input("Please Enter Command: ")

        inputArray = userInput.split()
        
        resultsArray = []
        teachResultsArray = []
        if len(inputArray) == 1:
                #R11 [info]
            if inputArray[0] == "I" or inputArray[0] == "Info":
                info(resultsArray, studentList, inputArray)
                g = 0
                for n in resultsArray:
                    print str(g) +": "+ str(n)
                    g += 1
            #R12 Q[uit]
            #quit the current session
            elif inputArray[0] == "Q" or inputArray[0] == "Quit":
                inputListFile.close()
                inputTeachFile.close()  
                break
    
    
        if len(inputArray) == 2:
            #R4 S[tudent]: <lastname> 
            #check if input is for student lastname
            if inputArray[0] == "S:" or inputArray[0] == "Student:":
                studentLastName(teachResultsArray, resultsArray, studentList, teacherList, inputArray)
                for r in resultsArray:
                    for t in teachResultsArray:
                        print r.stlastname + "," + r.stfirstname + "," + r.grade + "," + r.room + "," + t.tlastname + "," + t.tfirstname
                
            #R6 T[eacher]: <lastname>
            #check if input is for teacher lastname
            elif inputArray[0] == "T:" or inputArray[0] == "Teacher:":
                teacherLastName(teachResultsArray, resultsArray, studentList, teacherList, inputArray)
                for r in resultsArray:
                    print r.stlastname + "," + r.stfirstname
            #R7 G[rade]: <Number>
            #check if input is for grade number
            elif inputArray[0] == "G:" or inputArray[0] == "Grade:":
                gradeNumber(resultsArray, studentList, inputArray)
                for r in resultsArray:
                    print r.stlastname + "," + r.stfirstname
            #R8 B[us]: <Number>
            elif inputArray[0] == "B:" or inputArray[0] == "Bus:":
                busRoute(resultsArray, studentList, inputArray)
                for r in resultsArray:
                    print r.stlastname + "," + r.stfirstname + "," + r.grade + "," + r.room
            
            #R10 A[verage]: <number>
            elif inputArray[0] == "A:" or inputArray[0] == "Average:":
                a = average(resultsArray, studentList, inputArray)
                print inputArray[1] +": "+ str(a)
        
                    
        #R5 S[tudent]: <lastname> [B[us]]
        #check if input is for student lastname and bus route
        elif len(inputArray) == 3:
            if inputArray[0] == "S:" or inputArray[0] == "Student:":
                if inputArray[2] == "B" or inputArray[2] == "Bus":
                    studentLastName(teachResultsArray, resultsArray, studentList, teacherList, inputArray) 
                    for r in resultsArray:
                        print r.stlastname + "," + r.stfirstname + "," + r.bus
            #R9 G[rade]: <Number>
            elif inputArray[0] == "G:" or inputArray[0] == "Grade:":
                #R9 G[rade]: <Number> H[igh]
                if inputArray[2] == "H" or inputArray[2] == "High":
                    r = gradeTop(teachResultsArray, resultsArray, studentList, teacherList, inputArray)
                    if r is not None:
                        for t in teachResultsArray:
                            print r.stlastname + "," + r.stfirstname + "," + r.gpa + "," + t.tlastname + "," + t.tfirstname[:-1] + "," + r.bus
                elif inputArray[2] == "L" or inputArray[2] == "Low":
                    r = gradeLow(teachResultsArray, resultsArray, studentList, teacherList, inputArray)
                    if r is not None:
                        for t in teachResultsArray:
                            print r.stlastname + "," + r.stfirstname + "," + r.gpa + "," + t.tlastname + "," + t.tfirstname[:-1] + "," + r.bus




# Traceability: implements requirements R1, R2

runProg()