# 파이썬만 가능
num = 7
if 10>= num >= 7 :
    print("10에 해당되는 숫자이다")

# 일반적인 방법
if 10>= num and num >=0 :
    print("10")

# 345 봄 678여름 91011 가을 12.1.2 겨울
num = int(input("숫자를 입력하세요 :"))
if 5 >= num >= 3 :                 
    print("봄의 계절입니다.")
elif num >= 6 and num <= 8 :   
    print("여름의 계절입니다.")
elif 9 <= num <= 11 :                 
    print("가을의 계절입니다.")
else :                                  
    print("겨울의 계절입니다.")


