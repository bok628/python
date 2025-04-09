# 파일 읽어오기

# with open("py0404/stu.txt","r",encoding = "utf-8") as f :
f = open("py0404/stu.txt","r",encoding = "utf-8")
# 1줄씩 읽기 : 반복문을 실행
students = []
while True :
    data = f.readline()
    if not data :
        break
    s = data.strip().split(",")
    students.append({"no" : int(s[0]),"name" : s[1],
                     "kor" : int(s[2]),"eng" : int(s[3]),"math" : int(s[4]),
                     "total" : int(s[5]),"avg" : float(s[6]),"rank" : int(s[7])})

f.close()

print(students)