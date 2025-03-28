# # bool - True False / int, float / str

# # print()
# print("Hi")
# print(10)

# # variable
# a = 10
# b = 20

# print("hello", a)
# print("%d "% 10)
# print("{}".format(b))
# print("{}".format("Hi"))
# print(f"{a} * {b} = {a*b}")

# # input (str)
# num1 = int(input("Write number :"))
# num2 = float(input("Write number :"))
# print("number : {},{} / sum : {:.1f}".format(num1,num2,num1+num2))

#Grade
print("학생 성적 프로그램")
print("-"*50)
name = str(input("이름을 입력하세요 : "))
kor = float(input("국어 성적을 입력하세요 : "))
eng = float(input("영어 성적을 입력하세요 : "))
math = float(input("수학 성적을 입력하세요 : "))

total = kor + eng + math
# print("이름\t {}, 국어\t {}, 영어\t {}, 수학\t {}".format(name,kor,eng,math))
# print("합계 : ",total)
# print("평균 : ",total/3)
print("이름\t국어\t영어\t수학\t합계\t평균")
print("-"*50)
print("{}\t{}\t{}\t{}\t{}\t{}\t".format(name,kor,eng,math,total,total/3))

