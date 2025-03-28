# # 파이썬만 가능한 로또 프로그램 생성 방법 
# import random
# a_list = random.sample(range(1,45+1),6)  #range(최소범위,최대범위,n개 추출)
# print(a_list)

# #
# for i in range(0,1000) :
#     print("{:03d}".format(i),end = " ")

# 구구단 출력
for i in range(1,10) :
    for j in range(2,10) :
        print("{} X {} = {}".format(j,i,i*j),end = "\t") #,end = "  "
    print()
    