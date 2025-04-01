import random

list1 = [ i + 1 for i in range(25)]
random.shuffle(list1)

list2 = [[0] * 5 for i in range(5)]
for i in range(5) :
    for j in range(5) :
        list2[i][j] = list1[5 * i + j]
print(list2)

while True :
    print("         [좌표 맞추기 프로그램]")
    print("-" * 50)
    print("*  ㅣ",end = "\t")
    for i in range(5) :
        print(f"{i}  ㅣ",end = "\t")
    print()
    print("-" * 45)
    
    for i in range(5) :
        for j in range(5) :
            print(list2[i][j], end = "\t")
        print()
    
    print("-" * 45)
    num = int(input("숫자를 입력하세요 (1-25) : "))
    
    for i in range(5) :
        for j in range(5) :
            if list2[i][j] == num :
                list2[i][j] = "X"
