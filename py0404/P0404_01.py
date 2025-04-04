# #def 함수명(매개변수) : return 값
# def add(a,b) :
#     return a + b

# print(add(10,20))

# def add(a,b) :
#     a + b               # return 필요
# print(add(10,20))       # None으로 출력

# def func(a,b,c) :
#     return max(a,b,c)   # 최댓값 찾기

# print(max(10,5,20))

# # 람다식 lambda -> 함수 축약형 : 주로 map()과 사용
# # lambda 매개변수 : 값
# def func2(a) :
#     return a * 20
# lambda a : a*20

# # map(함수, 리스트) - 리스트에 함수를 적용해서 다시 리스트로 변환
# list 모든값에 제곱하여 리스트 생성
# def func(x) :
#     return x ** 2

# a_list = [1,2,3,4,5]  
# print(list(map(func,a_list)))

# # lambda + map
# print(list(map((lambda x : x**2),a_list)))

# filter() : 리스트에 함수를 적용해서 조건에 맞는 것만 다시 리스트로 반환

# filter 함수 관련
a_list = [1,2,3,4,5]
def func(x) :
    if x % 2 == 0 :
        return x

aaa_list = list(filter(func,a_list))

c_list = list(filter(lambda x : x % 2 == 0, a_list))
print(c_list)

print(aaa_list)
aa_list = []
for i in a_list : 
    if i % 2 == 0 :
        aa_list.append(i)
print(aa_list)



students = [
    {"no":1, "name":"홍길동","kor":100, "eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2, "name":"유관순","kor":100, "eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
    {"no":3, "name":"이순신","kor":100, "eng":100,"math":99,"total":299,"avg":99.67,"rank":2}
]

# sorted 기존의 리스트를 유지하고 새로운 리스트를 생성 (복사본)
s_list = sorted(students,key = lambda x : x['name'])
print(s_list)

# print(students.sort())      # 딕셔너리는 정렬 불가 (크기 비교 X)
# dict 정렬
# sort() 기존의 리스트 값을 변경시킴
print(students)
print("-"*60)
students.sort(key = lambda x : x['total'])
print(students)
students.sort(key = lambda x : x['name'])           # 이름으로 순차정렬
print(students)
students.sort(key = lambda x : x['name'], reverse = True)
print(students)


alist = [20,50,10,40,90]
alist.sort()                # 순차정렬
print(alist)
alist.sort(reverse = True)
print(alist)

