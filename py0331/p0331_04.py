# 1-25 랜덤리스트
import random
sample_list = [ i+1 for i in range(25) ]
random.shuffle(sample_list)

a_list = [[0] * 5 for j in range(5)]

for n in range(5) :
    for l in range(5) :
        a_list[n][l] = sample_list[n*5 + l]

# 5*5 출력
while True :
    print(" [ 좌표 맞추기 프로그램 ]")
    print("0ㅣ",end = "")
    for i in range(5) :
        print(i,end = "\t")
    print()
    print("-"*40)
    for k in range(5) :
        print(f"{k}ㅣ",end = "")
        for m in range(5) :
            print(a_list[k][m], end = "\t")
        print()
        
    print()
    num1 = int(input("x좌표를 입력하세요 : "))
    num2 = int(input("y좌표를 입력하세요 : "))
        
    a_list[num1][num2] = "X"
        
