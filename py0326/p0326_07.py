a = 100
b = 50
# a와 b의 값을 교체하기
#잘못된 예시
a = b
b = a
print(a) #50
print(b) #50
#새로운 변수를 생성하여 값을 교체 ex)주스&우유
a = 100
b = 50
c = a #
a = b #
b = c #
#파이썬만 가능한 교체 방법
a,b = b,a

# 입력 :input 출력 print
print(input("숫자 입력 :"))

#변수()의 형태 : 함수(기능구현을 말함) 
#ex) print() 

# input
c = input("숫자입력 : ")
d = input("숫자를 입력하세요. : ")
print(c,d)
# input의 type = str (문자열)
print(type(c)) #str
print(type(d)) #str
print(c+d) #105 (c = 10, d = 5일 때)

#input타입 변경 (정수 : int(), 실수 : float(), 문자열 : str()) ***********
c= int(c) #str => int
d=int(d)#str => int
print(c+d)

c = float(c)
d = float(d)
print(c,d)


