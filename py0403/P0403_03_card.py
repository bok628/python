# import math
# a = 3.141592
# b = 3.51582

# # 올림(소수 첫째자리에서 올림)
# print(math.ceil(a))
# # 버림(소수 첫째자리에서 버림)
# print(math.floor(a))

# # 반올림 (자리수 지정 가능)
# print(round(a,4))       # 넷째자리까지 반올림 - 3.1416
# print(round(b,3))       # 셋째자리까지 반올림 - 3.516

# # a를 셋째자리에서 올림하여 소수 2자리까지 표시해서 출력하기
# # a * 100 / 100
# print(math.ceil(a * 100) / 100)

# # b를 5자리에서 올림하여 출력
# print(math.ceil(b * 10000) / 10000)

# math 안에 있는 함수 출력
# print(dir(math))

# import math
# import random
# print(random.random())

# # 1-45 중 랜덤추출
# print(random.randint(1,45))

# a_list = [1,2,3,4,5]

# print(random.sample(a_list,2))

# random.shuffle(a_list)
# print(a_list)

# 카드 ( SPADE-4 > DIAMOND-3 > HEART-2 > CLOVER-1 )
# 번호 1-A , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11-J, 12-Q , 13-K
# 카드 총 개수 : 4 * 13 = 52장

# # 리스트-딕셔너리
# cList = [
#     {"shape":"SPADE","no":1},
#     {"shape":"SPADE","no":2}
# ]

import random

cList = []
sh = ["CLOVER", "HEART", "DIAMOND", "SPADE"]
no = ["","A","2","3","4","5","6","7","8","9","10","J","Q","K"] # 숫자로 표현하기 위해 0번째에 공백 추가



# 카드 생성
for i in range(52) :
    cList.append({"shape" : i // 13, "no" : i%13 + 1})

# 카드 랜덤으로 섞기
random.shuffle(cList)

# myCard, youCard
# 5장 입력
myCard = []
youCard = []

# 카드 5장씩 배부
for i in range(5) :
    myCard.append(cList[i])

for i in range(5,10) :
    youCard.append(cList[i])
    
# my카드 출력 - 번호에 해당되는 글자를 출력
print("[ my card ]")
for i in myCard :
    print(f"[ {sh[i['shape']]},{no[i['no']]} ]")

# you카드 출력
print("[ 상대카드 ]")
for i in youCard :
    print(f"[ {sh[i['shape']]},{no[i['no']]} ]")

# 내카드,상대카드 비교하여 승리 or 패배 or 무승부 출력하기
# 숫자만 비교해서 숫자가 높은게 이기는 것.

score = {"myWin":0,"youWin":0,"draw":0}

for i in range(5) :
    if myCard[i]['no'] > youCard[i]['no'] :
        score['myWin'] += 1
    elif myCard[i]['no'] < youCard[i]['no'] :
            score['youWin'] += 1
    else :
        score['draw'] += 1
    
print("[ 카드 승부 확인 ]")
print(f"승리 : {score['myWin']}, 패배 : {score['youWin']}, 무승부 : {score['draw']}")
    


# 승리한 카드 출력
# 무승부 카드 출력
# 패배 카드 출력
score = [0] * 5

for i in range(5) :
    if myCard[i]['no'] > youCard[i]['no'] :
        score[i] = 2
    elif myCard[i]['no'] < youCard[i]['no'] :
            score[i] = 1
    else :
        score[i] = 0
    
print("[ 카드 승부 확인 ]")
print(f"승리 : {score.count(2)}, 패배 : {score.count(1)}, 무승부 : {score.count(0)}")

print("승리 카드")
print("-"*20)
for i,c in enumerate(myCard) :
    if score[i] == 2 :
        print(f"[{sh[c['shape']]},{no[c['no']]}]",end = ",")
# i = 0
# while i <5 :
#     i += 1
#     for m in myCard :
#         for y in youCard :
#             myWin = 0
#             youWin = 0
#             tie = 0
#             if m['no'] > y['no'] :
#                 myWin += 1
#             elif m['no'] == y['no'] :
#                 tie += 1
#             elif m['no'] < y['no'] :
#                 youWin += 1

# if myWin > youWin :
#     print("승리")
# elif youWin > myWin :
#     print("패배")
# elif myWin == youWin :
#     print("무승부")
# print()
# print(f"내가 이긴 횟수 : {myWin}, 상대가 이긴 횟수 : {youWin}, 무승부 {tie}")


# 11-J, 12-Q, 13-K, 1-A
# # 카드 전체 출력
# for c in cList :
#     print(c['shape'],c['no'])
    