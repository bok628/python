# a, b = 100, 200
# c = 300; d = 400
# e = 500
# f = 600

# #관계 연산자 - True or False로만 출력
# print(a == b)
# print(a != b)
# print(a>b,a<b,a>=b,a<=b)

# 조건문
a = int(input("숫자 입력 : "))
if a < 100 : 
    print("입력한 값은 100보다 작은 수이다.")

else :
    print("입력한 값은 100보다 큰 수이다.")

# 양수(including 0)/음수 확인
num = int(input("숫자를 입력하세요 : "))
if num >= 0 :
    print("양수")
else : 
    print("음수")
    
# 짝수/홀수 확인 & 3의 배수
num1 = int(input("숫자를 입력하세요 : "))
if num % 2 == 0 & num % 3 == 0 :
    print("짝수이면서 3의 배수이다")    
else :
    print("홀수이다.")

