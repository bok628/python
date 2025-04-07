# 1. sModule.py - class 2개 생성
# 2. sMain.py - sModule을 사용하여 프로그램 구현
# 3. sFunc.py 함수 옮기기

from sModule import *
from sFunc import *



while True :
    choice = stu_title()
    
    if choice == 1 :
        count = stu_in()
              
    elif choice == 2 :
        stu_out()
    
    elif choice == 3 :
        print("[ 학생성적수정 ]")
        name = input("수정할 학생의 이름을 입력하세요. >> ")
        temp = 0
        for s in students.students :
            if s.name == name :
                temp = 1
                choice = int(input(f"{name} 학생을 찾았습니다. \n1.국어\n2.영어\n3.수학\n 수정할 과목의 번호를 입력하세요.(0.이전화면이동) >> "))
                if choice == 1 :
                    pre_score = s.kor
                    new_score = input(f"현재 {title[choice + 1]} 점수 : {pre_score} \n변경할 점수를 입력하세요. >> ")
                    s.kor = new_score
                    print(f"{new_score}점으로 변경되었습니다.")
                elif choice == 2 :
                    pre_score = s.eng
                    new_score = input(f"현재 {title[choice + 1]} 점수 : {pre_score} \n변경할 점수를 입력하세요. >> ")
                    s.eng = new_score
                    print(f"{new_score}점으로 변경되었습니다.")
                elif choice == 3 :
                    pre_score = s.math
                    new_score = input(f"현재 {title[choice + 1]} 점수 : {pre_score} \n변경할 점수를 입력하세요. >> ")
                    s.math = new_score
                    print(f"{new_score}점으로 변경되었습니다.")
                elif choice == 0 :
                    continue
        if temp == 0 :
            print(f"{name}학생을 찾지 못했습니다. 다시 입력하세요.")
            print()
        
    elif choice == 0 :
        print("프로그램 종료")
        break


