# 문서 읽어오기 - r
# 일반파일 읽어오기 - rb
f = open('py0404/a.jpg',"rb")
fData = f.read()
f.close()
print("파일 읽어오기 완료")

# 문서저장 - w,a
# 파일저장 - wb
# 폴더 존재 확인 : os.path.exists()
# 1개 폴더 생성 명령어 : os.makedir() - C:/down1/aaa
# 여러개 폴더 생성 명령어 : os.makedirs() - C:/down1/aaa/a.jpg

import os
# 폴더가 존재하지 않을 때, 폴더 생성
if not os.path.exists("c:/down1") :
    os.makedirs("c:/down1")
ff = open("C:/down1/b.jpg","wb")     # 폴더가 존재하지 않을 경우, 에러
len = ff.write(fData)
print(f"파일크기 : {len} 바이트")
ff.close()

print("파일 저장완료")