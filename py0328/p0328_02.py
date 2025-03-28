# for 반복문
for i in range(3) : # 0부터 시작 => 3번 반복
    print("안녕하세요")

# range(시작번호, 마지막번호 +1, 간격)
for i in range(1,11,2) : #range(1,11,2) 1부터 10까지 실행, 2씩 증가하면서 실행
    print("안녕", i)

# range => list로 대체
a_list = [1,2,3,4,5]
for i in a_list :
    print("안녕", i)   