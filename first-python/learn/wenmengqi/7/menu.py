import student

def showMenu():
    print("-"*30)
    print(" 学生通讯录管理系统 v1.0")
    print("1.添加学生")
    print("2.删除学生")
    print("3.修改学生")
    print("4.查询学生")
    print("5.获取所有学生通讯信息")
    print("6.推出系统")
    print("-"*30)


def selectMenu():
    num = int(input("请输入:"))
    return num

def handleMenu():
    studentManage = student.StudentManage()
    while True:
        showMenu()
        num = selectMenu()
        if num == 1:
            name = input("输入学生姓名:")
            sex = input("输入学生性别:")
            mobile = input("输入学生手机号:")
            studentManage.addStudent(student.Student(name,sex,mobile))
            print("添加用户成功")
        elif num==2:
            name = input("输入学生姓名:")
            studentManage.deleteStudent(name)
            print("删除用户成功")
        elif num==3:
            print("修改用户成功")
        elif num==4:
            name = input("输入学生姓名:")
            stu = studentManage.searchStudent(name)
            print(stu)
            print("查询用户成功")
        elif num==5:
            stus = studentManage.searchAll()
            print(stus)
            print("查询所有通讯录信息成功")
        else:
            exit()