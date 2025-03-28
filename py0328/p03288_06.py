# 숫자 맞추기 프로그램
import random

# 1-45번 중 숫자 1개 가져옴.
lotto = random.randint(1,45)
list = []
print("숫자 맞추기")
print("-"*50)
#------------10번 반복
for i in range(10) :
    print("{}번째".format(i+1))
    inp = int(input("1-45번 사이의 숫자를 입력하세요 : "))
    list.append(inp)
    if lotto == inp :
        print("당첨")
        break
    else :
        print("미당첨")
        if inp > lotto :
            print("틀렸습니다. {}보다 작은 수를 입력하세요.".format(inp))
        else :
            print("틀렸습니다. {}보다 큰 수를 입력하세요.".format(inp))
            
print("랜덤 번호 : {}".format(lotto))
print("입력 번호 : {}".format(list))
