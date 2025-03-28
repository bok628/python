# # 3가지 이상 조건 : elif
# # 음수, 0, 양수
# num = int(input("숫자를 입력하세요 : "))
# if num > 0 :
#     print("양수")
# elif num == 0 :
#     print("0")
# else :
#     print("음수")

# # 60점 이상 : 합격, 60점 미만 : 불합격
# grade = int(input("성적을 입력하세요 : "))
# if grade >= 60 :
#     print("합격입니다.")
# else :
#     print("불합격입니다.")
    
# # 70이상 합격, 60~69 재시험, 60 미만 불합격
# grade1 = int(input("성적을 입력하세요 : "))
# if grade1 >= 70 :
#     print("합격입니다.")
# elif grade1 >= 60 :
#     print("재시험")
# else :
#     print("불합격입니다.")

# # 90점 이상 A, 80점 이상 B, 70점 이상 C, 60점 이상 D, 60점 미만 F
# score = int(input("점수를 입력하세요 : "))
# if score >= 90 :
#     print("A",end = "")
#     if score >= 97 :
#          print("+")
#     elif score >= 93 : pass
#     else : 
#         print("-")
# elif score >= 80 :
#     print("B",end = "")
#     if score >= 87 :
#         print("+")
#     elif score >= 83 :
#         pass
#     else :
#         print("-")
# elif score >= 70 :
#     print("C",end = "")
#     if score >= 77 :
#         print("+")
#     elif score >= 73 :
#         pass
#     else :
#         print("-")
    
# elif score >= 60 :
#     print("D",end = "")
#     if score >= 67 :
#         print("+")
#     elif score >= 63 :
#         pass
#     else :
#         print("-")
# else :
#     print("F")

# #줄바꿈 없이 출력하기
# print("hi")
# print("hello")

# print("hi",end = "")
# print("hello")
