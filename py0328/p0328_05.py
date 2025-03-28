# # 두 수를 입력받아, 두 수 사이의 합계를 구하시오
# num1 = int(input("숫자를 입력하세요 : "))
# num2 = int(input("숫자를 입력하세요 : "))
# sum = 0
# t = 0

# # num1 > num2일 때 for 반복문 작동 X 
# if num1 > num2 :
#     t = num1
#     num1 = num2
#     num2 = t
    
# for i in range(num1,num2+1) :
#     sum = sum + i
# print("{}에서 {}까지의 합 : {}".format(num1,num2,sum))

# # 구구단 출력 프로그램(2~9단)
# print("-"*50)
# print("구구단")
# for i in range(2,10) :
#     print("[{}단]".format(i)) 
#     for j in range(1,10) :
#         print("{} X {} = {}".format(i,j,i*j))
#     print()  # 한 줄 띄우기
    
# #홀수단만 출력
# print("-"*50)
# for i in range(2,10) :
#     if i % 2 == 1 :
#         print("[{}단]".format(i)) 
#         for j in range(1,10) :
#             print("{} X {} = {}".format(i,j,i*j))
#         print()  # 한 줄 띄우기
        
# 시작단과 끝나는 단을 입력받아, 출력
num1 = int(input("숫자 입력 : "))
num2 = int(input("숫자 입력 : "))
t = 0

if num1 > num2 :
    t = num1
    num1 = num2
    num2 = t
    
print("-"*50)
for i in range(num1, num2 + 1) :
    print("[{}단]".format(i)) 
    for j in range(1,10) :
        print("{} X {} = {}".format(i,j,i*j),end = "  ")
    print()