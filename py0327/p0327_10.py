# 랜덤 숫자(1~100)를 생성해서 정답을 맞추는 프로그램을 구현
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