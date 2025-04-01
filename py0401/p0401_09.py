# # set -> 중복을 제거해서 키를 확인
# myset1 = {1,2,2,3,3,3,5,5,7}  # 키만 존재
# print(myset1)

# menu_list = ['삼각김밥','바나나','삼각김밥','사과','바나나','도시락','삼각김밥']
# print(set(menu_list)) # list타입 -> set타입으로 변경해서 확인

# # 
# list = [1,2,3,4,5]
# # list2 = ['10,100', '10,200', '10,300', '10,400', '10,500']
# list2 = ["{:,d}".format((i + 100) * 100) for i in list] # {:,d} - 천단위 표시
# print(list2)

# # 리스트 내포 : if + 조건 가능(한줄만)
# n_list = [i for i in range(1,51) if i%2 == 1]
# print(n_list)

# # 2개의 리스트를 출력.
# n_list = ['홍길동', '유관순', '이순신', '강감찬', '김구']
# t_list = [100,99,89,79,100]
# for n,t in zip(n_list, t_list) :
#     print(f"{n} : {t}점")


