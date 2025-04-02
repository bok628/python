# # num1, num2, num3 값을 입력받아 합계&평균 구하기
# n1 = int(input("점수를 입력하세요 : "))
# n2 = int(input("점수를 입력하세요 : "))
# n3 = int(input("점수를 입력하세요 : "))

# def add(x,y,z) :
#     return x + y + z

# total = add(n1,n2,n3)
# avg = total / 3

# print(f"{n1},{n2},{n3},{total},{avg:.1f}")

# 함수 사용 1. 중복 코드 2. 소스가 복잡할 때 
# # 함수를 사용하여 두 수를 입력받아 두 수 사이의 합계 출력
# num1 = int(input("숫자 입력 : "))
# num2 = int(input("숫자 입력 : "))

# def add(x,y) :
#     if x > y :
#         x,y = y,x
#     sum = 0
#     for i in range(x, y+1) :
#         sum = sum + i
#     print("합계 : ",sum)
# print(add(num1,num2))

# # 입력을 5개 받아, 짝수만 모두 더한 값을 출력하시오

# def cal(n_list) :
#     sum = 0
#     for n in n_list :
#         if n % 2 == 0 :
#             sum += n
#     return sum

# n_list = [0] * 5
# for i in range(5) :
#     n_list[i] = int(input("숫자입력 : "))    

# result = cal(n_list)
# print("짝수의 합 : ",result)

# # 직사각형 넓이와 둘레 구하기
# def cal(r1,r2) :
#     # return r1 * r2,2 * (r1+r2)
#     result1 = r1 * r2
#     result2 = 2 * (r1+r2)
#     return result1, result2

# r1 = int(input("직사각형의 밑변 길이 : "))
# r2 = int(input("직사각형의 높이 : "))
# result1,result2 = cal(r1,r2)
# # print("직사각형의 넓이,둘레 : ",cal(r1,r2))
# print(f"넓이 = {result1}, 둘레 = {result2}")


# # 이름, 국어, 영어, 수학 점수를 입력받아 합계, 평균 출력하기
# def cal(kor,eng,math) :
#     total = kor + eng + math
#     avg = total / 3
#     return total,avg
    
# no = 1
# name = input("이름을 입력하세요 : ")
# kor = int(input("국어 점수를 입력하세요 : "))
# eng = int(input("영어 점수를 입력하세요 : "))
# math = int(input("수학 점수를 입력하세요 : "))
# total,avg = cal(kor,eng,math)
# print(f"합계 : {total}, 평균 : {avg:.2f}")

# students = [
#     {"no":1, "name":"홍길동","kor":100, "eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
#     {"no":2, "name":"유관순","kor":100, "eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
#     {"no":3, "name":"이순신","kor":100, "eng":100,"math":99,"total":299,"avg":99.67,"rank":2}
# ]

# def stu_print() :
#     for s in students :
#         print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
        

# print("1. 학생 성적 입력")
# print("2. 학생 성적 출력")
# choice = int(input("원하는 번호를 입력하세요 : "))
# if choice == 2 :
#     stu_print()
    
# # 지역변수 : 함수 안 변수 ex) 함수 내에서 100은 할당되고 사라짐.  전역변수 : 함수 밖 변수
# def cal(a,b) :
#     a = 100 # 지역변수 - 함수 내 일반변수는 함수를 벗어나면 사라짐 - bool int float string *예외 : 그룹변수 list,dic 등 
#     b = 200
#     # return a,b

# #함수 밖
# a = 10 # 전역변수
# b = 20
# print("함수 호출전 a,b : ",a,b)

# cal(a,b)
# print("함수호출 후 a,b : ",a,b)


# def cal(a_list) :
#     a_list[0] = 100
#     a_list[1] = 200

# a_list = [0,0]
# a_list[0] = 10
# a_list[1] = 10
# print("함수호출 전 a_list : ",a_list[0],a_list[1])

# cal(a_list)
# print("함수호출 후 a_list : ",a_list[0],a_list[1])

# s = {"no":1, "name":"홍길동","kor":100, "eng":100,"math":100,"total":300,"avg":100.0,"rank":1}

# # 매개변수로 일반변수 전달 - return
# def cal(ss) :            # 주솟값으로 함수 정의 => 수정하면 바로 출력됨
#     ss['kor'] = int(input("수정할 국어 점수를 입력하세요 : "))
#     ss['total'] = ss['kor'] + ss['eng'] + ss['math']
#     ss['avg'] = ss['total'] / 3
    
# print("[ 학생 성적 수정 ]")
# # 국어 점수 변경 함수
# cal(s)
# print("수정된 국어 점수 : ",s['kor'])


# # global 변수 : 전역변수
# def func1() :
#     global a  # 전역변수 호출
#     a = 20    # 지역변수

# a = 10
# print("a : ",a)
# func1()
# print("a : ",a)

# def cal(n1,n2) :
#     return n1 + n2

# def cal2(n1,n2,n3) :
#     return n1 + n2 + n3

# def cal3(n1,n2,n3,n4) :
#     return n1 + n2 + n3 + n4

# n1 = 10
# n2 = 20
# n3 = 30
# n4 = 40

# result = cal(n1,n2)
# print(result)

# result2 = cal2(n1,n2,n3)
# print(result2)

# # 가변매개변수 사용 - 전개 연산자
# def cal(*num) :
#     result = 0
#     for n in num :
#         result += n
#     return result

# print("2개 합 ㅣ ",cal(1,2))
# print("3개 합 ㅣ ",cal(10,20,30))
# print("4개 합 ㅣ ",cal(1,2,3,4))

# # 키워드 매개변수 - 키워드변수 ( b = 10 )는 마지막에
# def cal(a,b = 10) :     
#     return a + b

# print(cal(1))


# 가변매개변수 + 키워드변수
def cal(b = 10,*a) :
    result = b
    for i in a :
        result += i
    return result
print(cal(1,2,3,4,5))                   # 15

def cal(*a, b = 10) :
    result = b
    for i in a :
        result += i
    return result
print(cal(1,2))                         # 13

def cal(*a, b = 10) :
    result = b
    for i in a :
        result += i
    return result
print(cal(1,2,b = 100))                 # 103