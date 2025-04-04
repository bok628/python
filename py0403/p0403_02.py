#import stu_func         # 외부 파일 불러오기
#import stu_func as stu # 별칭 사용 -> stu.stu_print()로 함수 호출
from stu_func import * # only 함수이름으로 호출



# 초기화 선언
students = [
    {"no":1, "name":"홍길동","kor":100, "eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2, "name":"유관순","kor":100, "eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
    {"no":3, "name":"이순신","kor":100, "eng":100,"math":99,"total":299,"avg":99.67,"rank":2}
]

count = 4
title = ['번호','이름','국어','영어','수학','합계','평균','등수']
choice = 0


def stu_fix() :
        print("[ 학생성적 수정 ]")
        name = input("수정하려고 하는 학생 이름을 입력하세요. >>")
        temp = 0
        for s in students :
            if s['name'] == name :
                temp = 1
                print(f"{name}학생을 찾았습니다. 과목을 수정합니다.")
                print("[ 수정 과목 선택 ]")
                print("1. 국어\n2. 영어\n3. 수학")
                print("-"*10)
                choice = int(input("원하는 과목의 번호를 입력하세요. >>"))
                
                # s['kor'] 대신해서 사용
                sub_list = ['','kor','eng','math']
                if choice == 1 :
                    pre_score = s[sub_list[choice]]
                    print(f"현재 {title[choice + 1]} 점수 : {pre_score}")
                    s[sub_list[choice]] = int(input(f"수정할 {title[choice + 1]}점수를 입력하세요. >>"))
                    s['total'] = s['kor'] + s['eng'] + s['math']
                    s['avg'] = s['total'] / 3
                    print("변경완료")
                    print(f"변경 전 점수 : {pre_score}점, 변경 후 점수 : {s[sub_list[choice]]}점")
                print()
                if choice == 2 :
                    pre_score = s[sub_list[choice]]
                    print(f"현재 {title[choice + 1]} 점수 : {pre_score}")
                    s[sub_list[choice]] = int(input(f"수정할 {title[choice + 1]}점수를 입력하세요. >>"))
                    s['total'] = s['kor'] + s['eng'] + s['math']
                    s['avg'] = s['total'] / 3
                    print("변경완료")
                    print(f"변경 전 점수 : {pre_score}점, 변경 후 점수 : {s[sub_list[choice]]}점")
                print()
                if choice == 3 :
                    pre_score = s[sub_list[choice]]
                    print(f"현재 {title[choice + 1]} 점수 : {pre_score}")
                    s[sub_list[choice]] = int(input(f"수정할 {title[choice + 1]}점수를 입력하세요. >>"))
                    s['total'] = s['kor'] + s['eng'] + s['math']
                    s['avg'] = s['total'] / 3
                    print("변경완료")
                    print(f"변경 전 점수 : {pre_score}점, 변경 후 점수 : {s[sub_list[choice]]}점")
                print()
        if temp == 0 :
            print(f"{name}학생을 찾지 못하였습니다. 다시 입력하세요")
            print()
    
while True :
    # 화면출력함수 사용
    choice = stu_print()
    
    if choice == 1 :
        # 1. 학생성적입력 함수 사용
        count = stu_input(count,students)
        
    elif choice == 2 :
        # 2. 학생성적출력 함수 사용
        stu_output(title,students)
        
    elif choice == 3 :
        # 3. 학생성적수정 함수 사용
        stu_fix()        
                
    elif choice == 4 :
        # 4. 등수처리 함수 사용
        stu_rank(students)
    elif choice == 0 :
        print("[프로그램 종료]")
        break
    else :
        print("번호를 다시 입력하세요")