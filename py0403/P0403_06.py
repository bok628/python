# 학생 성적 프로그램
# 데이터 생성(딕셔너리) -> 출력화면 
# -> 1.학생성적입력(학생번호 자동생성 - 성적입력 무한반복으로 실행 - 이전화면 이동구현 - 점수입력에 대한 체크(0~100의 숫자인지)
# -> 2.학생성적출력(상단타이틀 출력 - 학생별 성적 출력)
# -> 3.학생성적수정(수정하고자 하는 학생검색 - 수정하려는 과목 선택 - 검색이 되지 않았을 경우 구현)
# -> 4.학생성적정렬(이름으로 순차정렬 - 합계로 순차정렬) 
# -> 5.학생성적검색(찾고자 하는 학생 검색 후 학생이 존재하면 화면 출력) 
# -> 6.등수처리(합계를 기준으로 등수처리 진행)
# -> 0.종료

students = [
    {"no":1, "name":"홍길동","kor":100, "eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2, "name":"유관순","kor":100, "eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
    {"no":3, "name":"이순신","kor":100, "eng":100,"math":99,"total":299,"avg":99.67,"rank":2}
]

title = {"번호","이름","국어","영어","수학","합계","평균","순위"}


while True :
    print("<학생 성적 프로그램>")
    print("-"*50)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적정렬")
    print("5. 학생성적검색")
    print("6. 등수처리")
    print("0. 프로그램 종료")
    
    count = 4
    
    
    choice = int(input("번호를 입력하세요. >> "))
    
    if choice == 1 :
        print("[ 학생성적입력 ]")
        print("-"*50)
        no = count
        name = input(f"{count}번 학생의 이름을 입력하세요. >> ")
        kor = int(input("국어성적을 입력하세요. >>"))
        eng = int(input("영어성적을 입력하세요. >>"))
        math = int(input("수학성적을 입력하세요. >>"))
        total = kor + eng + math
        avg = total / 3
        rank = 0
        students.append({'no':no,'name':name,'kor':kor,'eng':eng,'math':math,'total':total,'avg':avg,'rank':rank})
        print(f"{name}학생의 성적이 입력되었습니다.")
        
    if choice == 2 :
        print("[ 학생성적출력 ]")
        print("-" * 50)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-" * 50)
        for s in students :
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}".format(students))
        print()
        
    if choice == 3 :
        print("[ 학생성적수정 ]")
        name = input("수정할 학생의 이름을 입력하세요.(0.이전화면 이동) >> ")
        temp = 0
        if name == "0" :
            break
        for s in students :
            if name == s['name'] :
                temp = 1
                print(f"{name}학생을 찾았습니다.")
                print()
                choice = int(input("1. 국어\n2. 영어\n3. 수학\n수정할 과목의 번호를 입력하세요. >>"))
                sub_list = ["","kor","eng","math"]
                if choice == 1 or choice == 2 or choice == 3 :
                    pre_score = s[sub_list[choice]]
                    print(f"현재 {title[choice + 1]} 점수 : {pre_score}")
                    s[sub_list[choice]] = int(input(f"수정할 {title[choice + 1]} 점수를 입력하세요 : "))
                    s['total'] = s['kor'] + s['eng'] + s['math']
                    s["avg"] = s['total'] / 3
                    print(f"{pre_score}점이 {s[sub_list[choice]]}점으로 변경되었습니다.")
                    
           
        if temp == 0 :
            print(f"{name}학생을 찾지 못했습니다.")
            continue
            
    if choice == 4 :
        print("[ 학생성적정렬 ]")
        pass
    if choice == 5 :
        print("[ 학생성적검색 ]")
        pass
    if choice == 6 :
        print("[ 등수처리 ]")
        for s in students :
            num = 1
            for ss in students :
                if s['total'] < ss['total'] :
                        num += 1
            s['rank'] = num
    if choice == 0 :
        break