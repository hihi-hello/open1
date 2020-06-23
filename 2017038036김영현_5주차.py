student1 = {}
student2 = {}
student3 = {}
student4 = {}
student5 = {}
students = [student1, student2, student3, student4, student5]


def print_menu():
    num = 0
    print("-----메뉴-----")
    print("1.데이터 추가\n2.데이터 검색\n3.데이터 삭제\n4.데이터 정렬\n0.프로그램 종료")
    num = int(input("실행할 메뉴의 번호를 입력하시오 : "))
    return num


def add_data():
    i = 0
    for i in range(0, 5, 1):
        students[i]["major"] = input("학과를 입력하시오 : ")
        students[i]["id"] = int(input("학번을 입력하시오 : "))
        students[i]["name"] = input("이름을 입력하시오 : ")
        students[i]["Kor"] = int(input("국어 점수를 입력하시오 : "))
        students[i]["Eng"] = int(input("영어 점수를 입력하시오 : "))
        students[i]["Math"] = int(input("수학 점수를 입력하시오 : "))
        students[i]["Total"] = students[i]["Kor"] + students[i]["Eng"] + students[i]["Math"]
        students[i]["Avg"] = students[i]["Total"] / 3
        students[i]["Grade"] = input("학점을 입력하시오 : ")


def find_data():
    sel = int(input("입력할 정보를 고르시오 (1.학번 2.이름) : "))
    if sel == 1:
        find = int(input("검색할 학생의 학번을 입력하시오 : "))
        if find == student1["id"]:
            print(students[0])
        elif find == student2["id"]:
            print(students[1])
        elif find == student3["id"]:
            print(students[2])
        elif find == student4["id"]:
            print(students[3])
        elif find == student5["id"]:
            print(students[4])
    elif sel == 2:
        find2 = input("검색할 학생의 이름을 입력하시오 : ")
        if find2 == student1["name"]:
            print(students[0])
        elif find2 == student2["name"]:
            print(students[1])
        elif find2 == student3["name"]:
            print(students[2])
        elif find2 == student4["name"]:
            print(students[3])
        elif find2 == student5["name"]:
            print(students[4])


def del_data():
    d1 = int(input("삭제할 학생의 학번을 입력하시오 : "))
    d2 = input("삭제할 학생의 이름을 입력하시오 : ")
    if d1 == students[0]["id"] and d2 == students[0]["name"]:
        del students[0]
    elif d1 == students[1]["id"] and d2 == students[1]["name"]:
        del students[1]
    elif d1 == students[2]["id"] and d2 == students[2]["name"]:
        del students[2]
    elif d1 == students[3]["id"] and d2 == students[3]["name"]:
        del students[3]
    elif d1 == students[4]["id"] and d2 == students[4]["name"]:
        del students[4]


def sort_data():
    met = int(input("정렬할 항목을 선택하시오 (1.학번순으로 2.이름순으로) : "))
    if met == 1:
        students = sorted(students, key=lambda x: x["id"])
    elif met == 2:
        students = sorted(students, key=lambda x: x["name"])
    print(students)


num = 1
print_menu()
while 0 < num < 5:
    if num == 1:
        add_data()
    elif num == 2:
        find_data()
    elif num == 3:
        del_data()
    elif num == 4:
        sort_data()



