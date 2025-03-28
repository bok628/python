# # 두 숫자를 입력받아, 합과 곱 출력
# a = input("숫자를 입력하세요. : ")
# b = input("숫자를 입력하세요. : ")

# a = float(a)
# b = float(b)

# print(a, b)
# print(a+b, a*b)

# #교체
# c = a
# a = b
# b = c
# print(a,b)

# a, b = b, a
# print(a, b)

# a = 100 # int 타입이므로 출력시 + 사용 불가
# st = "안녕"
# print("변수값 :",st) 
# print("변수값 :" + st) # 같은 타입일 경우 , 대신 + 가능

a = 10
b = 5
print(a,"+", b, "=", a+b)

c = 100
d = 7
print(c, "*", d, "=", c*d)
print("%d * %d = %d" % (c,d,c*d))
print(c, "/", d, "=", c/d)
print("%d / %d = %07.2f" % (c, d, c/d))
