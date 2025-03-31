# # while + 조건
# i = 0
# while i < 10 :
#     i = i + 1
#     print(i,end = " ")

# # for + 반복횟수 range(시작범위,끝범위 - 1, 증가수)
# for i in range(0,3,1) :
#     print()
#     print("hi")
    
# # 10번의 숫자를 입력받아, 합계 구하기
# sum = 0
# for i in range(10) :
#     num = int(input("숫자를 입력하세요 : "))
#     sum = sum + num
# print("합계 : ",sum)


# j = 0
# sum1 = 0
# while j < 10 :
#     number = int(input("숫자를 입력하세요 : "))
#     sum1 = sum1 + number
#     j = j + 1
# print("합계는 {}입니다.".format(sum1))

# # 로또 프로그램 - 6개 랜덤숫자와 입력숫자 6개를 출력 
# import random
# lotto = []
# my_input = []
# lotto_input = []

# for i in range(6) :
#     ran = random.randint(1,45) #중복가능
#     lotto.append(ran)
#     #lotto.append(random.randint(1,45))
    
#     num = int(input("숫자를 입력하세요(1-45) : "))
#     my_input.append(num)

# count = 0
# mylotto = []
# for j in range(0,6,1) :
#     for k in range(6) : 
#          if lotto[j] == my_input[k] :
#             count += 1
#             mylotto.append(lotto[j])
# print("랜덤숫자 : ",lotto)
# print("입력숫자 : ",my_input)
# print("겹치는 횟수 : {}개".format(count))
# print("겹치는 숫자 : ",mylotto)


# # random.sample(리스트,가져올 갯수)
# import random
# lotto1 = [i + 1 for i in range(45)]
# lotto_input = []
# m_input = []

# lotto_input = random.sample(lotto1,6)# 리스트에서 중복없이 6개를 가져옴.

# for i in range(6) :
#     numb = int(input("숫자 입력 : "))
#     m_input.append(numb)
# print("로또번호 : ", lotto_input)
# print("입력번호 : ", m_input)

# # 랜덤 숫자 6개 출력
# import random
# a_list = [ i + 1 for i in range(45) ]
# print(a_list)

# random.shuffle(a_list) # 위치 바꾸기
# print(a_list)

# print(a_list[:6]) # 앞자리 6개 출력

# 0 <= x < 1 사이의 랜덤 실수 : random.random()
import random
print(random.random()) #0.000000000000000 <= x <1.0000000000000000000

# # a_list에서 홀수값의 합계 구하기

# a_list = [i + 1 for i in range(10)]
# print(a_list)

# sum = 0
# for i in a_list :
#     if i % 2 == 1 :
#         sum += i
# print("홀수 합계 : ",sum)


# # 1-100까지의 숫자의 합을 구할 때 합계가 200을 넘을 때의 숫자를 출력하시오
# list = [ i + 1 for i in range(100) ]
# print(list)
# sum = 0
# for i in list :
#     sum += i
#     print(sum,i)
#     if sum >= 200 :
#         print("합계 : ",sum)
#         print("숫자 : ",i)
#         break

# list = [ i + 1 for i in range(100) ]
# sum = 0
# for i in list :
#     sum += i
#     if sum >= 200 :
#         break
# print(sum,i)
# print(f"i이전 : {}, sum : {}".format(i-1,sum-i))


# 입력한 숫자합이 50초과시로그램 종료 & 총합 구하기(입력한 숫자 중 5의 배수는 제외)
sum = 0

# while True :
#     num = int(input("숫자를 입력하세요 : "))
#     sum += num
#     if num % 5 == 0 :
#         sum -= num
#         print(f"입력한 숫자 : {num}, 5의 배수는 제외")
#     if sum > 50 :
#         print("프로그램 종료")
#         break
# print(sum)
    
# while True :
#     if sum < 50 :
#         num = int(input("숫자를 입력하세요 : "))
#         if num % 5 == 0 :
#             print(f"입력한 숫자 : {num}, 5의 배수는 제외")
#             continue # 실행을 1번 중지
#         sum += num
#     else :
#         break
# print(f"합계 : {sum}")

# continue : 실행을 중지시키고 다시 for문 실행 ex)1,2,3-continue : 제외, 4,5,6
# pass : 실행할 구문이 없음. for문을 계속 반복                                        
# break : 반복문 완전 중지

# for i in range(10) :
#     if i % 2 == 1 : continue #pass,break 다 넣어보기
#     print(i)
    
# # 모양 출력                                      
# for i in range(10) :
#     for j in range(i+1) :
#         print("*",end = "")
#     print()
    
# a_list = [1,2,"사과",True,False,5,6,7,8,9,10]
# print(a_list)
# print(a_list * 3) # 3번 반복

# a_list[::2] # 2칸씩 건너뜀
# print(a_list)

# a_list[::-2] # 거꾸로 2칸씩 건너뜀
# print(a_list)

# a_list[::-1] # 역순 출력
# print(a_list)

# a_list[5] = 10
# print(a_list)

# # 값 변경시 끝범위 포함 ([m : n] - m~n까지 값 변경)
# a_list[1:2] = [100:200] 
# print(a_list)


# #2차원 리스트
# aa = [
#     [1,2,3],        #aa[0]
#     [4,5,6],        #aa[1]
#     [7,8,9]         #aa[2]
# ]
# print(aa[0])
# print(aa[0][2])

aa = [
    [1,2,3],        #[0][0],[0][1],[0][2]       
    [4,5,6],        #[1][0],[1][1],[1][2]
    [7,8,9]         #[2][0],[2][1],[2][2]
]
print(aa)

for i in range(3) :
    for j in range(3) :
        print(aa[i][j],end = "\t")
    print()

    
# # 1 2 3 4 5
# # 6 7 8 9 10
# #11 12 13 14 15
# #16 17 18 19 20
# #21 22 23 24 25
# list = [
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15],
#     [16,17,18,19,20],
#     [21,22,23,24,25]
# ]
# for i in range(5) :
#     for j in range(5) :
#         print(list[i][j],end = "\t")
#     print()

# #랜덤으로 섞여진 리스트 출력
# import random
# i = 0
# a_list = [i+1 for i in range(25)]
# random.shuffle(a_list)
# print(a_list)

# 5X5리스트 초기화
a_list = [[0] * 3 ] * 5               #얕은 복사
a_list = [[0]*5 for i in range(5)]    #깊은 복사
print(a_list)

for i in range(5) :
    for j in range(5) : 
        a_list[i][j] = 5 * i + (j + 1)
print(a_list)
  

# # 순차적 리스트 생성 > 리스트 섞기 > 2차원 초기화 리스트 생성 > 2차원 리스트에 랜덤리스트의 값을 입력
import random
sample_list =[i+1 for i in range(25)]
random.shuffle(sample_list)

# a_list = [[0] * 5 for i in range(5)]
# for i in range(5) :
#     for j in range(5) :
#         a_list[i][j] = sample_list[5*i + j]
    
# print(a_list)

# 5 X 5 리스트 출력
sample_list = [[0] * 5 for i in range(5)]

for i in range(5) :
    for j in range(5) :
        print(a_list[i][j],end = "\t")
    print()
    

sample_list = list() # 리스트 초기화
for i in range(5) :
    temp = []
    for j in range(5) :
        temp.append(0)
    sample_list.append(temp) #[ [0,0,0,0,0] ]
print(sample_list)