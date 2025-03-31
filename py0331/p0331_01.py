# # 구구단
# for i in range(2,10) :
#     print("[{}단]".format(i))
#     for j in range(1,10) :
#         print("{} X {} = {}".format(i,j,i*j))
#     print()
    
# a_list = [1,2,3,4,5]
# sum = 0
# for i in a_list :
#     sum = sum + i
# print(sum)

a = 10
a_list = [1,2,3,4,5]
print("a : ",a)

a_list[0] = 100
print("a_list : ",a_list)  #[100,2,3,4,5]

b = a
b = 1000
print("a : ",a)
print("b : ",b)

# 얕은 복사 : 같은 리스트의 주소를 복사(리스트 동일)
b_list = a_list
b_list[1] = 200

# 깊은 복사
a_list = [1,2,3,4,5]
b_list = [*a_list]
b_list[1] = 200
print(a_list) # [100,2,3,4,5]
print(b_list) # [1,200,3,4,5]