# bool : True/False
if True :
    print("T")
if False :
    print("F")

print(10>3)

# print("1" + 1) X => 타입다름
print(int("1") + 1)
print("안녕",1)
print("{:05.2f}".format(11/3))
print(int(2.13)) # 실수형 -> 정수형 변환 출력결과 : 2
#print(int("10.1")) # ERROR

# = : 할당
a = 1
b = 1.1
c = "fxx"
print(a + b)

# list
list_a = [1,2,3,4]
list_a.append(5)
print(list_a[0] + list_a[4])

# score = input("데이터 입력 :")
# print("입력 데이터 : ",score)

#두수를 입력받아 함계평균 출력
a = int(input("숫자를 입력하세요 :"))
b = int(input("숫자를 입력하세요 :"))

sum = a + b
avg = sum/2
print("합계 {}, 평균 {}".format(sum,avg))

score = int(input("점수를 입력하세요 :"))
if score >= 60 :
    print("합격")
elif score >= 50 : 
    print("재시험")
else : 
    print("불합격")
    
    
sc = int(input("점수 입력 : "))
if sc >=90 : 
    print("A") 
elif sc >= 80 :
    print("B")
elif sc >= 70 :
    print("C") 
elif sc >= 60 :
    print("D")
else :
    print("F")   
