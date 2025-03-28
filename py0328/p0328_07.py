# for j in range(10) :
#     print(j)
# print("-"*50)
# # while 반복문 - 'while + 조건' 에서 조건이 맞으면 반복(무한반복 가능) <-> for 반복문 - 횟수만큼 반복
# i = 0
# while i < 10 :
#     print(i)
#     i += 1

# # # ex) 무한 반복되는 사례
# # i = 0
# # while True :
# #     print(i)
# #     i += 1

# list = [1,5,10,9,8,20]
# a = 5
# if a in list :
#     print("{}가 존재합니다.".format(a))
# else :
#     print("{}가존재하지 않습니다.".format(a))
    
# 입력숫자를 5번 반복해서 리스트에 추가하는 프로그램 구현
i = 0
list_aa = []
while i <= 9 :
    aa = int(input("{}번째 숫자를 입력하세요 : ".format(i+1)))
    if aa not in list_aa :
        list_aa.append(aa)
        i += 1

print(list_aa)

# num_list = []
# for i in range(10) :
#     num = int(input("숫자를 입력하세요 : "))
#     if num not in num_list : 
#         num_list.append(num)
