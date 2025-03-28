# # 반복을 해서, ran_list에 10개를 입력시키는 프로그램 구현(중복숫자 X)
# # 로또 프로그램
# import random
# ran_list = []
# i = 0

# while i < 6 :
#     ran_num = random.randint(1,45)
#     if ran_num not in ran_list :
#         print("{}번째 숫자 : {}".format(i+1,ran_num))
#         ran_list.append(ran_num)
#         i += 1

# print(ran_list)

# 랜덤 숫자 6개를 리스트에 저장 & 입력받은 숫자 6개를 다른 리스트에 저장
# 랜덤과 입력 숫자를 비교하여 당첨 개수와 당첨 번호 출력하기
import random
ran_list = []
i = 0

while i < 6 :
    ran_num = random.randint(1,45)
    if ran_num not in ran_list :
        ran_list.append(ran_num)
        i += 1
    
j = 0
inp_list = []

print("랜덤 숫자 : {}".format(ran_list))


while j < 6 :
    inp_num = int(input("{}번째 숫자를 입력하세요 : ".format(j+1)))
    if inp_num not in inp_list :
        inp_list.append(inp_num)
        j += 1

lotto_count = 0
lotto_list = []

# # 당첨 비교 (ran_list & inp_list)
# # 방법 1
# for k in range(6) :
#     for g in range(6):
#         if ran_list[k] == inp_list[g] :
#             lotto_count += 1
#             lotto_list.append(inp_list[g])
#             break
        
# 방법 2
for z in range(6) :
    if ran_list[z] in inp_list :
        lotto_count += 1 
        lotto_list.append(ran_list[z])
        
            
print("랜덤 숫자 : {}".format(ran_list))
print("입력 숫자 : {}".format(inp_list))
print("당첨 번호 : {}".format(lotto_list))
print("당첨 개수 : {}".format(lotto_count))

