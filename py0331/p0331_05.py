# 5 * 5 이차원 리스트 -> 랜덤으로 1-25까지의 숫자 넣기
# 1차원 리스트 생성
# 1차원 리스트 랜덤으로 섞기
# 2차원 리스트 생성
# 2차원 리스트에 1차원 랜덤번호 넣기

#
import random                                               
first_list = [ i+1 for i in range(25) ]                
random.shuffle(first_list)                                 

# 2차원 (for 2번)
a_list = [[0] * 5 for i in range(5)]                        
for i in range(5) :                                         
    for j in range(5) :                                        
        a_list[i][j] = first_list[5*i + j]                     
print(a_list)                                                 

# 2차원 형태로 출력
while True :
    print("           [ 좌표 맞추기 프로그램 ]")
    print("-"*45)
    print("*  ㅣ",end = "\t")
    for i in range(5) :
        print(i, end = "\t")
    print()
    print("-"*45)

    for i in range(5) :
        print( f"{i}  ㅣ",end = "\t")
        for j in range(5) :
            print(a_list[i][j],end ="\t")
        print()

    #입력
    print("-"*45)
    # num1 = int(input("x좌표를 입력하세요 : "))
    # if num1<0  or num1>4 :
    #     print("숫자를 잘못 입력하셨습니다. 다시 입력하세요. ")
    #     continue
    # num2 = int(input("y좌표를 입력하세요 : "))
    # if num2<0 or num2>4 :
    #     print("숫자를 다시 입력하세요.")
    #     continue
    
    num = 15
    
    a_list[num2][num1] = "X"
    print()
    
    