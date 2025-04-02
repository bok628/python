### 파일 - 저장해서 불러오기
### DB에서 불러오기
students = [
    {"no":1, "name":"홍길동","kor":100, "eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2, "name":"유관순","kor":100, "eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
    {"no":3, "name":"이순신","kor":100, "eng":100,"math":99,"total":299,"avg":99.67,"rank":2}
]

count = 4   # 학생번호 생성
title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']

while True :
    print(" "*4,end = "")
    print("[ 학생 성적 프로그램 ]")
    print("-"*30)
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    print("0. 프로그램 종료")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요 : "))
    
    # 번호 선택
    if choice == 1 :
        while True :
            print("[ 학생 성적 입력 ]")
            no = count
            name = input(f"{no}번 학생의 이름을 입력하세요(0. 이전 화면 이동) : ")
            print()
            if name == "0" :
                break
            while True :
                kor = input("국어 점수를 입력하세요 : ")
                if kor.isdigit() :
                    kor = int(kor)
                    if 0 <= kor <= 100 :
                        break
                    else : 
                        print("0~100 사이의 값을 입력해야 합니다.")
                else :
                    print("숫자만 가능합니다.")
                    
            while True :
                eng = input("영어 점수를 입력하세요 : ")
                if eng.isdigit() :
                    eng = int(eng)
                    if 0 <= eng <= 100 :
                        break
                    else : 
                        print("0~100 사이의 값을 입력해야 합니다.")
                else :
                    print("숫자만 가능합니다.")

            while True : 
                math = input("수학 점수를 입력하세요 : ")
                if math.isdigit() :
                    math = int(math)
                    if 0 <= math <= 100 :
                        break
                    else : 
                        print("0~100 사이의 값을 입력해야 합니다.")
                else :
                    print("숫자만 가능합니다.")
            total = kor + eng + math
            avg = total / 3
            rank = 0
            
            students.append({"no":no, "name":name,"kor":kor, "eng":eng,"math":math,"total":total,"avg":avg,"rank":rank})
            print(f"{no}번 {name}학생 성적을 저장했습니다.")    
            print()
            count += 1 # 학생수 1증가
            
    elif choice == 2 :
        print("[ 학생 성적 출력 ]")
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*60)
        for s in students :
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}".format(*students))
        print()
            
    elif choice == 3 :
        print("[ 학생 성적 수정 ]")
        name = input("수정하려고 하는 학생 이름을 입력하세요.(0.이전화면 이동) : ")
        temp = 0  # 찾고자 하는 학생이 없을 경우
        if name == "0" :
            break
        
        for s in students :
            if name in s['name'] :
                temp = 1
                print(f"{name}학생의 성적을 수정합니다.")
                print("[ 수정할 과목 선택 ]")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print("-"*10)
                choice = int(input("원하는 번호를 입력하세요 : "))
                
                # 수정할 과목 확인
                if choice == 1 : #국어
                    pre_kor = s['kor']
                    print(f"현재 국어 점수 : {pre_kor}")
                    s['kor'] = int(input("변경할 국어 점수 : "))
                    s['total'] = s['kor'] + s['eng'] + s['math']
                    s['avg'] = s['total'] / 3
                    print(f"{pre_kor}점을 {s['kor']}점으로 변경되었습니다.")
                elif choice == 2 :
                    pre_eng = s['eng']
                    print(f"현재 영어 점수 : {pre_eng}")
                    s['eng'] = int(input("변경할 영어 점수를 입력하세요 : "))
                    s['total'] = s['kor'] + s['eng'] + s['math']
                    s['avg'] = s['total'] / 3
                    print(f"{pre_eng}점이 {s['eng']}점으로 변경되었습니다.")
                elif choice == 3 :
                    pre_math = s['math']
                    print(f"현재 수학 점수 : {s['math']}점")
                    s['math'] = int(input("변경할 수학 점수를 입력하세요"))
                    s['total'] = s['kor'] + s['eng'] + s['math']
                    s['avg'] = s['total'] / 3
                    print(f"{pre_math}점을 {s['math']}점으로 변경하였습니다.")               
        # 수정할 학생을 찾지 못했을 경우
        if temp == 0 :
            print("수정하고자 하는 학생을 찾지 못했습니다. 다시 입력하세요.")
        
    elif choice == 0 :
        print("[ 프로그램 종료 ]")
    

    