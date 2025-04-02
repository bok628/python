# 함수 선언
# def cal(x,y) :
#     result = x + y
#     print("합계 : ",result)
#     result2 = x - y
#     print("빼기 : ",result2)
#     result3 = x * y
#     print("곱하기 : ",result3)
#     result4 = x / y
#     print("나누기 : ",result4)

# # 함수 호출 - cal(매개변수)
# a,b = 10,20
# cal(a,b)

# c,d = 100,200
# cal(c,d)

# e,f = 50,100
# cal(e,f)



# def add() :
#     print("안녕하세요.")
#     print("안녕하세요.")
#     print("안녕하세요.")
    
# print("누군가 오고 있어요.")
# print("인사")
# add() # 함수호출


# def add(x,y) :
#     print("x = ",x)
#     print("y = ",y)
#     print("x + y = ",x + y)
    
# # 특정값 
# a = 10
# b = 20
# c = 30
# d = 40

# add(a,b)
# add(a,c)
# add(a,d)
# add(c,d)


# 두 수를 입력받아 사칙연산 출력

def cal(x,y) :
    print("x + y = ",x + y)
    print("x - y = ",x - y)
    print("x X y = ",x * y)
    print(f"x / y = {(x / y):.2f}")
    return x + y

num1 = int(input("숫자를 입력하세요 : "))
num2 = int(input("숫자를 입력하세요 : "))    
result1 = cal(num1,num2)

num3 = int(input("숫자를 입력하세요 : "))
num4 = int(input("숫자를 입력하세요 : "))
result2 = cal(num3,num4)

num5 = int(input("숫자를 입력하세요 : "))
num6 = int(input("숫자를 입력하세요 : "))
result3 = cal(num5,num6)

print("총합계 : ",result1 + result2 + result3)
# 결과 중 합계를 모두 더해서 총 합계 구하기

