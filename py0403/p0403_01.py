# 로또 프로그램
# 6개 랜덤 번호 생성 -> 6개 입력한 번호 생성 -> 당첨번호 확인 -> 출력

import random
ran = random.randint(1,45)
ran.sample(6)
# 숫자맞추기 프로그램
# 1차원 리스트(1-25) 생성 -> 숫자 섞기 -> 2차원 리스트에 1차원 리스트 값 넣기 -> 번호 입력 -> 입력한 번호에 맞는 위치 X 출력
import random

# 성적처리 프로그램
# 데이터 생성(딕셔너리) -> 출력화면 
# -> 1.학생성적입력(학생번호 자동생성 - 성적입력 무한반복으로 실행 - 이전화면 이동구현 - 점수입력에 대한 체크(0~100의 숫자인지)
# -> 2.학생성적출력(상단타이틀 출력 - 학생별 성적 출력)
# -> 3.학생성적수정(수정하고자 하는 학생검색 - 수정하려는 과목 선택 - 검색이 되지 않았을 경우 구현)
# -> 4.학생성적정렬(이름으로 순차정렬 - 합계로 순차정렬) 
# -> 5.학생성적검색(찾고자 하는 학생 검색 후 학생이 존재하면 화면 출력) 
# -> 6.등수처리(합계를 기준으로 등수처리 진행)
# -> 0.종료