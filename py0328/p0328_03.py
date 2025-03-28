# # 반복문을 사용하여 1~10까지 출력
# for i in range(1,11) :
#     print(i)
    
# # 문자 선택 연산자
# a = "안녕하세요"
# print(a[2])
# print(a[1:4])
# print(a[::-1])
# print(a[::32])
# print([])
# # 슬라이싱
# list_b = [1,2,3,4,5]
# print(list_b[1:4])
# print(list_b[:4])
# print(list_b[3:])
# print(list_b[::2]) # 2개씩 증가해서 출력

# # 리스트 문법
# print(list_b[::-1]) # 역순으로 출력
# print(list_b[:-1])

# print(len(list_b))  # 리스트 개수 확인
# print(len(a))  # 문자열 길이
 
for i in range(1,11,2) :
    print(i, end = " ") # 줄바꿈 없이 출력

# 1-100까지의 합 구하기
sum = 0
for i in range(1,101) :
    sum = sum + i
    
print("\n1-100까지 합계 : {}".format(sum)) 
    
    
# 합계가 100이 넘는 위치의 숫자 구하기
sum = 0
i = 0
for i in range(1,100) : 
    sum = sum + i
    if sum >= 100 :
        print("i : {}, sum : {}".format(i, sum))
        break
print("1-100까지의 합계 : {}".format(sum))

