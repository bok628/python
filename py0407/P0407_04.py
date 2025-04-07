# # finally : 모두 실행
# try :
#     f = open("info.txt","w",encoding="utf-8")
#     raise NotImplementedError
# except Exception as e :
#     print(e)
# finally :
#     f.close() 
    
# a_list = [1,2,3,4,5]
# try :
#     print(a_list[5])
# except ValueError :     # ValueError만 처리함
#     print("출력되어야 함")
# except IndexError :     
#     print("인덱스에러")
# except Exception as e :      # 모든 예외처리 가능
#     print(e)
#     print("모든 예외처리가 다 가능함.")

# print(7)        # 위에서 오류가 났기 때문에 출력 X => try구문 사용
# print(8)

print(1)
print(2)
raise NotImplementedError("프로그램 미구현 - 수정부분이 프로그램 진행해야 함")  # 에러 구문 생성
print(3)

