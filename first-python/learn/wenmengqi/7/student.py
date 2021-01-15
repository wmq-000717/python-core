import static as static

class Student:
    def __init__(self,name,sex,mobile):
        self.name = name
        self.sex = sex
        self.mobile = mobile

    def showInfo(self):
        print("name:%s,sex:%s,mobile:%s"%(self.name,self.sex,self.mobile))



class StudentManage:
    def __init__(self):
        self.studentList = []

    def addStudent(self,student):
        self.studentList.append(student)

    def deleteStudent(self,student):
        self.studentList.remove(student)

    def searchStudent(self,name):
        for student in self.studentList:
            if student.name ==  name:
                return student;

    def searchAll(self):
        return self.studentList;