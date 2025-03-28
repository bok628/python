# # 숫자 2개를 입력 받아 사칙연산 결과값을 출력
# a=int(input("숫자를 입력하세요 : "))
# b=int(input("숫자를 입력하세요 : "))

# str1 = "{} + {} = {}".format(a,b,a+b)
# str2 = "{} - {} = {}".format(a,b,a-b)
# str3 = "{} * {} = {}".format(a,b,a*b)
# str4 = "{} / {} = {}".format(a,b,a/b)

# print(str1)
# print(str2)
# print(str3)
# print(str4)

#국영수 점수를 입력 받아 평균을 출력하시오
kor = int(input("국어 점수를 입력하세요 : "))
eng = int(input("영어 점수를 입력하세요 : "))
math = int(input("수학 점수를 입력하세요 : "))
avg = (kor + eng + math)/3
print("평균 : %.2f"%avg)

sum = "{} + {} + {} = {}".format(kor,eng,math, kor + eng + math)
avg2 = "{} / 3 = {:.2f}".format(kor + eng + math,(kor + eng + math)/3)
print(sum)
print(avg2)
total_score = "합계 : {}".format(kor + eng + math)
total_avg = "평균 : {:.2f}".format(avg)
print(total_score)
print(total_avg)

