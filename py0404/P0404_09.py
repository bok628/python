# a_list = ['홍길동','홍길순','홍길자','이순신','김유신','김구','순신스']

# while True :
#     name = input("찾고자 하는 이름을 입력하세요 : ")
#     temp = 0
#     for a in a_list :
#     #     # if name == a :      # 이름과 a가 일치할 때만
#         if name in a :   # 입력한 글자가 이름에 포함되었을 때
#             temp = 1 
#             print(f"{name}으로 검색된 {a}을(를) 찾았습니다.")
#     if temp == 0 :
#         print(f"{name}을 찾지 못했습니다. 다시 입력하세요.")
    
        


# # 파일 불러오기
# students = []
# with open("py0404/stu.txt","r",encoding = "utf-8") as f :
#     data = f.readline()
#     if not data :
#         break
#     s = data.strip().split(",")
#     students.append([{"no" : int(s[0]), "name" : (s[1])}])