# list = [1,2,3,1,2,3,5,6,8,9,10,1,2]
# dic = {}

# for i in list :
#     if i not in dic :
#         dic[i] = 0
#     dic[i] = dic[i] + 1 # 키가 몇 개 존재하는지 개수 파악
#     # dic[i] += "ㅁ"

# for i,d in enumerate(dic):
#     print(f"{i} : {dic[d]}")
    
# # dic = {1:3, 2:3, 3:2, 5:1, 6:1, 8:1, 9:1, 10:1}

list = ["지드래곤","황가람","제니","에스파","리쿠",
        "지드래곤","리쿠","리쿠","황가람","황가람",
        "지드래곤","지드래곤","지드래곤","황가람","황가람",
        "제니","제니","제니","제니","제니",
        "에스파","지드래곤","에스파","황가람","에스파",
        "리쿠","리쿠","리쿠","리쿠","리쿠"
        ]

singer = {}

# 각각의 가수가 몇번 존재하는지 출력
for i in list :
    if i not in singer :
        singer[i] = 1
    else :
        singer[i] = singer[i] + 1

for i,v in singer.items() :      # 튜플 형태 - item
# for i,v in enumerate(singer) 
    print(f"{i} : {v}")
    
