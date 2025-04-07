from sModule import *


students = Students()
title = ['번호','이름','국어','영어','수학','합계','평균','순위']

def stu_title() :
    print("[ 학생 성적 프로그램 ]")
    print("-"*60)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("0. 프로그램 종료")
    print("-"*60)
    
    choice = 0
    choice = (input("번호를 입력하세요. >> "))
    try :
        choice = int(choice)
    except Exception as e :
        print(e)
    return choice 

def stu_in() :
    score = [0] * 3
    print("[ 학생성적입력 ]")
    print("-"*60)
    name = input(f"{Student.count}번 학생 이름을 입력하세요. >> ")   # 클래스변수로 사용
    for i in range(len(score)) :
        score[i] = int(input(f"{title[i + 2]} 점수를 입력하세요. >> "))
    print(f"{Student.count}번 {name}학생의 성적이 입력되었습니다.")
    students.add(Student(name,*score))
    # score[0],score[1],score[2]
    
def stu_out() :
    print("[ 학생성적출력 ]")
    print("-"*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
    print("-"*60)
    for s in students.students :  # students.students. 처음 스튜던츠 : 스튜던츠 클래스 불러오기 두번째 : 클래스에 있는 리스트 불러오기
        print(f"{s.no}\t{s.name}\t{s.kor}\t{s.eng}\t{s.math}\t{s.total}\t{s.avg:.2f}\t{s.rank}")
    print()