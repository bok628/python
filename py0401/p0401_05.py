students = [
    [1, '홍길동', 100,100,100,300,100.0,1],
    [2, '유관순', 100,100,99,299,99.67,2],
    [3, '이순신', 100,100,99,299,99.67,2]
]
# students  = list()
count = 4   # 학생번호 생성
title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']

while True :
    # 화면 출력
    print("-" * 30)
    print(" "*5,end = "")
    print("[ 학생 성적 프로그램 ]")
    print("-" * 30)
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    print("4. 학생 성적 삭제")
    print("5. 학생 성적 정렬")
    print("6. 학생 성적 검색")
    print("7. 등수 처리")
    print("0. 프로그램 종료")
    print("-" * 30)
    choice = int(input("원하는 번호를 입력하세요 : "))
    
    if choice == 1 :
        no = count
        print("[ 학생 성적 입력 ]")
        name = input(f"{no}번 학생의 이름을 입력하세요 : ")
        kor = int(input("국어 점수를 입력하세요 : "))
        eng = int(input("영어 점수를 입력하세요 : "))
        math = int(input("수학 점수를 입력하세요 : "))
        total = kor + eng + math
        avg = total / 3
        rank = 0
        
        student = [no,name,kor,eng,math,total,avg,rank]
        students.append(student)
        print(f"{name}학생의 성적이 입력되었습니다.")
        count += 1
        print()
        
    elif choice == 2 :
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*60) 
        for student in students :
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(*student))
    
    elif choice == 3 :
        temp = 0
        print("[ 학생 성적 수정 ]")
        name = input("학생 이름을 입력해주세요 : ")
        for student in students :
            if name in student :
                temp = 1
                print(f"{name}학생을 찾았습니다.")
                sub = int(input("점수를 수정할 과목을 선택하세요 (1. 국어 2. 영어 3. 수학 0. 취소) :"))
                if sub == 1 :
                    print(f"현재 국어 점수 : {student[2]}")
                    student[2] = int(input("국어 점수를 입력해주세요 : "))
                    student[5] = student[2] + student[3] + student[4]
                    student[6] = student[5] / 3
                    print(f"{name}학생의 국어성적이 수정되었습니다.")
                elif sub == 2 :
                    print(f"현재 영어 점수 : {student[3]}")
                    student[3] = int(input("영어 점수를 입력해주세요 : "))
                    student[5] = student[2] + student[3] + student[4]
                    student[6] = student[5] / 3
                    print(f"{name}학생의 영어성적이 수정되었습니다.")
                elif sub == 3 :
                    print(f"현재 수학 점수 : {student[4]}")
                    student[4] = int(input("수학 점수를 입력해주세요 : "))
                    student[5] = student[2] + student[3] + student[4]
                    student[6] = student[5] / 3
                    print(f"{name}학생의 수학성적이 수정되었습니다.")
                else :
                    print(f"{name}학생의 성적 수정을 취소했습니다.")
                break
        if temp == 0 :
            print(f"{name}학생을 찾지 못했습니다. 다시 입력하세요")
        
         
    elif choice == 4 :
        print("[ 학생 성적 삭제 ]")
        name = input("삭제하려는 학생의 이름을 입력하세요 : ")
        temp = 0
        for i,student in enumerate(students) :
            if name in student :
                temp = 1
                print(f"{name}학생을 찾았습니다.")
                choice = input(f"{name}학생의 성적을 삭제하겠습니까? (0 : 취소, 1 : 삭제)")
                if choice == "1" :
                    print(f"{name}의 성적을 삭제했습니다.")
                    del students[i]
                else :
                    print(f"{name}학생의 성적 삭제를 취소했습니다. 다시 실행하세요")
                break
        if temp == 0 :
            print(f"{name}학생을 찾지 못했습니다. 다시 입력하세요.")
    elif choice == 0 :
        print("프로그램 종료")
        break