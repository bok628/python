# # 문자열
txt = ","
txt2 = txt.join("안녕하세요")
print(txt2)

a = "1234"
    
# while True :
#     my_input = input(" 숫자 입력 : ")
#     if my_input.isdigit : # 숫자로 변환
#         print(" 숫자로 변환 가능합니다.")
#     else :
#         print("숫자가 아닙니다. 다시 입력하세요")


print('1234'.isdigit())     # 숫자인지
print('abc'.isalpha())      # 알파벳인지 - 한글안됨
print('abc123'.isalnum)     # 모두 숫자인지 
print('abc'.islower())
# # map
# score = ['100','99','90']
# # 함수
# def cal(x) :
#     return int(x) * 100
# s_list = list(map(int,score))
# print(s_list)


# sum = 0
# for s in score :
#     sum += int(s)
# print("힙계 ㅣ ",sum)

# # DataBase는 리스트를 저장할 수 X
# txt = "1,홍길동,100,100,100,300,100.0,1"
# txt_list = txt.split(",")
# txt_list[3] = 90
# print(txt_list)
# txt = ""
# txt = "a,b,c,d,안녕,반가워"
# txt_list = txt.split(",")      # ,로 구분
# print(txt_list)

# txt = '  안녕하    세요  '
# print(txt.replace(" ",""))   # 특정 글자 -> 원하는 글자로 대체

# txt2 = "파이썬 공부가 쉬워요~ 너무 쉬워요. 파이썬은 재미있어요."
# print(txt2.replace("파이썬","자바"))
# print(txt.strip())           # 앞뒤 글자(공백) 제거 - strip 오른쪽 공백 제거 - rstrip(), 왼쪽 공백 제거 - lstrip()

# txt3 = "----파이썬 ---"
# print(txt3.strip("-"))
# print(txt3.replace("-",""))


# txt = "파이썬 공부가 쉬워요~ 너무 쉬워요. 파이썬은 재미있어요."
# print(txt.count("파이썬")) # 문자열의 특정 글자 개수
# print(txt.count("요"))
# print(txt.find("공부"))    # 공부의 위치를 알려줌.
# print(txt.find("자바"))    # 특정 글자가 문자열에 존재하지 않을 때 : -1

# t = "aaa.py"
# print(t.endswith("py"))    # 끝나는 말이 동일하면 True 

# txt = "안녕하세요"
# a_list = [1,2,3,4,5]

# print(txt[1])        # 문자열 : 인덱스(위치) 가짐
# print(a_list[1])

# print(a_list[1:3])   # [2, 3]
# print(txt[1:3])      # 녕하
# print(txt[2:])
# print(txt[::-1])

# print(txt*3)
# print(len(txt))      # 5 (글자 길이 출력)

# txt = "abBBcDd hello world"      # 대소문자
# print(txt.upper())   # 대문자
# print(txt.lower())   # 소문자
# print(txt.swapcase()) # 대문자 -> 소문자, 소문자 -> 대문자
# print(txt.title())   # 단어 첫글자 대문자   