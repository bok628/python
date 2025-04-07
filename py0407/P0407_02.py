# 에러(발생시 프로그램 종료) - 구문 & 런타임에러
# 구문에러(오타) : priint("")
# 런타임에러 : 실행시 에러 
# a = [1,2,3] 
# for i in range(5): print(a[i])

# 에러처리 방법
# 예외처리 & if 조건문
# 1. if 조건문
# print("1. 학생성적출력")
# choice =input("원하는 번호를 입력하세요. >> ")
# if choice.isdigit() :
#     choice = int(choice)
# else : 
#     print("숫자만 입력이 가능합니다.")
# print("입력한 번호 : ",choice)

# 2. 예외처리 ( try: ~  exception : ~) - 강제로 프로그램 종료되는 것을 해결, 에러에 대한 문제점 확인
print("1. 학생성적출력")
choice =input("원하는 번호를 입력하세요. >> ")
try : 
    choice = int(choice)
except Exception as e : # 에러에 대한 문제점 확인할 때
    print("숫자만 입력이 가능합니다.")
    print(e)
print("입력한 번호 : ",choice)

