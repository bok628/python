#import stu_func         # 외부 파일 불러오기
#import stu_func as stu # 별칭 사용 -> stu.stu_print()로 함수 호출
from StuFunc import * # only 함수이름으로 호출


students = []
#### 파일 불러오기
# stu.txt파일에서 데이터를 읽어와 students = [] 데이터 입력시킴
with open("py0404/stu.txt","r",encoding = "utf-8") as f :    # with 사용시 close X
    while True :              # txt가 여러줄일때
        line = f.readline()   # 1줄 읽어오기
        if not line :         # data X : 종료
            break
        s = line.strip().split(",") # 문자열 1줄을 공백제거 후 쉼표로 구분
        students.append({"no":int(s[0]), "name" : s[1],
                        "kor" : int(s[2]), "eng" : int(s[3]), "math" : int(s[4]),
                        "total" : int(s[5]), "avg" : float(s[6]), "rank" : int(s[7])})
        
        
    

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
    elif choice == 5 :
        print("[ 학생성적정렬 ]")
        print("1. 이름 순차정렬")
        print("2. 이름 역순정렬")
        print("3. 합계 순차정렬")
        print("4. 합계 역순정렬")
        print("5. 번호 순차정렬")
        print("6. 번호 역순정렬")
        print("0. 이전화면이동")
        print("-"*30)
        choice = int(input("원하는 번호를 입력하세요. >> "))
        students2 = [*students] # 깊은복사
        if choice == 1 :
            students2.sort(key = lambda x : x['name'])
        elif choice == 2 :
            students2.sort(key = lambda x : x['name'],reverse = True)
        elif choice == 3 :
            students2.sort(key = lambda x : x['total'])
        elif choice == 4 :
            students2.sort(key = lambda x : x['total'],reverse = True)
        elif choice == 5 :
            students2.sort(key = lambda x : x['no'])
        elif choice == 6 :
            students2.sort(key = lambda x : x['no'],reverse = True)
        elif choice == 0 :
            continue
        stu_output(title,students2)
    elif choice == 6 :
        print("[ 학생성적삭제 ]")
        name = input("삭제하고자 하는 학생 이름을 입력하세요. >> ")
        temp = 0
        for i,s in enumerate(students) :
            if name == s['name'] :
                temp = 1
                print(f"{s['no']}번 {s['name']}학생을 찾았습니다.")
                ans = input(f"{s['name']}학생의 성적을 삭제할까요? (* 삭제하면 복구불가)")
                if ans == "y" :
                    del students[i]
                print(f"{name}학생을 삭제했습니다.")
                print()
                break
        if temp == 0 :
            print(f"{name}학생을 찾지 못했습니다. 다시 입력하세요")
            print()
                
    elif choice == 7 :
        print("[ 학생성적저장 ]")
        with open("py0404/stu.txt","w",encoding = "utf-8") as f :
            for s in students :
                # 1,홍길동,100,100,100,300,100.0,1
                line = f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}\n"
                f.write(line)
        print("파일이 저장되었습니다")
        print()
        
    elif choice == 0 :
        print("[프로그램 종료]")
        break
    else :
        print("번호를 다시 입력하세요")