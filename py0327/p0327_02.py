# 달러 -> 원화 환산하여 출력
# $1 = 1467원
# mon = int(input("달러를 입력하세요 : "))
# won = mon*1467
# print("입력한 달러 : {} 한화 : {}".format(mon,won))

# #:.2f - 소수점자릿수 출력 :,d - 천단위 출력
# print("입력한 달러 : {:,d} : {:,d}".format(mon,won))

# 1759원을 동전으로 변경 (500원 3, 100원 2, 50원 1, 10원 2, 1원 9)
mon = int(input("동전으로 변경할 금액을 입력하세요 : "))
ch500 = mon // 500
ch100 = (mon % 500) // 100
ch50 = ((mon % 500) % 100) // 50
ch10 = (((mon % 500) % 100) % 50) // 10
ch1 = (((mon % 500) % 100) % 50) % 10
print("500원\t100원\t50원\t10원\t1원")
print("-"*40)
print("{}\t{}\t{}\t{}\t{}".format(ch500,ch100,ch50,ch10,ch1))

# 반지름(radius)을 입력받아, 원의 넓이를 구하는 프로그램
# 원의 넓이(dimension) = 3.14 * 반지름**2
# 원의 둘레(circumference) = 2 * 3.14 * 반지름
rad = int(input("원의 반지름을 입력하세요 : "))
ans1 = 3.14 * (rad**2)
ans2 = 2 * 3.14 * rad
print("원의 넓이 : {:.2f}cm^2\n원의 둘레 : {:.2f}cm".format(ans1,ans2))

# 직사각형의 가로, 세로 길이를 입력받아 넓이와 둘레를 구하시오
garo = int(input("직사각형의 가로 길이를 입력하세요 : "))
sero = int(input("직사각형의 세로 길이를 입력하세요 : "))
ans1 = garo * sero
ans2 = 2 * (garo + sero)
print("직사각형의 넓이 : {}cm^2\n직사각형의 둘레 : {}cm".format(ans1, ans2))

# 직각삼각형
garo = int(input("삼각형의 밑변의 길이를 입력하세요 : "))
height = int(input("삼각형의 높이를 입력하세요 : "))
wide = (garo * height) / 2
print("삼각형의 넓이 : {:.1f}cm^2".format(wide))