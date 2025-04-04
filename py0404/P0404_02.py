# 파일 입출력 : 파일열기 -> 파일읽기,파일쓰기 -> 파일닫기 f.close()
# 변수명 = open("파일명","r")
# r : 읽기 , w : 쓰기 , a : 추가, b : 이진파일(파일복사)
# f = open("a.txt","r")
# f = open("a.txt","w")
# f = open("a.txt","a")

# 파일읽기 - readlines() : 모두 읽어오기
# f = open("a.txt","r",encoding="utf-8")
# lines = f.readlines()
# for line in lines :
#     print(line.strip())
# f.close()

# # read()
# f = open("a.txt","r",encoding= "utf-8")
# # print(type(f))
# for line in f :
#     print(line.strip()) # 공백제거
# f.close()

# 파일읽어오기 - 절대경로 : 경로가 다를 때
# # f = open("C:/workspace/python/a.txt","r",encoding= "utf-8")
# f = open("py0404/b.txt","r",encoding="utf-8")

# for line in f :
#     print(line.strip())
# f.close()  # 여러 파일 열 때 필수


# f = open("C:/workspace/python/a.txt","r",encoding= "utf-8")
# while True :
#     line = f.readline()
#     if not line : 
#         break
#     print(line.strip())
# f.close()   

# 뉴스 출력
f = open("py0404/news.txt","r", encoding= "utf-8")
for line in f :
    print(line.strip())
f.close()