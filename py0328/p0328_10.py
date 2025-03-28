fruits = ['사과','배','딸기','바나나','멜론']
for fruit in fruits :
    print(fruit)

# scores = [65,90,100,50,88]
# for s in scores :
#     print(s,end = " ")

# enumerate : index 번호 부여
i = 0
for i,fruit in enumerate(fruits) :
    if len(fruits) - 1 != i :
        print("{}. {}".format(i+1, fruit),end = ", ")
    else :
        print("{}. {}".format(i+1, fruit),end = "")

