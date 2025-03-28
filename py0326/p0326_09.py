# 이름, 국영수 성적을 입력받아 합계와, 평균 출력시키기
# 이름 : 홍길동 
# 합계 : 300
# 평균 : 100.0 소수점은 1자리까지 출력

# name = input("이름 : ")
# Korean = input("국어 점수를 입력하시오. : ")
# Eng = input("영어 점수를 입력하시오. : ")
# math = input("수학 점수를 입력하시오. : ")
# science = int(input("과학 점수를 입력하시오. : "))

# Korean = int(Korean)
# Eng = int(Eng)
# math = int(math)
# sum = Korean + Eng + math + science #
# average = sum / 4 #

# print("이름 :", name)
# print("합계 :", sum)
# print("평균 :", "%.1f" % average)
# print("평균 : %.1f" % average) #

#\n : 한 줄 띄우기 (엔터) \t : 탭의 크기만큼 띄어쓰기 (탭키) 
# print("안녕하세요.\n반갑습니다.\t저는 홍길동이라고 합니다.")

#format() 문자형태 지정 함수
a = 7
b = 3
print("%d + %d = %d" % (a,b,a+b))
str = "{} + {} = {}".format(a,b,a+b) #str 형태로 저장
print(str)

print("%d / %d = %.2f" % (a,b,a/b))
str_print = "{} / {} = {:.2f}".format(a,b,a/b)
print(str_print)

#f""함수 = format()
str_print2 = f"{a} / {b} = {(a/b):.2f}"
print(str_print2)


