
# students = [
#     [1,'홍길동',100,100,100,300,100.0,0],
#     [2,'유관순',100,100,100,300,100.0,0],
#     [3,'이순신',100,100,100,300,100.0,0],
# ]

# #tudent = [1,'홍길동',100,100,100,300,100.0,0]

# print("                   [    학생 성적 프로그램    ]")
# print("-"*65)
# print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
# print("-"*65)
# for stu in students :
#     for s in stu :
#         print(s, end = "\t")
#     print()

# 학생 성적 프로그램 만들기
students = list()

while True :
    no = count
    name = input("이름을 입력하세요 : ")
    kor = int(input("국어 점수를 입력하세요 : "))
    eng = int(input("영어 점수를 입력하세요 : "))
    math = int(input("수학 점수를 입력하세요 : "))
    total = kor + eng + math
    avg = total / 3
    rank = 0
    
    count += 1

    student = [no,name,kor,eng,math,total,avg,rank]
    students.append(student)

    print("                   [    학생 성적 프로그램    ]")
    print("-"*65)
    print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
    print("-"*65)
    for stu in students :
        for i,s in enumerate(stu) :
            if i != 6 :
                print(s, end= "\t")
            else :
                print(f"{s:.2f}",end = "\t")
        print()