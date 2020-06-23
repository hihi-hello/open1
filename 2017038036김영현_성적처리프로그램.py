class Student:
    def __init__(self):
        self.name = input("학생 이름을 입력하세요 : ")
        self.hakbun = int(input("학번을 입력하세요 : "))
        self.major = input("학과를 입력하세요 : ")
        self.kor = int(input("국어 점수를 입력하시오 : "))
        self.eng = int(input("영어 점수를 입력하시오 : "))
        self.math = int(input("수학 점수를 입력하시오 : "))
        self.total = self.kor + self.eng + self.math
        self.avg = self.total_score / 3
        if self.avg >= 95:
            self.GPA = "A+"
        elif self.avg >= 90:
            self.GPA = "A0"
        elif self.avg >= 85:
            self.GPA = "B+"
        elif self.avg >= 80:
            self.GPA = "B0"
        elif self.avg >= 75:
            self.GPA = "C+"
        elif self.avg >= 70:
            self.GPA = "C0"
        elif self.avg >= 65:
            self.GPA = "D+"
        elif self.avg >= 60:
            self.GPA = "D0"
        else:
            self.GPA = "F"

    def print_info(self):
        print('이름 :', self.name, '/학번 :', self.hakbun, '/학과 :', self.major)
        print('국어 :', self.kor, '점/ 영어 :', self.eng, '점/ 수학 :', self.math, '점')
        print('총점 :', self.total_score, '/평균 :', self.avg, '/학점 :', self.GPA, '\n')


class ScoreManagement:
    def __init__(self):
        self.list = []

    def print_menu(self):
        print("1. 데이터 추가")
        print("2. 데이터 검색")
        print("3. 데이터 삭제")
        print("4. 데이터 정렬")
        print("0. 종료\n")

    def add_list(self):
        self.list.append(Student())

    def search_std(self):
        tmp = input("학생 이름 또는 학번을 입력하세요 : ")
        flg = 0
        ret = []
        if tmp.isdigit():
            tmp = int(tmp)
            for std in self.list:
                if std.hakbun == tmp:
                    pass
                    std.print_info()
                    ret.append(std)
                    flg = 1
        else:
            for std in self.list:
                if std.name == tmp:
                    std.print_info()
                    ret.append(std)
                    flg = 1
        if flg == 0:
            print("해당 학생의 정보가 없습니다.")
        else:
            return ret

    def delete_std(self):
        tmp = self.search_std()
        if tmp:
            for std in tmp:
                self.list.remove(std)
            print('출력된 정보를 삭제합니다.')

    def sort_std(self):
        print("1. 이름으로 정렬")
        print("2. 학번으로 정렬")
        tmp = int(input("정렬 방법을 선택해 주세요 : "))

        if tmp == 1:
            self.list = sorted(self.list, key=lambda x: x.name)
            print("이름으로 정렬한 값을 출력합니다.")
        elif tmp == 2:
            self.list = sorted(self.list, key=lambda x: x.hakbun)
            print("학번으로 정렬한 값을 출력합니다.")
        else:
            print("잘못입력하셨습니다.")
            return

        for std in self.list:
            std.print_info()


mng = ScoreManagement()
num = 1
while num:
    mng.print_menu()
    num = int(input("메뉴를 선택하세요 : "))

    if num == 1:
        mng.add_list()
    elif num == 2:
        mng.search_std()
    elif num == 3:
        mng.delete_std()
    elif num == 4:
        mng.sort_std()
    elif num == 0:
        print('프로그램을 종료합니다.')