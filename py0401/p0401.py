students = [{}]


while True :
    print(" 학생 성적 프로그램 ")
    print("-"*50)
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("0. 프로그램 종료")
    
    title = ["번호","이름","국어","영어","수학","합계","평균","순위"]
    count = 4
    choice = int(input("원하시는 번호를 입력하세요 : "))
        
    if choice == 0 :
        print("프로그램 종료")
        break
    
    while True :
        if choice == 1 :
            print("[ 학생 성적 입력 ]")
            no = count
            name = input(f"{no}번 학생의 이름을 입력하세요(0.이전화면 이동) : ")
            if name == "0" :
                break
            rank = 0
            kor = int(input("국어 점수를 입력하세요 : "))
            eng = int(input("영어 점수를 입력하세요 : "))
            math = int(input("수학 점수를 입력하세요 : "))
            total = kor + eng + math
            avg = total / 3   #float
            
            students.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg,"rank":rank})
            print(f"{no}번 학생 성적이 입력되었습니다.")
            count += 1
            print()
            
        if choice == 2 :
            print("[ 학생 성적 출력 ]")
            print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
            print("-"*60)
            
            #for문으로 딕셔너리 출력
            for s in students :
                print(f"{s["no"]}\t{s["name"]}\t{s["kor"]}\t{s["eng"]}\t{s["math"]}\t{s["total"]}\t{s["avg"]:.2f}\t{s["rank"]}")
                break
