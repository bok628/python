# a = [273,10,5,9,100,1000,50]

# # enumerate : 인덱스 번호 넣기
# for idx, value in enumerate(a) :
#     print(f"{idx + 1} : {value}")
    
# # 리스트에 추가하기 : append(리스트 마지막에 추가), insert(원하는 위치,원하는 값), extend(마지막에 리스트의 형태로 여러 개를 추가)
# a_list = []

# for i in range(1,11) :
#     a_list.append(i)
# print(a_list)

# a_list.insert(1,100) #특정 위치에 값 추가
# print(a_list)

# a_list.extend([200,252,628]) #다른 리스트를 추가
# print(a_list)


# # 리스트에 추가하기 : 내포(파이썬만 가능)
# a_list = [i for i in range(1,11)]
# print(a_list)

# 리스트 값 삭제 : del(특정위치제), pop(맨 뒤 삭제, 특정위치 삭제), remove(특정 데이터값 삭제), clear(전체 삭제)
c_list = [1,2,3,4,6,7,8,9,10]
del c_list[2] 
print(c_list)

c_list.pop()
print(c_list)

c_list.pop(1)
print(c_list)

c_list.remove(7)
print(c_list)

c_list.clear()
print(c_list)