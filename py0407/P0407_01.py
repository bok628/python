# 파이썬은 클래스 없이 사용 가능
# 객체지향언어 - 고급언어
# 클래스(객체) : 다른 타입형태를 넣을 수 있음(변수&함수) 
# 1.변수,함수 모두 포함
# 2.변수에 대한 값을 확인,비교
# 3.캡슐화 : 변수에 직접접근을 막을 수 있음

# stu = [1,"홍길동",100,100,100,300,100.0,1]
# while True :
#     stu[2] = 300 # 직접접근 가능
#     print("1.학생출력")
#     choice = int(input("원하는 번호를 입력하세요. >> "))
#     if choice == 1 :
#         print(stu)

# class + __(첫글자 대문자 사용)
# 설계도

# class Stu :
#     pass

# s = Stu()  # 클래스 선언
# s1 = Stu() 
# s.no = 1        # 변수 선언
# s.name = "홍길동"
# s.kor = 100

# print(s.no)

class Stu:
    # 생성자(init) : 클래스가 선언될 때 데이터를 받아서 변수에 저장하는 함수
    def __init__(self,no,name,kor,eng,math,total,avg,rank) :   # class안에 변수를 넣고 싶을 때 : self 사용
        self.no = no        # 클래스 안에 변수 선언
        self.name = name
        if kor > 0 and kor <=100 :   # else : kor에 데이터 입력 X
            self.kor = kor
        self.__eng = eng            # __변수명 : 접근권한 막을 수 있음
        self.math = math
        self.total = total
        self.avg = avg
        self.rank = rank
        

s = Stu(1,"홍길동",100,100,100,300,100.0,1)
print(s.eng)
