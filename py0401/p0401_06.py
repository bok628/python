a_list = [1,2,3,4,"홍길동",5]

# 리스트 삭제 명령어
del a_list[0] # 위치(index) 삭제
a_list.pop() 
print(a_list)
a_list.pop(2)
print(a_list)

a_list.remove(2) # 데이터 값 삭제
a_list.remove("홍길동")
print(a_list)

a_list.clear()  # 모두 삭제
print(a_list)

# 리스트 추가 명령어
a_list.append(1)
print(a_list)

a_list.insert(0,50)
print(a_list)

a_list.extend([10,11,12])  # 리스트 추가

print(a_list)

# 리스트 수정 
a_list[0] = "유관순"
print(a_list)

# 리스트 출력
for a in a_list :
    print(a)
    
# 리스트에 여러 데이터 묶음으로 추가 가능(리스트 안에 리스트 추가 가능)
a_list.append(['컴공','소웨','무역'])
print(a_list)

# 리스트 길이
print(len(a_list))

# 리스트 안에 해당 값의 개수 파악 : list.count(해당 값)
s_list = [1,2,3,2,2,2,1,1,3,3,4,5,7,7,7,7,7,10,9,8]
print("{} : {}".format(1,s_list.count(1)))

count = 0
for s in s_list :
    if s == 1 :
        count += 1
print(count)

# 리스트 정렬 (순차정렬, 낮은순정렬)
s_list.sort()
print(s_list)
s_list.sort(reverse = True)  # 역순정렬, 높은순정렬
s_list.reverse()             # 역순정렬, 높은순정렬
print(s_list)

