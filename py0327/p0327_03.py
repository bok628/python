# Grade
print("-"*50)
print("                학생 성적 프로그램")
print("-"*50)
name = str(input("이름을 입력하세요 : "))
kor = int(input("국어 성적을 입력하세요 : "))
eng = int(input("영어 성적을 입력하세요 : "))
math = int(input("수학 성적을 입력하세요 : "))
total = kor + eng + math
print("-"*50)
print("이름\t국어\t영어\t수학\t합계\t평균")
print("-"*50)
print("{}\t{}\t{}\t{}\t{}\t{:.2f}\t".format(name,kor,eng,math,total,total/3)) 

