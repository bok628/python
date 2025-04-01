# 1차원 리스트
import random
s_list = [i for i in range(1,26)]
#random.random() - 0.0000<= <1.00000, random.randint(), random.sample() - 특정 갯수 추출, random.shuffle()
random.shuffle(s_list)                  

# 2차원 리스트
my_list = list()
my_list = [[0]*5 for _ in range(5)]

# 1차원 리스트 값 -> 2차원 리스트 입력
for i in range(5) :
    for j in range(5) :
        my_list[i][j] = s_list[5*i + j] #5x + y
while True :

    print("               [좌표 맞추기 프로그램]")
    print("-" *45)
    print("*  ㅣ", end = "\t")
    for i in range(5) :
        print(f"{i}  ㅣ", end = "\t")
    print()
    print("-" * 45)


        
    # 화면출력
    for i in range(5) :                          
        print(f"{i}  ㅣ", end = "\t")
        for j in range(5) :
            print(my_list[i][j], end = "\t")
        print()

    print("-" * 45)
    
    # # 좌표입력
    # x = int(input("X좌표를 입력하세요 : "))
    # if x > 5 or x < 0 :
    #    print("좌표를 다시 입력하세요")
    #    continue
   
    # y = int(input("Y좌표를 입력하세요 : "))
    # if y > 5 or y < 0 :
    #    print("좌표를 다시 입력하세요")
    #    continue
   
    # my_list[y][x] = "X"
    # print()
    
    # 번호입력
    stop = 0
    num = int(input("숫자를 입력하세요 (1-25) : "))
    for i in range(5) :  
        for j in range(5) :
            if my_list[i][j] == num :
                my_list[i][j] = "X"
                stop = 1
                break
        if stop == 1 :
             break

    print()

