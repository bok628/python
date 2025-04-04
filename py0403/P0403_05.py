# LOTTO
import random
lotto = [i + 1 for i in range(45)]
lotto2 = [i + 1 for i in range(45)]
my_lotto = [0] * 6
win_lotto = []

def lotto_mix() :
    global lotto,lotto2
    random.shuffle(lotto)
    lotto2 = [i + 1 for i in range(45)]
    
lotto_mix()
while True :
    print("\n[로또 프로그램]")
    print("-"*30) 
    print("1. 로또프로그램 재실행")
    print("2. 로또번호 입력")
    print("3. 로또번호 당첨확인")
    print("4. 로또리스트 확인")
    print("5. 입력한 로또번호 확인")
    print("0. 프로그램 종료")
    print("-"*30)
    
    choice = int(input("원하는 번호를 입력하세요. >>"))
    
    if choice == 1 :
        lotto_mix()
        print("[ 로또프로그램 재실행 ]")
        print("재실행이 완료되었습니다.")
        print()
    elif choice == 2 :
        print("[ 로또번호 입력 ]")
        print("-"*45)
        for i in range(45) :
            if i % 7 != 0 : 
                print(lotto2[i],end="\t")
            else :
                print()
                print(lotto2[i],end = "\t")
        print()
        for i in range(6) : 
            num = int(input("로또번호를 입력하세요.(0.이전화면이동) : "))
            my_lotto[i] = num
            if num == "0" :
                break 
        
        
    elif choice == 3 :
        print("[ 로또번호 당첨확인 ]")
        print("-"*50)
        count = 0
        if my_lotto = [0] * 6 :
            print("입력한 로또번호가 없습니다.")
            break
        for i in range(6) :
            for j in range(6) :
                if lotto[i] == my_lotto[j] :
                    count += 1
                    win_lotto.append(i)
        print(f"로또번호 : {lotto[:6]}")
        print(f"입력한 로또번호 : {my_lotto}")
        print(f"당첨된 로또번호 : {win_lotto}")            
        print(f"당첨된 로또번호 개수 : {count}")
    elif choice == 4 :
        print("[ 로또리스트 확인 ]")
        print(lotto)
        print()
    elif choice == 5 :
        if my_lotto = [0] * 6 :
            print("입력한 로또번호가 없습니다.")
            continue
        print("[ 입력한 로또번호 확인 ]")
        print(my_lotto)
    elif choice == 0 :
        print("프로그램 종료")
        break