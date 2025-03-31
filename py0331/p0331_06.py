# # x좌표 : 1, y좌표 : 3 을 한번에 1,3로 입력하기
# num1 = int(input("X좌표 : "))
# num2 = int(input("Y좌표 : "))

# print(f"[X,Y좌표 : {num1},{num2}]")

num = input("X,Y 좌표 (0,0) : ")
n_list = num.split(",")              #숫자를 ,로 분리
print(f"[X,Y 좌표 {n_list}]")                            