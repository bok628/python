# 파일 쓰기 - w : 파일이 없어도 가능(파일 생성하여 쓰기모드)
f = open("aa.txt","w",encoding="utf-8")
while True :
    line = input("입력 : ")
    if line.lower() == "x" : 
        break
    f.write(line + "\n")
f.close()

# 파일 이어쓰기
f = open('py0404/memo.txt',"a",encoding="utf-8")
f.write("1,홍길동")
f.close()




