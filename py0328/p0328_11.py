# arr = [1,2,3,4,5,6,7,8,9,10]

# # 리스트 내 for
# arr2 = [i+1 for i in range(100)]
# print(arr2)

# a_list = [1,2,3]
# aa_list = [str(i)+"m"for i in a_list] # 같은 타입끼리 연산
# print(aa_list)

# #arr2 리스트 + cm
# arr2cm = [str(i) +"cm" for i in arr2]
# print(arr2cm)

# arr3 = []
# for i in arr2 :
#     arr3.append(str(i) + "cm")

# print(arr3)

arr = [i for i in range(100)]
print(arr)

# 리스트 내포 100개 리스트에 +100을 하여 출력

arr2 = [ i + 100 for i in arr ]
print(arr2)

a = []
for i in range(100) :
    a.append(i)
    print(a)