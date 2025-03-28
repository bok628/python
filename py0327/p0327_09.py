# # 0보다 같거나 크고 1미만인 random실수 값 전달해줌.
# import random
# print(random.random())

# print(random.randint(1,10)) 

# # 랜덤숫자를 맞추는 프로그램
# ran_num = random.randint(1,5)
# in_num = int(input("랜덤숫자 맞추기!(1~5) : "))
# if ran_num == in_num :
#     print("정답. 랜덤숫자 : {}".format(ran_num))
# else :
#     print("오답. 랜덤숫자 : {} 입력숫자 : {}".format(ran_num,in_num))

# for 반복문
for n in range(10) :  
    print(n)
for _ in range(10) :
    print("안녕")
for n in range(1,11) :
    print(n)

# 1-100까지의 숫자 10개를 입력 받음
num = []
n = 0 # 입력횟수

import random
ran_num = random.randint(1,100)

for n in range(1,11):
    in_num = int(input("숫자를 입력하세요 :"))
    num.append(in_num) # num list에 데이터 추가
    if ran_num == in_num :
        print("정답! {}".format(ran_num))
        break
    elif ran_num > in_num :
        print("더 큰 수를 입력하셔야 합니다. 입력숫자 {}".format(in_num))
    else :
        print("더 작은 수를 입력하셔야 합니다. 입력숫자 {}".format(in_num))
        
print("랜덤 숫자 : {}.".format(ran_num))
print("도전횟수: {}".format(n))
print("입력된 숫자 : {}".format(num))