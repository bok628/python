i_list = [1,2,3,4,5,1,2,10]
dic = {"no":1,"name":"홍길동","kor":100,"eng":90,"math":80,"total":270}
print(dic)

txt_list = ['안녕','반가워','다음','내일','봐','잘','지내','봐요']

# 얕은 복사, 깊은 복사
new_list = i_list     # 얕은 복사
new_list2 = [*i_list] # 깊은 복사



# # ZIP
# for i,t in zip(i_list,txt_list) :
#     print(i,t)
    
# # ZIP으로 리스트 생성
# new_list = list(zip(i_list,txt_list))
# print(new_list)
# # ZIP으로 dict 생성
# new_dic = dict(zip(i_list,txt_list))
# print(new_dic)                   # i_list에 동일한 데이터가 있으면 최근 txt_list로 출력(수정의 개념)


# # 딕셔너리 전체 출력
# for k in dic :
#     print(dic[k])
    
# for k,v in dic.items() :
#     print(k,v)

# # 리스트 전체 출력
# for i in i_list :
#     print(i)

# # 딕셔너리 정렬
# import operator
# dic_sort = sorted(dic.items(), key=operator.itemgetter(0)) # 0번째(key)를 기준으로 튜플형태로 정리
# print(dic_sort)
# # 리스트 정렬
# i_list.sort()
# print(i_list)
# i_list.sort(reverse = True)
# print(i_list)


# # 딕셔너리 개별 출력
# print(dic['no'])
# # ERROR : print(dic['kor'])
# print(dic.get('kor'))
# # 리스트 개별 출력
# print(list[0])

# # 딕셔너리 수정
# dic['name'] = "유관순"
# print(dic)
# # 리스트 수정
# list[0] = 100
# print(list)

# # 딕셔너리 삭제 - del dic["key"]
# del dic["no"]
# # 리스트 삭제 - del list[위치]
# del list[0]
# print(list)

# # 딕셔너리 추가
# dic['kor'] = 100
# print(dic)
# # 리스트 추가
# list.append(100)
# print(list)

# # 딕셔너리 keys,values 
# print(dic.keys())
# print(dic.values())
# print(dic.items())  # 튜플 형태(수정 X)

# if 'no' in dic :        # 딕셔너리를 비교 - key를 가지고 비교함
#     print("있습니다.")
    
# 1-10까지 리스트 내포를 이용한 리스트 생성
a_list = [i + 1 for i in range(10)]
print(a_list)

b_list = [0]*10
print(b_list)

c_list = [i for i in range(1,51) if i % 2 == 1]
print(c_list)

