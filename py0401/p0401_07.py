# 리스트 자리수 출력
num = [273,103,5,32,65,9,72,800,99]
sum = 0

# 자리수 : 3 값 : 273
# 자리수 : 3 값 : 103
# 자리수 : 1 값 : 5

for n in num :
    value = n
    length = len(str(n))
    print(f"자리수 : {length} 값 : {value}")

# 100이상의 숫자만 출력 & 합계
for n in num :
    if n >= 100 :
        print(n)
        sum += n

print("합계 : ",sum)


# 딕셔너리 생성 {키값:value값}
dic1 = {1:"a",2:"b",3:"c"}
print(dic1)

students_list = [1,"홍길동",100]
students = {"no":1,"name":"홍길동","kor":100}
print(students)

stu = {"학번":1000, "이름":"홍길동", "학과":"컴퓨터학과"}
print(stu)

# 딕셔너리 추가
dic = {}
dic["no"] = 1
dic["name"] = "홍길동"
dic["kor"] = 100
print(dic)

# 딕셔너리 삭제 - del dic[key값]
del dic["no"] 
print(dic)

# 딕셔너리 수정
dic["name"] = "이순신"
print(dic)

# 딕셔너리 출력
print(dic)
# print(dic["total"])
print(dic.get("total")) # 없으면 None으로 출력

# 딕셔너리 key값 or value값을 리스트 형태로 출력하기
print(dic.keys())
print(dic.values())

# 딕셔너리값을 tuple('name', '이순신')형태로 출력
print(dic.items())

# 전체 출력 - 키, 값 모두 출력
for i,value in enumerate(dic) :
    print(f"{i} : {value}")

# 키값만 출력.
for key in dic :
    print(key)
    print(dic[key])
    
if 'name' in dic : 
    print("키값이 존재합니다.")
    
if 'no' in dic :
    print(f"no : {dic['no']}")
else : 
    print("no 키는 존재하지 않습니다.")
